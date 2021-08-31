"""Data loaders."""
import os
import sys

from gendiff.utils.constants import SUPPORTED_EXTENSIONS
from gendiff.utils.parser import get_extension


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
