"""Data parsers for JSON and YAML files."""
import json
import os
import sys
from types import MappingProxyType

import yaml

SUPPORTED_EXTENSIONS = MappingProxyType(
    {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    },
)


def get_extension(file_path: str) -> str:
    """Check extension for given file.

    Parameters:
        file_path: absolute path to the file

    Returns:
        File extension.
    """
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    for extension in SUPPORTED_EXTENSIONS:
        if file_extension == extension:
            return file_extension

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
            output = SUPPORTED_EXTENSIONS[get_extension(abs_path)](input_data)
    except FileNotFoundError:
        sys.exit(
            "File '{0}' does not exist. Program execution stopped.".format(
                file_path,
            ),
        )
    return output
