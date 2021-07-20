"""Command line interface methods."""
import argparse


def init_arg_parser():
    """Create argument parser.

    Positional arguments:
        first_file
        second_file

    Returns:
         parsed arguments
    """
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    return parser.parse_args()
