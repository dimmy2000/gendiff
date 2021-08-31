"""Data parsers for given files."""
import os
import sys

from gendiff.utils.constants import SUPPORTED_EXTENSIONS


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
