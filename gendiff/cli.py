"""Command line interface methods."""
import argparse
import json
import os
import sys

operations = {
    "added": "+",
    "deleted": "-",
    "unchanged": " ",
}


def set_arg_parser():
    """Create argument parser.

    Returns:
         Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Generate diff")

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    return parser.parse_args()


def jsonify(input_data):
    """Return json object of input data."""
    return json.dumps(input_data)


def read_data(file_path):
    """Read data from file.

    Parameters:
        file_path: absolute or relative path to the file

    Returns:
        Dictionary object with file contents.
    """
    abs_path = os.path.abspath(file_path)

    try:
        with open(abs_path, "r") as input_data:
            output = json.load(input_data)
    except FileNotFoundError:
        sys.exit(
            "File '{0}' does not exist. Program execution stopped.".format(
                file_path,
            ),
        )
    return output


def collect_diffs(first_dict, second_dict, keys):
    """Collect differences between two given dictionaries into a list."""
    diff = []
    diff_list = []
    row = "  {0} {1}: {2}"

    for key in keys:
        if key not in first_dict:
            diff = [
                row.format(
                    operations["added"], key, jsonify(second_dict[key]),
                ),
            ]
        elif key not in second_dict:
            diff = [
                row.format(
                    operations["deleted"], key, jsonify(first_dict[key]),
                ),
            ]
        elif first_dict[key] == second_dict[key]:
            diff = [
                row.format(
                    operations["unchanged"], key, jsonify(second_dict[key]),
                ),
            ]
        else:
            diff = [
                row.format(
                    operations["deleted"], key, jsonify(first_dict[key]),
                ),
                row.format(
                    operations["added"], key, jsonify(second_dict[key]),
                ),
            ]
        diff_list.extend(diff)

    diff_list.insert(0, "{")
    diff_list.append("}")

    return diff_list


def generate_diff(first_file, second_file):
    """Calculate difference between two given files.

    Parameters:
        first_file: filepath to the first file
        second_file: filepath to the second file

    Returns:
          Difference between given files.
    """
    data1 = read_data(first_file)
    data2 = read_data(second_file)
    keys = sorted(data1.keys() | data2.keys())

    output = collect_diffs(data1, data2, keys)

    return "\n".join(output)
