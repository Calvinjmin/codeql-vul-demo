"""
File handling utilities for patient documents.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import os
import shutil


UPLOAD_DIR = "/var/www/uploads"
ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".png", ".doc", ".docx"}


def get_patient_document(patient_id: str, filename: str) -> bytes:
    """
    Retrieve a patient's document.

    VULNERABILITY: Path Traversal (HIGH)
    User input is used directly in file path without validation.
    """
    # VULNERABLE: No path validation, allows ../../../etc/passwd
    file_path = os.path.join(UPLOAD_DIR, patient_id, filename)

    with open(file_path, "rb") as f:
        return f.read()


def save_patient_document(patient_id: str, filename: str, content: bytes) -> str:
    """
    Save a document for a patient.

    VULNERABILITY: Path Traversal (HIGH)
    Attacker can write files outside upload directory.
    """
    # VULNERABLE: No sanitization of patient_id or filename
    patient_dir = os.path.join(UPLOAD_DIR, patient_id)
    os.makedirs(patient_dir, exist_ok=True)

    file_path = os.path.join(patient_dir, filename)

    with open(file_path, "wb") as f:
        f.write(content)

    return file_path


def delete_patient_documents(patient_id: str) -> bool:
    """
    Delete all documents for a patient.

    VULNERABILITY: Path Traversal (HIGH)
    Could delete arbitrary directories.
    """
    # VULNERABLE: No validation allows deleting arbitrary paths
    patient_dir = os.path.join(UPLOAD_DIR, patient_id)

    if os.path.exists(patient_dir):
        shutil.rmtree(patient_dir)  # VULNERABLE: Could delete system files

    return True


def list_patient_documents(patient_id: str) -> list:
    """
    List all documents for a patient.

    VULNERABILITY: Path Traversal (HIGH)
    Could list contents of arbitrary directories.
    """
    # VULNERABLE: Allows listing any directory
    patient_dir = os.path.join(UPLOAD_DIR, patient_id)

    if os.path.exists(patient_dir):
        return os.listdir(patient_dir)
    return []
