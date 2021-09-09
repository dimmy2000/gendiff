"""Plain format methods."""
import json
from typing import Mapping

from gendiff.constants import DIFF_NEW_VALUE
from gendiff.constants import DIFF_STATUS
from gendiff.constants import DIFF_VALUE
from gendiff.constants import LINE
from gendiff.constants import LINE_ADDED
from gendiff.constants import LINE_REMOVED
from gendiff.constants import LINE_UPDATED


def validate_data(raw_input):
    """Check if input value is plain formatted."""
    if not isinstance(raw_input, Mapping):
        if not isinstance(raw_input, str):
            return json.dumps(raw_input)
        return repr(raw_input)
    return "[complex value]"


def flatten_diff_dict(nested_dict, root_path=None, diff_dict=None):
    """Return flattened dictionary of diffs."""
    flattened_dict = {}

    for parent, child in nested_dict.items():
        flattened_dict.update(
            get_diff_roots(parent, child, root_path, diff_dict),
        )

    return flattened_dict


def check_if_diff(diff_data):
    """Check if input data is dictionary of differences."""
    if isinstance(diff_data, Mapping):
        if DIFF_STATUS in diff_data:
            return True
    return False


def get_diff_roots(parent, child, root_path="", diff_dict=None):
    """Return dictionary of root paths for every diff."""
    root_path = "{0}".format(parent) if root_path is None else (
        "{0}.{1}".format(root_path, parent)
    )

    diff_dict = {} if diff_dict is None else diff_dict

    if check_if_diff(child):
        if isinstance(child[DIFF_VALUE], Mapping):
            flatten_diff_dict(child[DIFF_VALUE], root_path, diff_dict)

        if child[DIFF_STATUS] != "unchanged":
            diff_dict[root_path] = child

    return diff_dict


def format_line(root_path, diff_values_dict):
    """Return plain text formatted line."""
    lines_list = [LINE.format(root_path)]
    status = diff_values_dict[DIFF_STATUS]

    if status == "added":
        added_value = validate_data(diff_values_dict[DIFF_VALUE])
        lines_list.append(
            LINE_ADDED.format(added_value),
        )

    elif status == "deleted":
        lines_list.append(LINE_REMOVED)

    elif status == "updated":
        old_value = validate_data(diff_values_dict[DIFF_VALUE])
        new_value = validate_data(diff_values_dict[DIFF_NEW_VALUE])
        lines_list.append(
            LINE_UPDATED.format(
                old_value,
                new_value,
            ),
        )

    return " ".join(lines_list)


def plain(raw_dict):
    """Return string formatted in plain format.

    Parameters:
        raw_dict: dictionary with generated differences

    Returns:
        String of differences formatted as a plain text
    """
    formatted_lines = []
    flattened_dict = flatten_diff_dict(raw_dict)

    for parent, child in flattened_dict.items():
        formatted_lines.append(format_line(parent, child))

    formatted_lines.sort()

    return "\n".join(formatted_lines)
