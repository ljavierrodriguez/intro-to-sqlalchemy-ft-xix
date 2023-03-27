from models import Contact, PhoneNumbers
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
session = Session(engine)

""" 
INSERT INTO contacts (field1, field2, field3, field4) VALUES ('value1', 'value2', 10, FALSE);
"""

contact = Contact()
contact.name = 'John'
contact.lastname = 'Doe'
contact.email = 'lrodriguez@4geeks.co'
contact.is_active = False

session.add(contact)
session.commit()
# session.rollback()


"""
SELECT * FROM table_name WHERE condicion
"""

contacts = Contact.query.all() # SELECT * FROM contacts; # [<Contact 1>, <Contact 2>, <Contact 3>]
contact = Contact.query.get(1) # SELECT * FROM contacts WHERE id = 1; # <Contact 1>
contacts = Contact.query.filter_by(is_active=True) # [<PhoneNumbers 1>, <Contact 1>, <Contact 2>]
# contacts = Contact.query.filter_by(email="lrodriguez@4geeks.co") # [<Contact 1>]
contact = Contact.query.filter_by(email="lrodriguez@4geeks.co").firts() # [<Contact 1>]
contact = Contact.query.filter_by(email="lrodriguez@4geeks.co", is_active=True).first() # <Contact 1>

print(contact.phone_numbers) # [<PhoneNumbers 1>]


phoneNumber = PhoneNumbers.query.get(1)
print(phoneNumber) # <PhoneNumbers 1>
print(phoneNumber.contact.name) # John
print(phoneNumber.contact.email) # lrodriguez@4geeks.co


""" 
UPDATE table_name SET field1=value1 WHERE condicion;
"""
contact = Contact.query.get(1) # SELECT * FROM contacts WHERE id = 1; # <Contact 1>
contact.email = 'john.doe@gmail.com'
contact.is_active = True
session.commit()


""" 
DELETE FROM table_name WHERE condicion;
"""
contact = Contact.query.get(1)
session.delete(contact)
session.commit()