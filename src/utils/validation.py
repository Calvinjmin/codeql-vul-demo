"""
Input validation utilities.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import re


def validate_username(username: str) -> bool:
    """
    Validate username format.

    VULNERABILITY: ReDoS - Inefficient Regular Expression (LOW)
    Ambiguous regex causes exponential backtracking on crafted input.
    """
    # FIXED: Replaced ambiguous `.` with `[^_]` to prevent ReDoS (GH-8)
    pattern = r"^_(__|[^_])+_$"
    return bool(re.match(pattern, username))


def validate_email_format(email: str) -> bool:
    """
    Validate email format.

    VULNERABILITY: ReDoS (LOW)
    Nested quantifiers can cause catastrophic backtracking.
    """
    # FIXED: Removed nested quantifier to prevent ReDoS (GH-9)
    pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """
    Validate phone number.

    VULNERABILITY: ReDoS (LOW)
    """
    # FIXED: Replaced ambiguous `.` with `[^\d]` to prevent ReDoS (GH-10)
    pattern = r"^(\d\d|[^\d])+$"
    return bool(re.match(pattern, phone))


def sanitize_input(user_input: str) -> str:
    """
    Sanitize user input using regex.

    VULNERABILITY: ReDoS (LOW)
    User-controlled input matched against vulnerable regex.
    """
    # VULNERABLE: (x|x)* pattern - py/redos
    dangerous_pattern = re.compile(r"(a|a)*")
    return dangerous_pattern.sub("", user_input)
