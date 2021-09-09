"""Constants used by app utilities."""
import json
from collections import OrderedDict
from types import MappingProxyType

import yaml

FORMAT_NAMES = (
    "stylish",
    "plain",
)

DIFF_NEW_VALUE = "updated_value"
DIFF_STATUS = "status"
DIFF_VALUE = "value"

LINE = "Property '{0}'"
LINE_ADDED = "was added with value: {0}"
LINE_REMOVED = "was removed"
LINE_UPDATED = "was updated. From {0} to {1}"

STATUSES = MappingProxyType(
    OrderedDict(
        {
            "added": "+",
            "deleted": "-",
            "unchanged": " ",
            "updated": " ",
        },
    ),
)

STATUSES_LIST = list(STATUSES.keys())

# MappingProxyType == immutable dict
SUPPORTED_EXTENSIONS = MappingProxyType(
    {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    },
)
