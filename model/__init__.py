"""The application's model objects"""
from hw.model.meta import Session, Base
from hw.model.person import Person
from hw.model.adress import Address
from hw.model.chanel import Chanel
from hw.model.message import Message

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
