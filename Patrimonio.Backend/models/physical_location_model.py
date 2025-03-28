from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PhysicalLocation(Base):
    __tablename__ = 'physicalLocations'

    id = Column(Integer, primary_key=True, index=True)
    acronym = Column(String)
    active = Column(Boolean, default=True)
    observation = Column(String)
    module = Column(String)
    level = Column(Integer)
    code = Column(String)
    description = Column(String)
    managementUnit = Column(String)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)