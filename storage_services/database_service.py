from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from constants.database_constants import (
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
)


class DatabaseService:
    def __init__(self):
        """Initialize database service with connection pooling and validation."""
        if not all([DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD]):
            raise ValueError("Database configuration is incomplete. Please check environment variables.")
        
        self.database_url = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        
        # Create engine with optimized connection pooling
        self._engine = create_engine(
            self.database_url,
            poolclass=QueuePool,
            pool_size=10,                    # Number of connections to maintain
            max_overflow=20,                 # Additional connections when pool is exhausted
            pool_recycle=3600,               # Recycle connections after 1 hour
            pool_timeout=30,                 # Wait max 30 seconds for available connection
            pool_pre_ping=True,              # Test connection before using
            echo=False                       # Set to True for SQL debugging
        )
        
        self._SessionLocal = sessionmaker(
            autocommit=False, 
            autoflush=False, 
            bind=self._engine,
            expire_on_commit=False
        )


    @contextmanager
    def get_session(self):
        """
        Provide a transactional scope around a series of operations.
        Usage: with db_service.get_session() as session:
        """
        session = self._SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

