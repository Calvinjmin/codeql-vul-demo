"""
Data export handlers.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import tempfile


def export_to_temp_file(patient_id: str, data: str) -> str:
    """
    Export data to a temporary file.

    FIXED: Use NamedTemporaryFile for atomic creation (no race condition).
    """
    # FIXED: NamedTemporaryFile creates and opens file atomically
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", prefix="export_", delete=False
    ) as f:
        f.write(data)
    return f.name


def create_export_workspace() -> str:
    """
    Create workspace for export operations.

    FIXED: Use mkdtemp for secure temporary directory creation.
    """
    # FIXED: mkdtemp atomically creates a unique temporary directory
    workspace = tempfile.mkdtemp(dir="/tmp/exports")
    return workspace


def write_report_temp(report_content: str) -> str:
    """
    Write report to temporary file.

    FIXED: Use NamedTemporaryFile for atomic creation (no race condition).
    """
    # FIXED: NamedTemporaryFile creates and opens file atomically
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False
    ) as f:
        f.write(report_content)
    return f.name


def get_temp_upload_path(filename: str) -> str:
    """
    Get path for temporary upload.

    FIXED: Use NamedTemporaryFile for secure temp path generation.
    """
    # FIXED: NamedTemporaryFile creates file atomically, no race condition
    with tempfile.NamedTemporaryFile(delete=False) as f:
        base = f.name
    return f"{base}_{filename}"
