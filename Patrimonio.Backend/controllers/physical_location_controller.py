from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class PhysicalLocation(Base):
    __tablename__ = 'physicalLocations'

    id = Column(Integer, primary_key=True, index=True)
    referencial = Column(String)
    refProprio = Column(String)
    refSubordinacao = Column(String)
    refSubordinacaoAdmMigra = Column(String)
    refResponsavel = Column(String)
    refTipoMigra = Column(String)
    sigla = Column(String)
    ativo = Column(Boolean, default=True)
    obs = Column(String)
    modulo = Column(String)
    nivel = Column(Integer)
    codigo = Column(String)
    descricao = Column(String)
    unidadeGestora = Column(String)
    refTipo = Column(String)
    refSubordinacaoAdm = Column(String)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind=engine)

physical_location_bp = Blueprint('physical_location', __name__, url_prefix='/physical_location')

@physical_location_bp.route('', methods=['POST'])
def create_physical_location():
    data = request.get_json()
    if not data or 'referencial' not in data:
        return jsonify({'error': 'referencial é obrigatório'}), 400

    physical_location = PhysicalLocation(
        referencial=data.get('referencial'),
        refProprio=data.get('refProprio'),
        refSubordinacao=data.get('refSubordinacao'),
        refSubordinacaoAdmMigra=data.get('refSubordinacaoAdmMigra'),
        refResponsavel=data.get('refResponsavel'),
        refTipoMigra=data.get('refTipoMigra'),
        sigla=data.get('sigla'),
        ativo=data.get('ativo', True),
        obs=data.get('obs'),
        modulo=data.get('modulo'),
        nivel=data.get('nivel'),
        codigo=data.get('codigo'),
        descricao=data.get('descricao'),
        unidadeGestora=data.get('unidadeGestora'),
        refTipo=data.get('refTipo'),
        refSubordinacaoAdm=data.get('refSubordinacaoAdm')
    )

    db = SessionLocal()
    try:
        db.add(physical_location)
        db.commit()
        db.refresh(physical_location)
        return jsonify({
            'id': physical_location.id,
            'referencial': physical_location.referencial,
            'refProprio': physical_location.refProprio,
            'refSubordinacao': physical_location.refSubordinacao,
            'refSubordinacaoAdmMigra': physical_location.refSubordinacaoAdmMigra,
            'refResponsavel': physical_location.refResponsavel,
            'refTipoMigra': physical_location.refTipoMigra,
            'sigla': physical_location.sigla,
            'ativo': physical_location.ativo,
            'obs': physical_location.obs,
            'modulo': physical_location.modulo,
            'nivel': physical_location.nivel,
            'codigo': physical_location.codigo,
            'descricao': physical_location.descricao,
            'unidadeGestora': physical_location.unidadeGestora,
            'refTipo': physical_location.refTipo,
            'refSubordinacaoAdm': physical_location.refSubordinacaoAdm,
            'createdAt': physical_location.createdAt.isoformat(),
            'updatedAt': physical_location.updatedAt.isoformat()
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()