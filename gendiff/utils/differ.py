"""Difference generator methods."""
import json

from gendiff.utils.constants import STATUSES
from gendiff.utils.loader import read_data


def jsonify(input_data):
    """Return json object of input data."""
    return json.dumps(input_data)


def normalize_diff(diff_dict, key, operation):
    """Convert the diff to a required format string."""
    row = "  {0} {1}: {2}"
    return row.format(STATUSES[operation], key, jsonify(diff_dict[key]))


def check_diff(key, first_dict, second_dict):
    """Check the difference between two dicts."""
    if key not in first_dict:
        diff = normalize_diff(second_dict, key, "added")
    elif key not in second_dict:
        diff = normalize_diff(first_dict, key, "deleted")
    elif first_dict[key] == second_dict[key]:
        diff = normalize_diff(second_dict, key, "unchanged")
    else:
        diff = "{0}\n{1}".format(
            normalize_diff(first_dict, key, "deleted"),
            normalize_diff(second_dict, key, "added"),
        )

    return diff


def collect_diffs(first_dict: dict, second_dict: dict) -> list:
    """Collect differences between two dicts into a list."""
    keys = sorted(first_dict.keys() | second_dict.keys())
    diff_list = ["{", "}"]

    for key in keys:
        diff = check_diff(key, first_dict, second_dict)
        diff_list.insert(-1, diff)
    return diff_list


def generate_diff(first_file: str, second_file: str) -> str:
    """Generate difference between two given files.

    Parameters:
        first_file: filepath to the first file
        second_file: filepath to the second file

    Returns:
          Difference between two files as a string.
    """
    data1 = read_data(first_file)
    data2 = read_data(second_file)

    output = collect_diffs(data1, data2)

    return "\n".join(output)
