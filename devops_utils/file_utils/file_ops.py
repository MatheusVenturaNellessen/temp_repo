print(f"Importing {__name__} module...\n")

import yaml
import json
from typing import Any
import sys

SUPPORTED_EXTENSIONS: list[str] = [
    ".yaml",
    ".yml",
    ".json"
]

def check_file_extension(filename: str) -> bool:
    """Checks if a file has a supported extension"""
    print(f"\t- {__name__}.{sys._getframe(0).f_code.co_name} called for {filename} by {__name__}.{sys._getframe(1).f_code.co_name}\n")

    filename_lower: str = filename.lower()

    return any(filename_lower.endswith(extension) for extension in SUPPORTED_EXTENSIONS)

def parse_yaml_or_json_file(file_path: str) -> dict[str, list[str]]:
    """Parses a YAML or JSON file and returns its content"""
    print(f"\t- {__name__}.{sys._getframe().f_code.co_name} called for {file_path} by {__name__}.{sys._getframe(1).f_code.co_name}\n")

    file_extension_is_valid: bool = check_file_extension(file_path)
    
    if not file_extension_is_valid:
        raise ValueError("File extension must be YAML or JSON")
    
    try:
        with open(file = file_path, mode = "r", encoding = "utf-8") as file:
            file_path_lower: str = file_path

            if file_path_lower.endswith(".json"):
                return json.load(file)

            return yaml.safe_load(file)

    except (json.JSONDecodeError, yaml.YAMLError) as parse_err:
        print(f"Error while parsing YAML or JSON file: {parse_err}\n")
        raise
