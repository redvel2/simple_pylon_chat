"""Person model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation, backref
from hw.model.meta import Base
from sqlalchemy import Column, ForeignKey

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(50))
    last_activity = Column(Integer)
    chanel_id=Column(Integer, ForeignKey('chanel.id'))
    chanel=relation('Chanel', backref=backref('persons', order_by=id))
    def __init__(self, name='', email='', password=''):
        self.name = name
        self.email = email
        self.password=password

    def __repr__(self):
        return "<Person('%s')" % self.name