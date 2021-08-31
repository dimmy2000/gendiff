"""Constants used by app utilities."""
import json
from types import MappingProxyType

import yaml

# Immutable dict
SUPPORTED_EXTENSIONS = MappingProxyType(
    {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    },
)

STATUSES = MappingProxyType(
    {
        "added": "+",
        "deleted": "-",
        "unchanged": " ",
    },
)

FORMATS = (
    "stylish",
)
