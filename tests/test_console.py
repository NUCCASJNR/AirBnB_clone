#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):
    """
        Tests HBNBCommand console

    """

    def setUp(self):
        print("Testing Console methods")

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'Quit command to exit the program\n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates a new instance\n'
        self.assertEqual(s, f.getvalue())

    def test_help_default(self):
        """Tests default"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help default")
            s = '*** No help on default\n'
            self.assertEqual(s, f.getvalue())


if __name__ == "__main__":
    unittest.main()
