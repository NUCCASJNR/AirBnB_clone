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

    def test_object_ids_list(self):
        b2 = BaseModel()
        self.assertNotEqual(list,  type(b2.id))

    def test_object_ids_tuple(self):
        b1 = BaseModel()
        self.assertNotEqual(tuple, type(b1.id))

    def test_object_ids_bool(self):
        b2 = BaseModel()
        self.assertNotEqual(bool,  type(b2.id))

    def test_object_ids_None(self):
        b2 = BaseModel()
        self.assertNotEqual(None,  type(b2.id))

    def test_object_ids_float(self):
        b2 = BaseModel()
        self.assertNotEqual(float, type(b2.id))

    def test_object_ids_int(self):
        b1 = BaseModel()
        self.assertNotEqual(int, type(b1.id))

    def test_object_ids_dict(self):
        b2 = BaseModel()
        self.assertNotEqual(dict,  type(b2.id))

    def test_object_ids_complex(self):
        b2 = BaseModel()
        self.assertNotEqual(complex, type(b2.id))

    def test_object_ids_set(self):
        b2 = BaseModel()
        self.assertNotEqual(set, type(b2.id))

    def test_object_ids_frozenset(self):
        b2 = BaseModel()
        self.assertNotEqual(frozenset, type(b2.id))

    def test_object_ids_range(self):
        b2 = BaseModel()
        self.assertNotEqual(range, type(b2.id))

    def test_object_ids_bytes(self):
        b2 = BaseModel()
        self.assertNotEqual(bytes, type(b2.id))

    def test_object_ids_bytearray(self):
        b2 = BaseModel()
        self.assertNotEqual(bytearray, type(b2.id))

    def test_object_ids_memoryview(self):
        b2 = BaseModel()
        self.assertNotEqual(memoryview, type(b2.id))

    def test_object_str_representation(self):
        b1 = BaseModel()
        self.assertIn("[BaseModel]", b1.__str__())


    if __name__ == "__main__":
        unittest.main()
