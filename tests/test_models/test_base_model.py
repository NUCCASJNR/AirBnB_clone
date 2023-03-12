#!/usr/bin/python3
""" Unittest test module for base model module
    """

import os
from datetime import datetime, date
import unittest
from models.base_model import BaseModel
from time import sleep
import os


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

    def test_object_instance_updated_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().updated_at)

    def test_object_instance_sameday_creation(self):
        self.assertEqual(date.today().strftime("%d/%m/%Y"),
                         BaseModel().created_at.strftime("%d/%m/%Y"))

    def test_kwargs_param1(self):
        b3 = BaseModel(name="Al-Areef")
        self.assertEqual(b3.name, "Al-Areef")

    def test_kwargs_param2(self):
        b3 = BaseModel(name="Al-Areef", partner="Ayobami")
        self.assertEqual(b3.partner, "Ayobami")

    def test_unique_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

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

    def test_to_dict_name(self):
        b = BaseModel()
        b.name = "My dict"
        d = b.to_dict()
        self.assertEqual(d["name"], b.name)

    def test_to_dict_age(self):
        b1 = BaseModel()
        b1.age = 16
        d = b1.to_dict()
        self.assertEqual(d["age"], b1.age)

    def test_to_dict_id(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)

    def test_to_dict_created_at(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["created_at"], b.created_at.isoformat())

    def test_to_dict_updated_at(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uniq_ids(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_diff_created_at(self):
        o1 = BaseModel()
        sleep(0.05)
        o2 = BaseModel()
        self.assertLess(o1.created_at, o2.created_at)

    def test_diff_updated_at(self):
        o1 = BaseModel()
        sleep(0.05)
        o2 = BaseModel()
        self.assertLess(o1.updated_at, o2.updated_at)\



class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
