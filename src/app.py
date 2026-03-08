"""
Flask application entry point.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import json  # VULNERABLE: Unused import - py/unused-import (quality, Low severity)
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
    # VULNERABLE: User input passed directly to redirect - no validation
    return redirect(next_url)


@app.route("/logout")
def logout():
    """
    Logout handler with open redirect.

    VULNERABILITY: URL Redirection (MEDIUM)
    """
    redirect_url = request.args.get("redirect", "/")
    return redirect(redirect_url)


@app.route("/sso/callback")
def sso_callback():
    """
    SSO callback with open redirect.

    VULNERABILITY: URL Redirection (MEDIUM)
    """
    target = request.args.get("target", "/")
    return redirect(target, code=302)
