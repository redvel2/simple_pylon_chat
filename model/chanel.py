"""Person model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation, backref
from hw.model.meta import Base

class Chanel(Base):
    __tablename__ = "chanel"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    owner = Column(String(100))
    created = Column(String(100))
    def __init__(self, name='', owner='', created=''):
        self.name = name
        self.owner = owner
        self.created=created

    def __repr__(self):
        return "<Chanel('%s')" % self.name