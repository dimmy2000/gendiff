"""Stylish format methods."""
import json
from itertools import chain
from typing import Mapping

from gendiff.constants import DIFF_STATUS
from gendiff.constants import DIFF_VALUE
from gendiff.constants import STATUSES


def jsonify_lines(indent, parent, child, nested_indent):
    """Return list of JSON-formatted lines."""
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
        depth: counter of recursive function calls

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

    for parent, child in raw_input.items():
        formatted_lines.extend(
            jsonify_lines(deep_indent, parent, child, depth),
        )

    formatted_lines = chain(
        "{", formatted_lines, [closing_bracket_indent + "}"],  # noqa: WPS336
    )

    return "\n".join(formatted_lines)
