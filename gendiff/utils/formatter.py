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


def jsonify_lines(indent, parent, child, nested_indent):
    """docstring."""
    line = "{0}{1} {2}: {3}"

    if isinstance(child, Mapping):
        status = child.get(DIFF_STATUS, "unchanged")
        if child.get("status"):
            if child["status"] == "updated":
                return [
                    line.format(
                        indent,
                        STATUSES["deleted"],
                        parent,
                        stylish(child[DIFF_VALUE], nested_indent),
                    ),
                    line.format(
                        indent,
                        STATUSES["added"],
                        parent,
                        stylish(child["updated_value"], nested_indent),
                    ),
                ]
            return [
                line.format(
                    indent,
                    STATUSES[status],
                    parent,
                    stylish(child[DIFF_VALUE], nested_indent),
                ),
            ]
        return [
            line.format(
                indent,
                STATUSES[status],
                parent,
                stylish(child, nested_indent),
            ),
        ]
    return [
        line.format(indent, " ", parent, stylish(child, nested_indent)),
    ]


def stylish(raw_input, depth=0) -> str:  # noqa: WPS210
    """Return string formatted in stylish format.

    Parameters:
        raw_input: dictionary with generated differences

    Returns:
        String formatted as a prettified JSON with indicated differences
    """
    if not isinstance(raw_input, Mapping):
        if not isinstance(raw_input, str):
            return json.dumps(raw_input)
        return raw_input

    formatted_lines = []
    spaces_count = 4
    replacer = " "

    closing_bracket_indent = replacer * depth
    depth += spaces_count
    # magic number 2 is len(status_indicator) + len(replacer)
    deep_indent = replacer * (depth - 2)

    for parent, child in sorted(raw_input.items()):
        formatted_lines.extend(
            jsonify_lines(deep_indent, parent, child, depth),
        )

    formatted_lines = chain(
        "{", formatted_lines, "{0}{1}".format(closing_bracket_indent, "}"),
    )

    return "\n".join(formatted_lines)


FORMATTERS = MappingProxyType(
    {
        "stylish": stylish,
    },
)


def format_output(raw_dict: dict, format_name: str) -> Callable[[dict], str]:
    """Return data formatted with given formatter."""
    return FORMATTERS[format_name](raw_dict)
