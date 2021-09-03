"""Constants used by app utilities."""
import json
from collections import OrderedDict
from types import MappingProxyType

import yaml

FORMAT_NAMES = (
    "stylish",
)

DIFF_STATUS = "status"
DIFF_VALUE = "value"

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
