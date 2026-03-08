"""
Configuration loading utilities.
WARNING: This file contains intentional vulnerabilities for demo purposes.
"""
import yaml


def load_config_from_string(config_yaml: str) -> dict:
    """
    Load configuration from YAML string.

    VULNERABILITY: Insecure Deserialization (MEDIUM)
    yaml.load() without Loader allows arbitrary code execution.
    """
    # VULNERABLE: yaml.load() uses FullLoader by default in older versions,
    # or unsafe Loader - allows !!python/object and code execution
    # py/unsafe-deserialization
    return yaml.load(config_yaml, Loader=yaml.Loader)  # VULNERABLE: Unsafe loader


def load_config_file(filepath: str) -> dict:
    """
    Load configuration from YAML file.

    VULNERABILITY: Insecure Deserialization (MEDIUM)
    """
    with open(filepath, "r") as f:
        # VULNERABLE: Should use yaml.safe_load()
        return yaml.load(f, Loader=yaml.UnsafeLoader)  # py/unsafe-deserialization


def parse_user_config(user_provided_yaml: str) -> dict:
    """
    Parse user-submitted YAML configuration.

    VULNERABILITY: Insecure Deserialization (MEDIUM)
    User input deserialized with unsafe loader.
    """
    # VULNERABLE: User can submit malicious YAML with !!python/object
    return yaml.load(user_provided_yaml, Loader=yaml.UnsafeLoader)  # py/unsafe-deserialization
