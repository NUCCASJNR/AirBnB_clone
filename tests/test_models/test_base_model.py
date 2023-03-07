#!/usr/bin/python3
""" Unittest test module for base model module
    """

from datetime import datetime, date
import unittest
from models.base_model import BaseModel


class TestBaseModel_Object_instance(unittest.TestCase):
    """ Test Base Model Object Instance

    Args:
        unittest (module): unittest module
    """

    def setUp(self):
        print("Testing Base Object Instance")

    def test_object_isinstance(self):
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_object_instance_not_equal(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1, b2)

    def test_object_instance_unique_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_object_instance_creation_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().created_at)

    def test_object_instance_sameday_creation(self):
        self.assertEqual(date.today().strftime("%d/%m/%Y"),
                         BaseModel().created_at.strftime("%d/%m/%Y"))

    def test_kwargs_param1(self):
        b3 = BaseModel(name="Al-Areef")
        self.assertEqual(b3.name, "Al-Areef")

    def test_kwargs_param2(self):
        b3 = BaseModel(name="Al-Areef", partner="Ayobami")
        self.assertEqual(b3.partner, "Ayobami")

    def test_object_ids_type(self):
        b1 = BaseModel()
        self.assertEqual(str, type(b1.id))

    def test_object_str_representation(self):
        b1 = BaseModel()
        self.assertIn("[BaseModel]", b1.__str__())
