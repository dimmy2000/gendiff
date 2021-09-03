"""Difference generator methods."""
import json
from collections.abc import Mapping

from gendiff.constants import STATUSES_LIST
from gendiff.formatters import format_output
from gendiff.formatters import mutate_dict
from gendiff.loader import read_data


def extract_keys(first_dict: dict, second_dict: dict) -> tuple:
    """Extract keys from two given dicts into three sets.

    Parameters:
        first_dict: first given dictionary
        second_dict: second given dictionary

    Returns:
        Three sets of keys:
            intersected: keys that are in both dictionaries
            added: keys that are only in second dictionary
            removed: keys that are only in first dictionary
    """
    intersected = first_dict.keys() & second_dict.keys()
    added = second_dict.keys() - first_dict.keys()
    removed = first_dict.keys() - second_dict.keys()

    return (intersected, added, removed)


def compare_values(first, second) -> dict:
    """Compare two given values."""
    if first == second:
        return mutate_dict(STATUSES_LIST[2], json.dumps(first))

    elif isinstance(first, Mapping) and isinstance(second, Mapping):
        return mutate_dict(
            STATUSES_LIST[2],
            json.dumps(collect_diffs(first, second)),
        )
    return mutate_dict(STATUSES_LIST[3], json.dumps(first), json.dumps(second))


def collect_diffs(before, after) -> dict:  # noqa: WPS210
    """Create dictionary of differences between two given dicts.

    Parameters:
        before: dictionary before changes take effect
        after: dictionary after changes take effect

    Returns:
        Dictionary of collected differences between two given dictionaries.
    """
    intersected, added, removed = extract_keys(before, after)
    diff = {}

    for added_key in added:
        diff[added_key] = mutate_dict(
            STATUSES_LIST[0],
            json.dumps(after[added_key]),
        )

    for removed_key in removed:
        diff[removed_key] = mutate_dict(
            STATUSES_LIST[1],
            json.dumps(before[removed_key]),
        )

    for key in intersected:
        diff[key] = compare_values(before[key], after[key])

    return diff


def generate_diff(
    first_file: str,
    second_file: str,
    format_name: str = "stylish",
) -> str:
    """Generate difference between two given files.

    Parameters:
        first_file: path to the first file
        second_file: path to the second file

    Returns:
          Difference between two files.
    """
    data1 = read_data(first_file)
    data2 = read_data(second_file)

    output = collect_diffs(data1, data2)
    return format_output(output, format_name)
