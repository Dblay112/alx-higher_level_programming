#!/usr/bin/python3
"""Running the tests"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class testBase(unittest.TestCase):
    "class of all the tests"""

    def test_init(self):
        """tests class initialization with id"""
        tbase = Base(id=1)
        self.assertEqual(tbase.id, 1)

    def test_no_init(self):
        """tests class initialization without an id"""
        tbase = Base()
        self.assertEqual(tbase.id, 1)

    def test_nb_objects(self):
        """
        tests wehther class keeps track of
        nb objects created
        """
        tbase1 = Base()
        tbase2 = Base()
        self.assertEqual(Base.__nb_objects, 2)

    def test_base_basic(self):
        """tests base id functionality
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id + 1, b3.id)

    def test_given_id(self):
        """tests id with a set value and not a default
        """
        b1 = Base()
        b2 = Base(30)
        b3 = Base(55)
        b4 = Base()
        self.assertEqual(55, b3.id)
        self.assertEqual(b.id + 1, b4.id)
