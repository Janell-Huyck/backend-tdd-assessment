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


def create_parser(sys_args):
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

    return parser


def main(sys_args):
    """Implementation of echo"""
    parser = create_parser(sys_args)

    # main_args = parser.parse_args(sys_args)
    main_args = parser.parse_args(
        args=sys_args if len(sys_args) else ['--help'])
    result_text = main_args.text

    # manipulate the result text based off the passed
    # arguments.  Intentionally overwrite if mulitple
    # arguments are passed.
    if main_args.upper:
        result_text = main_args.text.upper()
    if main_args.lower:
        result_text = main_args.text.lower()
    if main_args.title:
        result_text = main_args.text.title()

    print(result_text)
    return result_text


if __name__ == '__main__':
    main(sys.argv[1:])
