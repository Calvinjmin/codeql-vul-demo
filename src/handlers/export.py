"""
Data export handlers.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import os
import tempfile
from tempfile import NamedTemporaryFile


def export_to_temp_file(patient_id: str, data: str) -> str:
    """
    Export data to a temporary file.

    VULNERABILITY: Insecure Temporary File (LOW)
    tempfile.mktemp() creates predictable path with race condition.
    """
    # FIXED: Use NamedTemporaryFile to atomically create and open the file
    with NamedTemporaryFile(mode="w", suffix=".csv", prefix="export_", delete=False) as f:
        f.write(data)
    return f.name


def create_export_workspace() -> str:
    """
    Create workspace for export operations.

    VULNERABILITY: Insecure Temporary File (LOW)
    """
    # FIXED: Use mkdtemp() to atomically create a secure temporary directory
    os.makedirs("/tmp/exports", exist_ok=True)
    workspace = tempfile.mkdtemp(dir="/tmp/exports")
    return workspace


def write_report_temp(report_content: str) -> str:
    """
    Write report to temporary file.

    VULNERABILITY: Insecure Temporary File (LOW)
    """
    # FIXED: Use NamedTemporaryFile to atomically create and open the file
    with NamedTemporaryFile(mode="w", suffix=".html", delete=False) as f:
        f.write(report_content)
    return f.name


def get_temp_upload_path(filename: str) -> str:
    """
    Get path for temporary upload.

    VULNERABILITY: Insecure Temporary File (LOW)
    """
    # FIXED: Use NamedTemporaryFile to securely generate a unique temp path
    with NamedTemporaryFile(delete=False) as f:
        base = f.name
    return f"{base}_{filename}"
