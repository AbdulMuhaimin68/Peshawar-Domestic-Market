from project.app.db import db
from project.app.model.contact import Contact
from sqlalchemy.orm import scoped_session

class ContactRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_contact(args:dict, session:scoped_session):
        try:
            contact = Contact(**args)
            session.add(contact)
            session.commit()
            return contact
        except Exception as e:
            session.rollback()
            raise e
        