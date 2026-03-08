"""
File handling utilities for patient documents.
"""
import os
import re
import shutil


UPLOAD_DIR = "/var/www/uploads"
ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".png", ".doc", ".docx"}

# Only allow alphanumeric characters, hyphens, and underscores in patient IDs
_PATIENT_ID_RE = re.compile(r"^[a-zA-Z0-9_-]+$")


def _validate_patient_id(patient_id: str) -> str:
    """Validate that patient_id contains only safe characters."""
    if not patient_id or not _PATIENT_ID_RE.match(patient_id):
        raise ValueError(f"Invalid patient_id: {patient_id!r}")
    return patient_id


def _safe_resolve(base: str, *parts: str) -> str:
    """Join path parts and ensure the result is inside *base*."""
    resolved = os.path.normpath(os.path.join(base, *parts))
    if not resolved.startswith(os.path.normpath(base) + os.sep) and resolved != os.path.normpath(base):
        raise ValueError("Path escapes the upload directory")
    return resolved


def get_patient_document(patient_id: str, filename: str) -> bytes:
    """Retrieve a patient's document."""
    _validate_patient_id(patient_id)
    safe_filename = os.path.basename(filename)
    file_path = _safe_resolve(UPLOAD_DIR, patient_id, safe_filename)

    with open(file_path, "rb") as f:
        return f.read()


def save_patient_document(patient_id: str, filename: str, content: bytes) -> str:
    """Save a document for a patient."""
    _validate_patient_id(patient_id)
    safe_filename = os.path.basename(filename)
    patient_dir = _safe_resolve(UPLOAD_DIR, patient_id)
    os.makedirs(patient_dir, exist_ok=True)

    file_path = _safe_resolve(UPLOAD_DIR, patient_id, safe_filename)

    with open(file_path, "wb") as f:
        f.write(content)

    return file_path


def delete_patient_documents(patient_id: str) -> bool:
    """Delete all documents for a patient."""
    _validate_patient_id(patient_id)
    patient_dir = _safe_resolve(UPLOAD_DIR, patient_id)

    if os.path.exists(patient_dir):
        shutil.rmtree(patient_dir)

    return True


def list_patient_documents(patient_id: str) -> list:
    """List all documents for a patient."""
    _validate_patient_id(patient_id)
    patient_dir = _safe_resolve(UPLOAD_DIR, patient_id)

    if os.path.exists(patient_dir):
        return os.listdir(patient_dir)
    return []
