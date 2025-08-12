from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    max_kw = Column(Float)
    is_active = Column(Boolean, default=True)
