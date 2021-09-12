"""JSON format functions."""
import json


def jsonify_diff(raw_dict):
    """Return JSON formatted string."""
    return json.dumps(raw_dict, indent=2)
