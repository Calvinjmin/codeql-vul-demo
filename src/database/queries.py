"""
Database query utilities for patient records.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import sqlite3


def get_db_connection():
    """Get database connection."""
    return sqlite3.connect("patients.db")


def get_patient_by_id(patient_id: str) -> dict:
    """
    Fetch patient record by ID.

    VULNERABILITY: SQL Injection (HIGH)
    User input is directly concatenated into SQL query.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # FIX: Use parameterized query to prevent SQL injection
    query = "SELECT * FROM patients WHERE id = ?"
    cursor.execute(query, (patient_id,))

    result = cursor.fetchone()
    conn.close()
    return result


def search_patients(name: str, department: str) -> list:
    """
    Search patients by name and department.

    VULNERABILITY: SQL Injection (HIGH)
    Multiple user inputs concatenated into query.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # FIX: Use parameterized query to prevent SQL injection
    query = """
        SELECT * FROM patients
        WHERE name LIKE ?
        AND department = ?
    """
    cursor.execute(query, (f"%{name}%", department))

    results = cursor.fetchall()
    conn.close()
    return results


def delete_patient_record(patient_id: str) -> bool:
    """
    Delete a patient record.

    VULNERABILITY: SQL Injection (HIGH)
    Destructive operation with unvalidated input.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # FIX: Use parameterized query to prevent SQL injection
    query = "DELETE FROM patients WHERE id = ?"
    cursor.execute(query, (patient_id,))

    conn.commit()
    conn.close()
    return True
