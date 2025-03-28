from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from datetime import datetime
from models.physical_location_model import PhysicalLocation
from database import db

load_dotenv()

Base = declarative_base()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

physical_location_bp = Blueprint('physical_location', __name__, url_prefix='/physical_location')

@physical_location_bp.route('', methods=['POST'])
def create_physical_location():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'error': 'code é obrigatório'}), 400

    physical_location = PhysicalLocation(
        acronym=data.get('acronym'),
        active=data.get('active', True),
        observation=data.get('observation'),
        module=data.get('module'),
        level=data.get('level'),
        code=data.get('code'),
        description=data.get('description'),
        managementUnit=data.get('managementUnit')
    )

    db = db.get_db()
    try:
        db.add(physical_location)
        db.commit()
        db.refresh(physical_location)
        return jsonify({
            'id': physical_location.id,
            'acronym': physical_location.acronym,
            'active': physical_location.active,
            'observation': physical_location.observation,
            'module': physical_location.module,
            'level': physical_location.level,
            'code': physical_location.code,
            'description': physical_location.description,
            'managementUnit': physical_location.managementUnit,
            'createdAt': physical_location.createdAt.isoformat(),
            'updatedAt': physical_location.updatedAt.isoformat()
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@physical_location_bp.route('', methods=['GET'])
def get_physical_locations():
    db = db.get_db()
    try:
        physical_locations = db.query(PhysicalLocation).all()
        return jsonify([{
            'id': location.id,
            'acronym': location.acronym,
            'active': location.active,
            'observation': location.observation,
            'module': location.module,
            'level': location.level,
            'code': location.code,
            'description': location.description,
            'managementUnit': location.managementUnit,
            'createdAt': location.createdAt.isoformat(),
            'updatedAt': location.updatedAt.isoformat()
        } for location in physical_locations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@physical_location_bp.route('/<int:location_id>', methods=['GET'])
def get_physical_location(location_id):
    db = db.get_db()
    try:
        location = db.query(PhysicalLocation).filter(PhysicalLocation.id == location_id).first()
        if not location:
            return jsonify({'error': 'Local físico não encontrado'}), 404
        return jsonify({
            'id': location.id,
            'acronym': location.acronym,
            'active': location.active,
            'observation': location.observation,
            'module': location.module,
            'level': location.level,
            'code': location.code,
            'description': location.description,
            'managementUnit': location.managementUnit,
            'createdAt': location.createdAt.isoformat(),
            'updatedAt': location.updatedAt.isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@physical_location_bp.route('/<int:location_id>', methods=['PUT'])
def update_physical_location(location_id):
    data = request.get_json()
    db = db.get_db()
    try:
        location = db.query(PhysicalLocation).filter(PhysicalLocation.id == location_id).first()
        if not location:
            return jsonify({'error': 'Local físico não encontrado'}), 404

        location.acronym = data.get('acronym', location.acronym)
        location.active = data.get('active', location.active)
        location.observation = data.get('observation', location.observation)
        location.module = data.get('module', location.module)
        location.level = data.get('level', location.level)
        location.code = data.get('code', location.code)
        location.description = data.get('description', location.description)
        location.managementUnit = data.get('managementUnit', location.managementUnit)
        location.updatedAt = datetime.utcnow()

        db.commit()
        db.refresh(location)
        return jsonify({
            'id': location.id,
            'acronym': location.acronym,
            'active': location.active,
            'observation': location.observation,
            'module': location.module,
            'level': location.level,
            'code': location.code,
            'description': location.description,
            'managementUnit': location.managementUnit,
            'createdAt': location.createdAt.isoformat(),
            'updatedAt': location.updatedAt.isoformat()
        }), 200
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@physical_location_bp.route('/<int:location_id>', methods=['DELETE'])
def delete_physical_location(location_id):
    db = db.get_db()
    try:
        location = db.query(PhysicalLocation).filter(PhysicalLocation.id == location_id).first()
        if not location:
            return jsonify({'error': 'Local físico não encontrado'}), 404

        db.delete(location)
        db.commit()
        return jsonify({'message': 'Local físico removido com sucesso'}), 200
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()