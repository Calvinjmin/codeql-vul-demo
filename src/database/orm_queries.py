"""
ORM-based database queries (SQLAlchemy).
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
from sqlalchemy import create_engine, text


def get_engine():
    """Get database engine."""
    return create_engine("sqlite:///patients.db")


def get_patient_by_ssn(ssn: str):
    """
    Fetch patient by SSN using raw SQL.

    VULNERABILITY: SQL Injection (HIGH)
    User input concatenated into SQLAlchemy text() clause.
    """
    engine = get_engine()
    # VULNERABLE: f-string in raw SQL - py/sql-injection
    query = text(f"SELECT * FROM patients WHERE ssn = '{ssn}'")
    with engine.connect() as conn:
        return conn.execute(query).fetchall()


def search_by_insurance(insurance_id: str, plan_type: str):
    """
    Search patients by insurance info.

    VULNERABILITY: SQL Injection (HIGH)
    Multiple injection points in raw SQL.
    """
    engine = get_engine()
    # VULNERABLE: Both inputs in query - py/sql-injection
    query = text(f"""
        SELECT * FROM patients
        WHERE insurance_id = '{insurance_id}'
        AND plan_type LIKE '%{plan_type}%'
    """)
    with engine.connect() as conn:
        return conn.execute(query).fetchall()


def update_patient_notes(patient_id: str, notes: str):
    """
    Update patient notes.

    VULNERABILITY: SQL Injection (HIGH)
    """
    engine = get_engine()
    # VULNERABLE: User input in UPDATE - py/sql-injection
    query = text(f"UPDATE patients SET notes = '{notes}' WHERE id = '{patient_id}'")
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()
