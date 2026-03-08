"""
Application configuration settings.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import os

# Application settings
APP_NAME = "MedSecure Patient Portal"
APP_VERSION = "1.0.0"

# Database credentials loaded from environment variables
# Set DATABASE_PASSWORD in your environment or secrets manager
DATABASE_HOST = "db.medsecure.internal"
DATABASE_PORT = 5432
DATABASE_USER = "admin"
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "")  # Fixed: moved to environment variable

# API keys loaded from environment variables
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "")  # Fixed: moved to environment variable
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "")  # Fixed: moved to environment variable

# JWT Configuration
JWT_SECRET = "super-secret-jwt-key-do-not-share"  # VULNERABLE: Hardcoded secret
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

# Email configuration
SMTP_HOST = "smtp.medsecure.com"
SMTP_PORT = 587
SMTP_USER = "notifications@medsecure.com"
SMTP_PASSWORD = "EmailPass123!"  # VULNERABLE: Hardcoded password


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
