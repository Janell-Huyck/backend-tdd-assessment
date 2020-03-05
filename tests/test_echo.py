#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess


# Your test case class goes here


class TestEcho(unittest.TestCase):
    def test_no_manipulation(self):

        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "hEllo\n")

    def test_uppercase_manipulation(self):

        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "--upper"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "HELLO\n")

    def test_lowercase_manipulation(self):

        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "--lower"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "hello\n")

    def test_titlecase_manipulation(self):

        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "-t"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "Hello\n")

    # only the case manipulation that's listed last in the
    # usage file should be printed.

    def test_ult_returns_t(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "-ult"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "Hello\n")

    def test_ul_returns_l(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "-ul"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "hello\n")

    def test_ut_returns_t(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "-ut"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "Hello\n")

    def test_tl_returns_t(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "-tl"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "Hello\n")


if __name__ == '__main__':
    unittest.main()
