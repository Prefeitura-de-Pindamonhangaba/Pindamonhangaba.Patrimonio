from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
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
        return jsonify({
            'id': item.id,
            'assetCode': item.assetCode,
            'description': item.description,
            'acquisitionDate': item.acquisitionDate.isoformat() if item.acquisitionDate else None,
            'acquisitionMethod': item.acquisitionMethod,
            'supplier': item.supplier,
            'physicalLocationId': item.physicalLocationId,
            'oldPhysicalLocationId': item.oldPhysicalLocationId,
            'imageUrl': item.imageUrl,
            'status': item.status,
            'inventoried': item.inventoried,
            'reference': item.reference,
            'observation': item.observation,
            'itemChanged': item.itemChanged,
            'createdAt': item.createdAt.isoformat(),
            'updatedAt': item.updatedAt.isoformat()
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@item_bp.route('', methods=['GET'])
def listAllItems():
    db = SessionLocal()
    try:
        asset_code = request.args.get('assetCode')
        query = db.query(Item)
        
        if asset_code:
            query = query.filter(Item.assetCode.ilike(f'%{asset_code}%'))
            
        items = query.all()
        result = []
        for item in items:
            physicalLocation = db.query(PhysicalLocation).filter(Item.physicalLocationId == PhysicalLocation.id).first()
            oldPhysicalLocation = db.query(PhysicalLocation).filter(Item.oldPhysicalLocationId == PhysicalLocation.id).first()

            result.append({
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
            })
        return jsonify(result), 201
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
        print(item_id)
        return jsonify({
            'id': item.id,
            'assetCode': item.assetCode,
            'description': item.description,
            'acquisitionDate': item.acquisitionDate.isoformat() if item.acquisitionDate else None,
            'acquisitionMethod': item.acquisitionMethod,
            'supplier': item.supplier,
            'physicalLocationId': item.physicalLocationId,
            'oldPhysicalLocationId': item.oldPhysicalLocationId,
            'imageUrl': item.imageUrl,
            'status': item.status,
            'inventoried': item.inventoried,
            'reference': item.reference,
            'observation': item.observation,
            'itemChanged': item.itemChanged,
            'createdAt': item.createdAt.isoformat(),
            'updatedAt': item.updatedAt.isoformat()
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()