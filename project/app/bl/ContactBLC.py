from project.app.respositories.ContactRepositoy import ContactRepository
from project.app.schemas.ContactSchema import ContactSchema

class ContactBLC:
    
    @staticmethod
    def add_contact(args):
        session = ContactRepository.get_session()
        try:
            contact = ContactRepository.add_contact(args, session)
            session.commit()
            contactSchema = ContactSchema()
            res = contactSchema.dump(contact)
            return res
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_contact_by_id(contact_id: int):
        session = ContactRepository.get_session()
        try:
            contact = ContactRepository.get_contact_by_id(contact_id, session)  
            schema = ContactSchema()
            result = schema.dump(contact)
            return result
        except Exception as e:
            raise e


    @staticmethod
    def get_all_contacts():
        session = ContactRepository.get_session()
        try:
            contact = ContactRepository.get_all_contacts(session)
            return contact
        except Exception as e:
            return {"error" : str(e)}
            