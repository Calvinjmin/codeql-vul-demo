"""
Data export handlers.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import os
import tempfile


def export_to_temp_file(patient_id: str, data: str) -> str:
    """
    Export data to a temporary file.

    VULNERABILITY: Insecure Temporary File (LOW)
    tempfile.mktemp() creates predictable path with race condition.
    """
    # VULNERABLE: mktemp() is deprecated and insecure - py/insecure-temporary-file
    # Race condition: attacker can create file between mktemp() and open()
    temp_path = tempfile.mktemp(suffix=".csv", prefix="export_")
    with open(temp_path, "w") as f:
        f.write(data)
    return temp_path


def create_export_workspace() -> str:
    """
    Create workspace for export operations.

    VULNERABILITY: Insecure Temporary File (LOW)
    """
    # VULNERABLE: mktemp() returns path that may be claimed by attacker
    workspace = tempfile.mktemp(dir="/tmp/exports")
    os.makedirs(workspace, exist_ok=True)
    return workspace


def write_report_temp(report_content: str) -> str:
    """
    Write report to temporary file.

    VULNERABILITY: Insecure Temporary File (LOW)
    """
    # VULNERABLE: mktemp() - py/insecure-temporary-file
    report_path = tempfile.mktemp(suffix=".html")
    with open(report_path, "w") as f:
        f.write(report_content)
    return report_path


def get_temp_upload_path(filename: str) -> str:
    """
    Get path for temporary upload.

    VULNERABILITY: Insecure Temporary File (LOW)
    """
    # VULNERABLE: os.tempnam() is also insecure - py/insecure-temporary-file
    base = tempfile.mktemp()
    return f"{base}_{filename}"
