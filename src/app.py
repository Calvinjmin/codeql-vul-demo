"""
Flask application entry point.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import json  # VULNERABLE: Unused import - py/unused-import (quality, Low severity)
from urllib.parse import urlparse

from flask import Flask, redirect, request

app = Flask(__name__)


@app.route("/login")
def login():
    """
    Login handler with open redirect.

    VULNERABILITY: URL Redirection (MEDIUM - py/url-redirection, severity 6.1)
    User-controlled redirect without validation enables phishing attacks.
    """
    next_url = request.args.get("next", "/dashboard")
    # Validate redirect target to prevent open redirect
    next_url = next_url.replace('\\', '')
    if not urlparse(next_url).netloc and not urlparse(next_url).scheme:
        return redirect(next_url)
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    """
    Logout handler with open redirect.

    VULNERABILITY: URL Redirection (MEDIUM)
    """
    redirect_url = request.args.get("redirect", "/")
    # Validate redirect target to prevent open redirect
    redirect_url = redirect_url.replace('\\', '')
    if not urlparse(redirect_url).netloc and not urlparse(redirect_url).scheme:
        return redirect(redirect_url)
    return redirect("/")


@app.route("/sso/callback")
def sso_callback():
    """
    SSO callback with open redirect.

    VULNERABILITY: URL Redirection (MEDIUM)
    """
    target = request.args.get("target", "/")
    # Validate redirect target to prevent open redirect
    target = target.replace('\\', '')
    if not urlparse(target).netloc and not urlparse(target).scheme:
        return redirect(target, code=302)
    return redirect("/", code=302)
