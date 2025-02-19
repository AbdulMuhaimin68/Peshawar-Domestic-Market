from sqlalchemy.orm import Session
from project.app.respositories.LoginRepository import LoginRepository 

class LoginBLC:
    
    @staticmethod
    def login(args):
        session: Session = LoginRepository.get_session()
        
        try:
            result = LoginRepository.login(args, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            print(f"Error in LoginBLC.login: {e}")  
            raise e
        finally:
            session.close()  
