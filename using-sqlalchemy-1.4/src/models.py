from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from datetime import datetime
Base = declarative_base()

""" 
primary_key=True => PRIMARY KEY(id)
unique=True => UNIQUE kEY(email)
ForeignKey('table_name.field_name') 
"""

# DDL => CREATE TABLE

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True) # clave primaria de la tabla contacts
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(120), unique=True) 
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime(), default=datetime.now())
    #phone_numbers = relationship('PhoneNumbers') # [<PhoneNumbers 1>, <PhoneNumbers2>, <PhoneNumbersN>]

class PhoneNumbers(Base):
    __tablename__ = 'phone_numbers'
    id = Column(Integer, primary_key=True) # clave primaria de la tabla contacts
    phone = Column(String(50), nullable=False)
    comment = Column(Text())
    contacts_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship('Contact', uselist=False, backref="phone_numbers") # [<Contact 1>], con el uselist=False retorna <Contacts 1>



