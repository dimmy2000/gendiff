"""Data parsers for JSON and YAML files."""
import json
import os
import sys

import yaml

formats = {
    ".json": json.load,
    ".yaml": yaml.safe_load,
    ".yml": yaml.safe_load,
}


def check_extension(file_path: str) -> str:
    """Check extension for given file.

    Parameters:
        file_path: absolute or relative path to the file

    Returns:
        File extension.
    """
    for file_type in formats:
        if file_path.endswith(file_type):
            return file_type
    sys.exit(
        "Program does not support given file format. "
        "Use JSON or YAML files instead.",
    )


def read_data(file_path: str) -> dict:
    """Read data from file.

    Parameters:
        file_path: absolute or relative path to the file

    Returns:
        Dictionary object with file contents.
    """
    abs_path = os.path.abspath(file_path)

    try:
        with open(abs_path, "r") as input_data:
            output = formats[check_extension(abs_path)](input_data)
    except FileNotFoundError:
        sys.exit(
            "File '{0}' does not exist. Program execution stopped.".format(
                file_path,
            ),
        )
    return output
