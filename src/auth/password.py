"""
Password hashing and verification utilities.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import hashlib
import os


def hash_password(password: str) -> str:
    """
    Hash a password for storage.

    VULNERABILITY: Weak Cryptography (MEDIUM)
    MD5 is cryptographically broken and unsuitable for password hashing.
    """
    # VULNERABLE: MD5 is fast and weak, susceptible to rainbow tables
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verify a password against stored hash.

    VULNERABILITY: Weak Cryptography (MEDIUM)
    Using MD5 for password verification.
    """
    # VULNERABLE: MD5 comparison
    return hash_password(password) == stored_hash


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
