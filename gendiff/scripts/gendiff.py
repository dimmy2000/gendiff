#!/usr/bin/env python3
"""Main logic of application."""
from gendiff.cli import init_arg_parser


def main():
    """Run the application."""
    args = init_arg_parser()
    print(args)


if __name__ == "__main__":
    main()
