from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

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