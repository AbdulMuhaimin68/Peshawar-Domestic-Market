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
        

    @staticmethod
    def get_contact_by_id(contact_id: int, session):
        return session.query(Contact).filter(Contact.contact_id == contact_id).first()

        
    @staticmethod
    def get_all_contacts(session:scoped_session):
        try:
            return session.query(Contact).all()
        except Exception as e:
            raise e