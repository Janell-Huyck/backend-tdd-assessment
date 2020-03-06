#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo
import sys


class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser(sys.argv[1:])

    def test_display_full_help_with_h(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_display_help_with_no_args(self):

        process = subprocess.Popen(
            ["python", "./echo.py"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_no_manipulation(self):

        args = ["hEllo"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.text)
        self.assertEquals(echo.main(args), "hEllo")

    def test_uppercase_manipulation(self):

        args = ["hEllo", "-u"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO")

        args = ["hEllo", "--upper"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO")

    def test_lowercase_manipulation(self):

        args = ["hEllo", "-l"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), "hello")

        args = ["hEllo", "--lower"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), "hello")

    def test_titlecase_manipulation(self):

        args = ["hEllo", "-t"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(args), "Hello")

        args = ["hEllo", "--title"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(args), "Hello")

    # only the case manipulation that's listed last in the
    # usage file should be printed.

    def test_ult_returns_t(self):

        args = ["hEllo", "-ult"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(
            namespace.title and namespace.upper and namespace.lower)
        self.assertEquals(echo.main(args), "Hello")

    def test_ul_returns_l(self):

        args = ["hEllo", "-ul"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper and namespace.lower)
        self.assertFalse(namespace.title)
        self.assertEquals(echo.main(args), "hello")

    def test_ut_returns_t(self):

        args = ["hEllo", "-ut"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper and namespace.title)
        self.assertFalse(namespace.lower)
        self.assertEquals(echo.main(args), "Hello")

    def test_tl_returns_t(self):

        args = ["hEllo", "-tl"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title and namespace.lower)
        self.assertFalse(namespace.upper)
        self.assertEquals(echo.main(args), "Hello")


if __name__ == '__main__':
    unittest.main()
