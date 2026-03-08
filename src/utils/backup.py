"""
Backup utilities for patient data export.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import os
import subprocess


def run_backup_script(script_name: str) -> bool:
    """
    Execute a backup script by name.

    VULNERABILITY: Command Injection (HIGH)
    User input passed directly to shell execution.
    """
    # VULNERABLE: script_name from user input, no sanitization
    # Attacker can use: "; rm -rf /" or "backup.sh && cat /etc/passwd"
    os.system(f"/opt/scripts/{script_name}")  # py/command-line-injection
    return True


def export_patient_data(patient_id: str, format_type: str) -> str:
    """
    Export patient data using external tool.

    VULNERABILITY: Command Injection (HIGH)
    User-controlled values in subprocess call.
    """
    # VULNERABLE: Both patient_id and format_type from user input
    cmd = f"python export_tool.py --patient {patient_id} --format {format_type}"
    subprocess.call(cmd, shell=True)  # py/command-line-injection
    return f"Exported {patient_id} as {format_type}"


def run_system_diagnostic(diagnostic_type: str) -> str:
    """
    Run system diagnostic command.

    VULNERABILITY: Command Injection (HIGH)
    """
    # VULNERABLE: User input in shell command
    result = subprocess.check_output(
        f"diagnose --type {diagnostic_type}",  # py/command-line-injection
        shell=True,
        text=True
    )
    return result


def execute_custom_report(report_name: str) -> bool:
    """
    Execute a custom report generator.

    VULNERABILITY: Command Injection (HIGH)
    """
    # VULNERABLE: report_name could be "report; id"
    os.system(f"generate_report.sh '{report_name}'")  # py/command-line-injection
    return True


def run_dynamic_filter(filter_expr: str, data: list) -> list:
    """
    Filter data using user-provided expression.

    VULNERABILITY: Code Injection via eval (HIGH)
    User input passed to eval() allows arbitrary code execution.
    """
    # VULNERABLE: filter_expr from user - e.g. "__import__('os').system('id')"
    return [item for item in data if eval(filter_expr)]  # py/code-injection
