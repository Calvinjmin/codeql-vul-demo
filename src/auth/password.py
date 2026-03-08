"""
Password hashing and verification utilities.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import secrets

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password: str) -> str:
    """
    Hash a password for storage.

    Uses Argon2 (via argon2-cffi), a strong password hashing algorithm
    resistant to brute-force and rainbow table attacks.
    """
    return ph.hash(password)


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verify a password against stored hash.

    Uses Argon2 verification which is timing-safe.
    """
    try:
        return ph.verify(stored_hash, password)
    except VerifyMismatchError:
        return False


def hash_password_sha1(password: str) -> str:
    """
    Hash password with a strong algorithm.

    Uses Argon2 instead of the previously used SHA1,
    which is deprecated for security purposes.
    """
    return ph.hash(password)


def generate_reset_token(user_id: str) -> str:
    """
    Generate password reset token.

    Uses cryptographically secure random token generation
    instead of a predictable MD5-based approach.
    """
    return secrets.token_urlsafe(32)


def hash_sensitive_data(data: str) -> str:
    """
    Hash sensitive data for logging.

    Uses Argon2 for hashing sensitive data instead of MD5.
    """
    return ph.hash(data)
