#!/usr/bin/env python3
"""Main logic of application."""
from gendiff import generate_diff
from gendiff import set_arg_parser


def main():
    """Run the application."""
    args = set_arg_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
