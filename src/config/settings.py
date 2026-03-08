"""
Application configuration settings.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import os

# Application settings
APP_NAME = "MedSecure Patient Portal"
APP_VERSION = "1.0.0"

# VULNERABILITY: Hardcoded credentials (HIGH)
# These should be in environment variables or a secrets manager
DATABASE_HOST = "db.medsecure.internal"
DATABASE_PORT = 5432
DATABASE_USER = "admin"
DATABASE_PASSWORD = "MedSecure2024!SuperSecret"  # VULNERABLE: Hardcoded password

# VULNERABILITY: Hardcoded API keys (HIGH)
STRIPE_API_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"  # VULNERABLE: Hardcoded secret
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # VULNERABLE: Hardcoded secret

# JWT Configuration
JWT_SECRET = "super-secret-jwt-key-do-not-share"  # VULNERABLE: Hardcoded secret
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

# Email configuration
SMTP_HOST = "smtp.medsecure.com"
SMTP_PORT = 587
SMTP_USER = "notifications@medsecure.com"
SMTP_PASSWORD = "EmailPass123!"  # VULNERABLE: Hardcoded password

# VULNERABLE: Additional hardcoded secrets
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/FAKE/FAKE/placeholder-not-a-real-secret"
ENCRYPTION_KEY = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"  # VULNERABLE: Hardcoded encryption key


def get_database_url():
    """Build database connection URL."""
    # Using hardcoded credentials instead of environment variables
    return f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/patients"


def get_config():
    """Return application configuration."""
    return {
        "app_name": APP_NAME,
        "database_url": get_database_url(),
        "jwt_secret": JWT_SECRET,
    }
