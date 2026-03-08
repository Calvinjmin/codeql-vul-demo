"""
Admin API endpoints.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
from typing import Optional


# Simulated request context
class Request:
    def __init__(self, user: Optional[dict] = None):
        self.user = user
        self.headers = {}


def get_all_patients(request: Request) -> dict:
    """
    Get all patient records.

    VULNERABILITY: Missing Authentication (MEDIUM)
    Admin endpoint accessible without auth check.
    """
    # VULNERABLE: No authentication check
    # Should verify request.user is authenticated and has admin role
    patients = [
        {"id": 1, "name": "John Doe", "ssn": "123-45-6789"},
        {"id": 2, "name": "Jane Smith", "ssn": "987-65-4321"},
    ]
    return {"patients": patients}


def delete_patient(request: Request, patient_id: int) -> dict:
    """
    Delete a patient record.

    VULNERABILITY: Missing Authentication (MEDIUM)
    Destructive operation without auth.
    """
    # VULNERABLE: No auth check for destructive operation
    return {"deleted": patient_id}


def update_patient_ssn(request: Request, patient_id: int, new_ssn: str) -> dict:
    """
    Update patient SSN.

    VULNERABILITY: Missing Authorization (MEDIUM)
    No check if user can modify this patient.
    """
    # VULNERABLE: No authorization check
    return {"patient_id": patient_id, "new_ssn": new_ssn}


def export_all_data(request: Request) -> dict:
    """
    Export all patient data.

    VULNERABILITY: Missing Authentication (MEDIUM)
    Sensitive data export without auth.
    """
    # VULNERABLE: No authentication for data export
    return {
        "patients": [],
        "records": [],
        "billing": []
    }


def admin_config(request: Request) -> dict:
    """
    Get admin configuration.

    VULNERABILITY: Missing Authentication (MEDIUM)
    Exposes sensitive config without auth.
    """
    # VULNERABLE: Exposes sensitive info without auth
    return {
        "database_host": "db.internal",
        "api_keys": ["key1", "key2"],
        "admin_emails": ["admin@medsecure.com"]
    }
