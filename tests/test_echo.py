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

    def test_all_case_manipulation(self):

        process = subprocess.Popen(
            ["python", "./echo.py", "hEllo", "-ult"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout, "HELLO\nhello\nHello\n")


if __name__ == '__main__':
    unittest.main()
