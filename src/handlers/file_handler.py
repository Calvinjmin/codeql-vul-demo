"""
File handling utilities for patient documents.
"""
import os
import re
import shutil


UPLOAD_DIR = "/var/www/uploads"
ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".png", ".doc", ".docx"}


def _sanitize_path_component(value: str) -> str:
    """Strip directory traversal sequences by extracting the base name."""
    return os.path.basename(value)


def _validate_patient_id(patient_id: str) -> str:
    """Validate and return a safe patient_id (alphanumeric, hyphens, underscores)."""
    if not re.match(r"^[a-zA-Z0-9_-]+$", patient_id):
        raise ValueError("Invalid patient_id format")
    return patient_id


def _safe_patient_dir(patient_id: str) -> str:
    """Return a validated patient directory path that resides under UPLOAD_DIR."""
    safe_id = _validate_patient_id(patient_id)
    patient_dir = os.path.realpath(os.path.join(UPLOAD_DIR, safe_id))
    if not patient_dir.startswith(os.path.realpath(UPLOAD_DIR) + os.sep):
        raise ValueError("Invalid patient directory")
    return patient_dir


def get_patient_document(patient_id: str, filename: str) -> bytes:
    """
    Retrieve a patient's document.
    """
    patient_dir = _safe_patient_dir(patient_id)
    safe_filename = _sanitize_path_component(filename)
    file_path = os.path.join(patient_dir, safe_filename)

    with open(file_path, "rb") as f:
        return f.read()


def save_patient_document(patient_id: str, filename: str, content: bytes) -> str:
    """
    Save a document for a patient.
    """
    patient_dir = _safe_patient_dir(patient_id)
    os.makedirs(patient_dir, exist_ok=True)

    safe_filename = _sanitize_path_component(filename)
    file_path = os.path.join(patient_dir, safe_filename)

    with open(file_path, "wb") as f:
        f.write(content)

    return file_path


def delete_patient_documents(patient_id: str) -> bool:
    """
    Delete all documents for a patient.
    """
    patient_dir = _safe_patient_dir(patient_id)

    if os.path.exists(patient_dir):
        shutil.rmtree(patient_dir)

    return True


def list_patient_documents(patient_id: str) -> list:
    """
    List all documents for a patient.
    """
    patient_dir = _safe_patient_dir(patient_id)

    if os.path.exists(patient_dir):
        return os.listdir(patient_dir)
    return []
