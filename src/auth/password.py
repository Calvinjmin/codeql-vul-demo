"""
Password hashing and verification utilities.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import hashlib
import os
import secrets

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def hash_password(password: str) -> str:
    """
    Hash a password for storage.

    Uses Argon2 (winner of the Password Hashing Competition) which is
    resistant to brute-force and rainbow table attacks.
    """
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verify a password against stored hash.

    Uses Argon2 verification which is timing-safe.
    """
    ph = PasswordHasher()
    try:
        return ph.verify(stored_hash, password)
    except VerifyMismatchError:
        return False


def hash_password_sha1(password: str) -> str:
    """
    Hash password with Argon2.

    Uses Argon2 which is a strong, modern password hashing algorithm.
    Note: Function name retained for backward compatibility.
    """
    ph = PasswordHasher()
    return ph.hash(password)


def generate_reset_token(user_id: str) -> str:
    """
    Generate password reset token.

    Uses cryptographically secure random token generation.
    """
    return secrets.token_urlsafe(32)


def hash_sensitive_data(data: str) -> str:
    """
    Hash sensitive data for logging.

    VULNERABILITY: Using weak hash (MEDIUM)
    """
    # VULNERABLE: MD5 for any security purpose
    return hashlib.md5(data.encode()).hexdigest()
