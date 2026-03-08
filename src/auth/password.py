"""
Password hashing and verification utilities.
"""
import hashlib
import os

import bcrypt


def hash_password(password: str) -> str:
    """
    Hash a password for storage using bcrypt.

    Returns a bcrypt hash string.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verify a password against a stored bcrypt hash.
    """
    return bcrypt.checkpw(password.encode(), stored_hash.encode())


def hash_password_sha1(password: str) -> str:
    """
    Hash password with SHA1.

    VULNERABILITY: Weak Cryptography (MEDIUM)
    SHA1 is deprecated for security purposes.
    """
    # VULNERABLE: SHA1 is also weak for passwords
    return hashlib.sha1(password.encode()).hexdigest()


def generate_reset_token(user_id: str) -> str:
    """
    Generate password reset token.

    VULNERABILITY: Weak token generation (MEDIUM)
    Predictable token based on user_id.
    """
    # VULNERABLE: Predictable token, should use secrets.token_urlsafe()
    return hashlib.md5(f"{user_id}-reset".encode()).hexdigest()


def hash_sensitive_data(data: str) -> str:
    """
    Hash sensitive data for logging.

    VULNERABILITY: Using weak hash (MEDIUM)
    """
    # VULNERABLE: MD5 for any security purpose
    return hashlib.md5(data.encode()).hexdigest()
