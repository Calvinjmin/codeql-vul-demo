"""
Webhook service for external integrations.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import requests
import socket
import urllib.parse


def send_webhook_notification(webhook_url: str, payload: dict) -> bool:
    """
    Send notification to external webhook.

    VULNERABILITY: Server-Side Request Forgery (HIGH)
    User-provided URL is fetched without validation.
    """
    # VULNERABLE: No URL validation, can access internal services
    try:
        response = requests.post(
            webhook_url,  # VULNERABLE: User-controlled URL
            json=payload,
            timeout=10
        )
        return response.status_code == 200
    except Exception:
        return False


def fetch_external_resource(url: str) -> str:
    """
    Fetch content from external URL.

    VULNERABILITY: Server-Side Request Forgery (HIGH)
    Can be used to scan internal network or access cloud metadata.
    """
    # VULNERABLE: No validation allows requests to:
    # - http://169.254.169.254/latest/meta-data/ (AWS metadata)
    # - http://localhost:8080/admin (internal services)
    # - file:///etc/passwd (local files)

    response = requests.get(url, timeout=30)  # VULNERABLE: SSRF
    return response.text


def validate_callback_url(url: str) -> bool:
    """
    Validate a callback URL (insufficient validation).

    VULNERABILITY: SSRF bypass (HIGH)
    Validation is easily bypassed.
    """
    parsed = urllib.parse.urlparse(url)

    # VULNERABLE: Insufficient validation
    # Can be bypassed with: http://localhost.attacker.com
    # Or: http://127.0.0.1.nip.io
    if parsed.hostname == "localhost" or parsed.hostname == "127.0.0.1":
        return False

    return True


def test_endpoint_connectivity(url: str) -> dict:
    """
    Test if an endpoint is reachable.

    VULNERABILITY: SSRF for port scanning (HIGH)
    Can be used to scan internal network.
    """
    try:
        # VULNERABLE: Allows internal port scanning
        response = requests.head(url, timeout=5)
        return {
            "reachable": True,
            "status_code": response.status_code
        }
    except requests.exceptions.ConnectionError:
        return {"reachable": False, "error": "Connection refused"}
    except Exception as e:
        return {"reachable": False, "error": str(e)}
