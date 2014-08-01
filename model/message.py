"""Person model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation, backref
from hw.model.meta import Base
from sqlalchemy import Column, ForeignKey

class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    body = Column(String(100))
    date = Column(String(100))
    timestamp=Column(Integer)
    person_id=Column(Integer, ForeignKey('person.id'))
    person_name=Column(String(50))
    person=relation('Person', backref=backref('persons', order_by=id))
    type = Column(String(10))
    to=Column(Integer)
    chanel_id=Column(Integer, ForeignKey('chanel.id'))
    chanel=relation('Chanel', backref=backref('messages', order_by=id))


    def __repr__(self):
        return "<Message('%s')" % self.body