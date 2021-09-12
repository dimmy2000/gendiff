"""Formatters for different data structures."""
import json
from types import MappingProxyType
from typing import Callable

from gendiff.constants import DIFF_STATUS
from gendiff.constants import DIFF_VALUE
from gendiff.formatters.json import jsonify_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

FORMATTERS = MappingProxyType(
    {
        "stylish": stylish,
        "plain": plain,
        "json": jsonify_diff,
    },
)


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


def format_output(raw_dict: dict, format_name: str) -> Callable[[dict], str]:
    """Return data formatted with given formatter."""
    return FORMATTERS[format_name](raw_dict)
