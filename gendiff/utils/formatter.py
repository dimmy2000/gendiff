"""Formatters for different data structures."""
import json
from collections.abc import Mapping
from itertools import chain
from types import MappingProxyType
from typing import Callable

from gendiff.utils.constants import DIFF_STATUS
from gendiff.utils.constants import DIFF_VALUE
from gendiff.utils.constants import STATUSES


def mutate_dict(
    status: str,
    old_value: str,
    new_value: str = None,
) -> dict:
    """Return a dictionary of a specific format."""
    if new_value is None:
        return {DIFF_STATUS: status, DIFF_VALUE: json.loads(old_value)}

    return {
        DIFF_STATUS: status,
        DIFF_VALUE: json.loads(old_value),
        "updated_value": json.loads(new_value),
    }


def jsonify_lines(indent, status, parent, child):
    return "{0}{1} {2}: {3}".format(indent, status, parent, child)


def stylish(raw_input, depth=0) -> str:
    """Return string formatted in stylish format.

    Parameters:
        diff_dict: dictionary with generated differences

    Returns:
        String formatted as a prettified JSON with indicated differences
    """
    if not isinstance(raw_input, Mapping):
        if raw_input in {True, False, None}:
            return json.dumps(raw_input)
        return str(raw_input)
    output = []
    dict_items = sorted(raw_input.items())
    spaces_count = 4
    replacer = " "

    deep_spaces_count = depth + spaces_count
    # 2 - status_indicator + replacer
    deep_indent = replacer * (deep_spaces_count + - 2)
    current_indent = replacer * depth

    for parent, child in dict_items:
        if isinstance(child, Mapping):
            status = child.get(DIFF_STATUS, "unchanged")
            if child.get("status"):
                if child["status"] != "updated":
                    lines = [
                        jsonify_lines(deep_indent, STATUSES[status], parent, stylish(child["value"], deep_spaces_count)),
                    ]
                else:
                    lines = [
                        jsonify_lines(deep_indent, STATUSES["deleted"], parent, stylish(child["value"], deep_spaces_count)),
                        jsonify_lines(deep_indent, STATUSES["added"], parent, stylish(child["updated_value"], deep_spaces_count)),
                    ]
            else:
                lines = [
                    jsonify_lines(deep_indent, STATUSES[status], parent, stylish(child, deep_spaces_count)),
                ]
            output.extend(lines)
        else:
            output.append(
                jsonify_lines(deep_indent, " ", parent, stylish(child, deep_spaces_count)),
            )

    output = chain("{", output, [current_indent + "}"])

    return "\n".join(output)


FORMATTERS = MappingProxyType(
    {
        "stylish": stylish,
    },
)


def format_output(raw_dict: dict, format_name: str) -> Callable[[dict], str]:
    """Return data formatted with given formatter."""
    return FORMATTERS[format_name](raw_dict)
