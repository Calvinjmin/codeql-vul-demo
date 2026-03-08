"""
Patient profile views.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
from html import escape


def render_profile_page(patient: dict) -> str:
    """
    Render patient profile page.

    VULNERABILITY: Cross-Site Scripting (MEDIUM)
    User input rendered without proper escaping.
    """
    # VULNERABLE: Patient name could contain <script> tags
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Patient Profile</title></head>
    <body>
        <h1>Patient Profile</h1>
        <div class="patient-info">
            <p><strong>Name:</strong> {patient['name']}</p>
            <p><strong>Email:</strong> {patient['email']}</p>
            <p><strong>Notes:</strong> {patient['notes']}</p>
        </div>
    </body>
    </html>
    """
    return html


def render_search_results(query: str, results: list) -> str:
    """
    Render search results page.

    VULNERABILITY: Reflected XSS (MEDIUM)
    Search query reflected in page without escaping.
    """
    # VULNERABLE: Query is reflected without sanitization
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Search Results</title></head>
    <body>
        <h1>Search Results for: {query}</h1>
        <p>Found {len(results)} results</p>
        <ul>
    """

    for result in results:
        # VULNERABLE: Result names not escaped
        html += f"<li>{result['name']} - {result['department']}</li>"

    html += """
        </ul>
    </body>
    </html>
    """
    return html


def render_error_message(error_message: str) -> str:
    """
    Render error page.

    VULNERABILITY: XSS via error messages (MEDIUM)
    Error messages may contain user input.
    """
    # VULNERABLE: Error message rendered without escaping
    return f"""
    <div class="error">
        <h2>Error</h2>
        <p>{error_message}</p>
    </div>
    """
