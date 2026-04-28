import string
import secrets
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_random_password(length: int = 8) -> tuple:
    """
    Generate a random password with uppercase, lowercase, digits, and special characters.
    
    Args:
        length: Length of the password to generate (default: 12)
    
    Returns:
        A tuple containing the randomly generated password string and its hashed version
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password, hash_password(password)


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    Args:
        password: The plain text password to hash
    
    Returns:
        The hashed password
    """
    return password_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    
    Args:
        plain_password: The plain text password to verify
        hashed_password: The hashed password to compare against
    
    Returns:
        True if the password is correct, False otherwise
    """
    return password_context.verify(plain_password, hashed_password)
