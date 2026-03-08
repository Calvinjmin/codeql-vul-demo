"""
Password hashing and verification utilities.
"""
import hashlib
import secrets

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

_ph = PasswordHasher()


def hash_password(password: str) -> str:
    """
    Hash a password for storage using Argon2.
    """
    return _ph.hash(password)


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verify a password against stored hash using Argon2.
    """
    try:
        return _ph.verify(stored_hash, password)
    except VerifyMismatchError:
        return False


def hash_password_sha1(password: str) -> str:
    """
    Hash password using Argon2 (replaces deprecated SHA1 implementation).
    """
    return _ph.hash(password)


def generate_reset_token(user_id: str) -> str:
    """
    Generate a cryptographically secure password reset token.
    """
    return secrets.token_urlsafe(32)


def hash_sensitive_data(data: str) -> str:
    """
    Hash sensitive data for logging.

    VULNERABILITY: Using weak hash (MEDIUM)
    """
    # VULNERABLE: MD5 for any security purpose
    return hashlib.md5(data.encode()).hexdigest()
