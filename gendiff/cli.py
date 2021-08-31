"""Command line interface methods."""
import argparse

from gendiff.utils.constants import FORMATS


def set_arg_parser() -> argparse.Namespace:
    """Create argument parser.

    Returns:
         Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Generate diff")

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        metavar="FORMAT",
        help="set format of output from stylish, plain or json",
        choices=FORMATS,
        default=FORMATS[0],
    )

    return parser.parse_args()
