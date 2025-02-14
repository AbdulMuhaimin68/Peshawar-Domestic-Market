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