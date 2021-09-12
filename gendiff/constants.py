"""Constants used by app utilities."""
import json
from collections import OrderedDict
from types import MappingProxyType

import yaml

# Constants used by cli.py
FORMAT_NAMES = (
    "stylish",
    "plain",
)

# Constants used by formatter plain.py
DIFF_NEW_VALUE = "updated_value"
DIFF_STATUS = "status"
DIFF_VALUE = "value"

LINE = "Property '{0}'"
LINE_ADDED = "was added with value: {0}"
LINE_REMOVED = "was removed"
LINE_UPDATED = "was updated. From {0} to {1}"

# Constants used by formatter stylish.py
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

# Constants used by differ.py
STATUSES_LIST = list(STATUSES.keys())

# Constants used by parser.py and loader.py
# MappingProxyType == immutable dict
SUPPORTED_EXTENSIONS = MappingProxyType(
    {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    },
)
