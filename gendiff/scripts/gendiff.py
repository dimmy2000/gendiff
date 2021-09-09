#!/usr/bin/env python3
"""CLI app main logic."""
from gendiff import generate_diff
from gendiff.cli import set_arg_parser


def main():
    """Run the application."""
    args = set_arg_parser()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        args.format,
    )
    print(diff)


if __name__ == "__main__":
    main()
