from storage_services.database_service import DatabaseService
from serializers.auth import AuthRequest
from storage_services.db_models import Admin

class AuthRepository(DatabaseService):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AuthRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def is_admin(self, body:AuthRequest) -> Admin:
        with self.get_session() as session:
            query = session.query(Admin.id, Admin.email, Admin.password)   
            if body.username:
                query = query.filter(Admin.username == body.username)
            elif body.email:
                query = query.filter(Admin.email == body.email)
            admin = query.first()
            return admin    