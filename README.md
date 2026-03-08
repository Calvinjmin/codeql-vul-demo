# MedSecure Patient Portal (Vulnerable Demo)

**WARNING: This repository contains intentional security vulnerabilities for demonstration purposes.**

This is a sample vulnerable application used to demonstrate automated security remediation with Devin.

## Vulnerabilities

### HIGH Severity
- **SQL Injection** - `src/database/queries.py`
- **SQL Injection (ORM)** - `src/database/orm_queries.py`
- **Command Injection** - `src/utils/backup.py`
- **Hardcoded Credentials** - `src/config/settings.py`
- **Path Traversal** - `src/handlers/file_handler.py`
- **Insecure Deserialization** - `src/utils/cache.py`
- **SSRF** - `src/services/webhook.py`

### MEDIUM Severity
- **XSS** - `src/views/profile.py`
- **Weak Cryptography** - `src/auth/password.py`
- **Missing Authentication** - `src/api/admin.py`
- **YAML Unsafe Deserialization** - `src/utils/config_loader.py`
- **LDAP Injection** - `src/auth/ldap_auth.py`
- **URL Redirection** - `src/app.py` - Flask redirect with user input (py/url-redirection, CVSS 6.1 → Medium)

### LOW Severity
- **Debug Mode Enabled** - `src/config/app.py`
- **Open Redirect** - `src/auth/login.py`
- **ReDoS (Inefficient Regex)** - `src/utils/validation.py`
- **Insecure Temporary File** - `src/handlers/export.py`

## Purpose

This repository is used with the Security Backlog Autopilot to demonstrate:
1. Automated triage of CodeQL findings
2. Launching Devin sessions to fix vulnerabilities
3. Automated PR generation for security fixes

**Do not deploy this application.**
