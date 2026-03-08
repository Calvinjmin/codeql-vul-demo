"""
Login and authentication handlers.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
from urllib.parse import urlparse


def handle_login(username: str, password: str, redirect_url: str = None) -> dict:
    """
    Handle user login.

    VULNERABILITY: Open Redirect (LOW)
    Redirect URL not validated, allows phishing attacks.
    """
    # Simulate authentication
    authenticated = len(username) > 0 and len(password) > 0

    if authenticated:
        # VULNERABLE: No validation of redirect URL
        # Attacker can use: ?redirect=https://evil.com/steal-creds
        return {
            "success": True,
            "redirect": redirect_url or "/dashboard"  # VULNERABLE
        }

    return {"success": False, "error": "Invalid credentials"}


def handle_logout(redirect_url: str = None) -> dict:
    """
    Handle user logout.

    VULNERABILITY: Open Redirect (LOW)
    Post-logout redirect not validated.
    """
    # VULNERABLE: Unvalidated redirect
    return {
        "success": True,
        "redirect": redirect_url or "/"
    }


def validate_redirect_url(url: str) -> bool:
    """
    Validate redirect URL (insufficient validation).

    VULNERABILITY: Open Redirect bypass (LOW)
    Validation can be bypassed.
    """
    if not url:
        return True

    # VULNERABLE: Insufficient validation
    # Can be bypassed with: //evil.com or https://evil.com
    if url.startswith("/"):
        return True

    return False


def handle_sso_callback(token: str, redirect_url: str) -> dict:
    """
    Handle SSO callback.

    VULNERABILITY: Open Redirect (LOW)
    SSO redirect not validated.
    """
    # Simulate token validation
    valid_token = len(token) > 10

    if valid_token:
        # VULNERABLE: Unvalidated redirect after SSO
        return {
            "success": True,
            "redirect": redirect_url  # VULNERABLE
        }

    return {"success": False, "error": "Invalid SSO token"}


def build_login_redirect(next_page: str) -> str:
    """
    Build redirect URL for login page.

    VULNERABILITY: Open Redirect (LOW)
    """
    # VULNERABLE: User-controlled redirect embedded in URL
    return f"/login?next={next_page}"
