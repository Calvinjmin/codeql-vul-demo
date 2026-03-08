"""
LDAP authentication utilities.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
# Simulated LDAP filter construction (actual ldap3/python-ldap would be used in production)


def build_user_search_filter(username: str) -> str:
    """
    Build LDAP search filter for user lookup.

    VULNERABILITY: LDAP Injection (MEDIUM)
    User input concatenated into LDAP filter without escaping.
    """
    # VULNERABLE: username could contain )(*)(| to bypass filter
    # e.g. "admin)(|(password=*" to match any password
    return f"(uid={username})"  # py/ldap-injection (if query exists) or similar


def build_group_membership_filter(user_id: str, group_name: str) -> str:
    """
    Build LDAP filter for group membership check.

    VULNERABILITY: LDAP Injection (MEDIUM)
    Multiple user inputs in filter.
    """
    # VULNERABLE: Both inputs can inject LDAP filter syntax
    return f"(&(member={user_id})(cn={group_name}))"


def search_users_by_department(department: str) -> str:
    """
    Build LDAP filter for department search.

    VULNERABILITY: LDAP Injection (MEDIUM)
    """
    # VULNERABLE: department from user input
    return f"(department={department})"


def build_combined_filter(username: str, email: str) -> str:
    """
    Build combined LDAP filter.

    VULNERABILITY: LDAP Injection (MEDIUM)
    """
    # VULNERABLE: OR condition with user input
    return f"(|(uid={username})(mail={email}))"
