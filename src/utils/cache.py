"""
Caching utilities for session and data caching.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import pickle
import base64
import os


CACHE_DIR = "/tmp/medsecure_cache"


def serialize_session(session_data: dict) -> str:
    """
    Serialize session data for storage.

    Uses pickle for serialization (will be deserialized unsafely later).
    """
    pickled = pickle.dumps(session_data)
    return base64.b64encode(pickled).decode("utf-8")


def deserialize_session(session_string: str) -> dict:
    """
    Deserialize session data from storage.

    VULNERABILITY: Insecure Deserialization (HIGH)
    Pickle can execute arbitrary code during deserialization.
    """
    # VULNERABLE: Deserializing untrusted data with pickle
    decoded = base64.b64decode(session_string)
    return pickle.loads(decoded)  # VULNERABLE: Arbitrary code execution


def load_cached_data(cache_key: str) -> any:
    """
    Load data from file cache.

    VULNERABILITY: Insecure Deserialization (HIGH)
    Loading pickled data from files that could be tampered with.
    """
    cache_path = os.path.join(CACHE_DIR, f"{cache_key}.cache")

    if os.path.exists(cache_path):
        with open(cache_path, "rb") as f:
            # VULNERABLE: Loading untrusted pickled data
            return pickle.load(f)

    return None


def save_cached_data(cache_key: str, data: any) -> bool:
    """Save data to file cache using pickle."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"{cache_key}.cache")

    with open(cache_path, "wb") as f:
        pickle.dump(data, f)

    return True


def process_user_cache(user_submitted_cache: str) -> dict:
    """
    Process cache data submitted by user (e.g., from cookie).

    VULNERABILITY: Insecure Deserialization (HIGH)
    Directly deserializing user-controlled input.
    """
    try:
        # VULNERABLE: User can submit malicious pickled data
        return deserialize_session(user_submitted_cache)
    except Exception:
        return {}
