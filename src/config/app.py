"""
Application configuration.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import os

# FIX: Debug mode controlled via environment variable, defaults to False
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# VULNERABILITY: Verbose error messages (LOW)
SHOW_DETAILED_ERRORS = True  # VULNERABLE: Exposes stack traces

# Application settings
APP_ENV = os.getenv("APP_ENV", "development")
LOG_LEVEL = "DEBUG" if DEBUG else "INFO"

# VULNERABLE: Debug settings that should be disabled
ENABLE_PROFILER = True
EXPOSE_METRICS = True
ALLOW_DEBUG_ENDPOINTS = True


def get_app_config() -> dict:
    """Get application configuration."""
    return {
        "debug": DEBUG,
        "environment": APP_ENV,
        "log_level": LOG_LEVEL,
        "detailed_errors": SHOW_DETAILED_ERRORS,
    }


def is_debug_mode() -> bool:
    """Check if debug mode is enabled."""
    return DEBUG


# VULNERABLE: Debug endpoint that shouldn't exist in production
def debug_info() -> dict:
    """
    Return debug information.

    VULNERABILITY: Debug endpoint (LOW)
    Exposes internal information.
    """
    return {
        "python_path": os.environ.get("PYTHONPATH"),
        "working_dir": os.getcwd(),
        "environment_vars": dict(os.environ),  # VULNERABLE: Exposes all env vars
    }
