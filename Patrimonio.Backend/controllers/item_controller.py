from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from datetime import datetime
from models.physical_location_model import PhysicalLocation

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    assetCode = Column(String)
    description = Column(String)
    acquisitionDate = Column(DateTime)
    acquisitionMethod = Column(String)
    supplier = Column(String)
    physicalLocationId = Column(Integer)
    oldPhysicalLocationId = Column(Integer)
    imageUrl = Column(String)
    status = Column(String)
    inventoried = Column(Boolean, default=False)
    reference = Column(String)
    observation = Column(String)
    itemChanged = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind=engine)

item_bp = Blueprint('item', __name__, url_prefix='/item')

def format_item(item, db):
    physicalLocation = db.query(PhysicalLocation).filter(PhysicalLocation.id == item.physicalLocationId).first()
    oldPhysicalLocation = db.query(PhysicalLocation).filter(PhysicalLocation.id == item.oldPhysicalLocationId).first()

    return {
        'id': item.id,
        'assetCode': item.assetCode,
        'description': item.description,
        'acquisitionDate': item.acquisitionDate.isoformat() if item.acquisitionDate else None,
        'acquisitionMethod': item.acquisitionMethod,
        'supplier': item.supplier,
        'physicalLocation': {
            'id': physicalLocation.id,
            'acronym': physicalLocation.acronym,
            'active': physicalLocation.active,
            'observation': physicalLocation.observation,
            'module': physicalLocation.module,
            'level': physicalLocation.level,
            'code': physicalLocation.code,
            'description': physicalLocation.description,
            'managementUnit': physicalLocation.managementUnit,
            'createdAt': physicalLocation.createdAt.isoformat(),
            'updatedAt': physicalLocation.updatedAt.isoformat()
        } if physicalLocation else None,
        'oldPhysicalLocation': {
            'id': oldPhysicalLocation.id,
            'acronym': oldPhysicalLocation.acronym,
            'active': oldPhysicalLocation.active,
            'observation': oldPhysicalLocation.observation,
            'module': oldPhysicalLocation.module,
            'level': oldPhysicalLocation.level,
            'code': oldPhysicalLocation.code,
            'description': oldPhysicalLocation.description,
            'managementUnit': oldPhysicalLocation.managementUnit,
            'createdAt': oldPhysicalLocation.createdAt.isoformat(),
            'updatedAt': oldPhysicalLocation.updatedAt.isoformat()
        } if oldPhysicalLocation else None,
        'imageUrl': item.imageUrl,
        'status': item.status,
        'inventoried': item.inventoried,
        'reference': item.reference,
        'observation': item.observation,
        'itemChanged': item.itemChanged,
        'createdAt': item.createdAt.isoformat(),
        'updatedAt': item.updatedAt.isoformat()
    }

@item_bp.route('', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'assetCode' not in data:
        return jsonify({'error': 'assetCode é obrigatório'}), 400

    item = Item(
        assetCode=data.get('assetCode'),
        description=data.get('description'),
        acquisitionDate=data.get('acquisitionDate'),
        acquisitionMethod=data.get('acquisitionMethod'),
        supplier=data.get('supplier'),
        physicalLocationId=data.get('physicalLocationId'),
        oldPhysicalLocationId=data.get('oldPhysicalLocationId'),
        imageUrl=data.get('imageUrl'),
        status=data.get('status'),
        inventoried=data.get('inventoried', False),
        reference=data.get('reference'),
        observation=data.get('observation'),
        itemChanged=data.get('itemChanged', False)
    )

    db = SessionLocal()
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
        return jsonify(format_item(item, db)), 201
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@item_bp.route('', methods=['GET'])
def listAllItems():
    db = SessionLocal()
    try:
        # Get pagination parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search = request.args.get('search', '')
        
        # Base query
        query = db.query(Item)
        
        # Apply search filter if provided
        if search:
            query = query.filter(
                or_(
                    Item.assetCode.ilike(f'%{search}%'),
                    Item.description.ilike(f'%{search}%'),
                    Item.reference.ilike(f'%{search}%')
                )
            )
            
        # Get total count for pagination
        total = query.count()
        
        # Apply pagination
        items = query.offset((page - 1) * per_page).limit(per_page).all()
        
        result = [format_item(item, db) for item in items]
            
        return jsonify({
            'items': result,
            'total': total,
            'page': page,
            'per_page': per_page,
            'total_pages': (total + per_page - 1) // per_page
        }), 200
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@item_bp.route('/<int:item_id>', methods=['GET'])
def getItemById(item_id):
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if not item:
            return jsonify({'error': 'Item não encontrado'}), 404
        return jsonify(format_item(item, db)), 200
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@item_bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if not item:
            return jsonify({'error': 'Item não encontrado'}), 404

        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)

        db.commit()
        db.refresh(item)
        return jsonify(format_item(item, db)), 200
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@item_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if not item:
            return jsonify({'error': 'Item não encontrado'}), 404

        db.delete(item)
        db.commit()
        return jsonify({'message': 'Item removido com sucesso'}), 200
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()