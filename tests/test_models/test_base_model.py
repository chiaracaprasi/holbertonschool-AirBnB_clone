#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pycodestyle
import json
import os

import models
Base = models.base_model.BaseModel


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel class """

    def setUp(self):
        """ general test setup, will create a temp baseModel """
        self.temp_b = Base()

    def tearDown(self):
        """ general tear down, will delete the temp baseModel """
        self.temp_b = None

    def test_type_creation(self):
        """ will test the correct type of creation """
        self.assertEqual(type(self.temp_b), Base)
