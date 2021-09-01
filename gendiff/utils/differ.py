"""Difference generator methods."""
from collections.abc import Mapping

from gendiff.utils.constants import STATUSES
from gendiff.utils.loader import read_data

STATUS = "status"
STATUSES = list(STATUSES.keys())


def validate_dict(status, old_value, new_value=None):
    """Return a dictionary of a specific format."""
    if new_value is None:
        return {STATUS: status, "value": old_value}
    return {STATUS: status, "value": old_value, "updated_value": new_value}


def extract_keys(first_dict: dict, second_dict: dict) -> tuple:
    """Extract keys from two given dicts into three sets.

    Parameters:
        first_dict: first given dictionary
        second_dict: second given dictionary

    Returns:
        Three sets of keys:
        intersected: keys that are in both dictionaries.
        added: keys that are only in second_dict
        removed: keys that are only in first_dict
    """
    intersected = first_dict.keys() & second_dict.keys()
    added = second_dict.keys() - first_dict.keys()
    removed = first_dict.keys() - second_dict.keys()
    return (intersected, added, removed)


def compare_keys(first, second) -> dict:
    """Compare two given values."""
    if first == second:
        return validate_dict(STATUSES[2], first)

    elif isinstance(first, Mapping) and isinstance(second, Mapping):
        return validate_dict(STATUSES[3], collect_diffs(first, second))

    return validate_dict(STATUSES[3], first, second)


def collect_diffs(before: dict, after: dict) -> dict:  # noqa: WPS210
    """Collect differences between two dicts."""
    intersected, added, removed = extract_keys(before, after)
    diff = {}

    for added_key in added:
        diff[added_key] = validate_dict(STATUSES[0], after[added_key])

    for removed_key in removed:
        diff[removed_key] = validate_dict(STATUSES[1], before[removed_key])

    for key in intersected:
        diff[key] = compare_keys(before[key], after[key])

    return diff


def generate_diff(first_file: str, second_file: str) -> str:
    """Generate difference between two given files.

    Parameters:
        first_file: path to the first file
        second_file: path to the second file

    Returns:
          Difference between two files.
    """
    data1 = read_data(first_file)
    data2 = read_data(second_file)

    return collect_diffs(data1, data2)
