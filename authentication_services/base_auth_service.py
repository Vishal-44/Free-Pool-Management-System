from abc import ABC, abstractmethod

class BaseAuthService(ABC):
    
    @abstractmethod
    def authenticate(self, **kwargs):
        pass

    @abstractmethod
    def create_auth_headers(self, **kwargs):
        pass