# MedSecure Patient Portal (Vulnerable Demo)

**WARNING: This repository contains intentional security vulnerabilities for demonstration purposes.**

This is a sample vulnerable application used to demonstrate automated security remediation with Devin.

## Vulnerabilities

### HIGH Severity
- **SQL Injection** - `src/database/queries.py`
- **Hardcoded Credentials** - `src/config/settings.py`
- **Path Traversal** - `src/handlers/file_handler.py`
- **Insecure Deserialization** - `src/utils/cache.py`
- **SSRF** - `src/services/webhook.py`

### MEDIUM Severity
- **XSS** - `src/views/profile.py`
- **Weak Cryptography** - `src/auth/password.py`
- **Missing Authentication** - `src/api/admin.py`

### LOW Severity
- **Debug Mode Enabled** - `src/config/app.py`
- **Open Redirect** - `src/auth/login.py`

## Purpose

This repository is used with the Security Backlog Autopilot to demonstrate:
1. Automated triage of CodeQL findings
2. Launching Devin sessions to fix vulnerabilities
3. Automated PR generation for security fixes

**Do not deploy this application.**
