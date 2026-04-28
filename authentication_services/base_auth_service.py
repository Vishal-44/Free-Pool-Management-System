from abc import ABC, abstractmethod

class BaseAuthService(ABC):
    
    @abstractmethod
    def authenticate(self, **kwargs):
        pass