#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = """Janell.Huyck with help from madarp, knmarvel, and:
                https://stackoverflow.com/questions/4042452/display-
                    help-message-with-python-argparse-when-script-is-
                    called-without-any-argu"""


import sys
import argparse

if sys.version_info[0] >= 3:
    raise Exception("This program requires python2 interpreter")


def parse_args(sys_args):
    """Creates and returns an argparse cmd line option parser"""

    parser = argparse.ArgumentParser(add_help=True,
                                     description="""Perform transformation
                                     on input text.""")
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', action="store_true",
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action="store_true",
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action="store_true",
                        help='convert text to titlecase')

    if len(sys.argv) == 1:
        print("\nCaught with too few arguments. How embarrassing...\n")
        parser.print_help(sys.stderr)
        sys.exit(1)

    parsed_args = parser.parse_args(sys_args)

    return parsed_args


def main():
    """Implementation of echo"""
    args = parse_args(sys.argv[1:])
    result_text = args.text

    # manipulate the result text based off the passed
    # arguments.  Intentionally overwrite if mulitple
    # arguments are passed.
    if args.upper:
        result_text = args.text.upper()
    if args.lower:
        result_text = args.text.lower()
    if args.title:
        result_text = args.text.title()

    print(result_text)


if __name__ == '__main__':
    main()
