#!/usr/bin/python3
"""
    Test City unittest module
"""

from datetime import datetime, date
import unittest
from models.city import City
from models.base_model import BaseModel

class Test_City_object_instance(unittest.TestCase):
    """ Test City class object instance"""

    def setUp(self):
        print("Testing City object instance")

    def test_city_is_a_subclass_basemodel(self):
        c1 = City()
        self.assertIsInstance(c1, BaseModel)

    def test_city_two_id(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_city_three_ids(self):
        c1 = City()
        c2 = City()
        c3 = City()
        self.assertNotEqual(c2.id, c3.id)

    def test_id_type(self):
        c1 = City()
        self.assertEqual(type(c1.id), str)

    def test_created_at_time(self):
        c1 = City()
        self.assertNotEqual(datetime.now(), c1.created_at)

    def test_updated_at_time(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.updated_at, c2.updated_at)

    def test_state_id_value(self):
        c1 = City()
        self.assertEqual(c1.state_id, "")

    def test_name(self):
        c1 = City()
        self.assertEqual(c1.name, "")

class TestCity_Has_Attr_basemodel(unittest.TestCase):
    """
            Test City for basemodel attributes
    """

    def setUp(self):
        print("Testing if City has the attributes of BaseModel")

    def test_city_has_id_attr(self):
        c1 = City()
        self.assertTrue(c1.id)

    def test_city_has_created_at_attr(self):
        c1 = City()
        self.assertTrue(c1.created_at)

    def test_city_has_updated_at_attr(self):
        c1 = City()
        self.assertTrue(c1.updated_at)

    def test_city_has___str__attr(self):
        c1 = City()
        self.assertTrue(c1.__str__)

    def test_city_has_to_dict_attr(self):
        c1 = City()
        self.assertTrue(c1.to_dict)

    def test_City_kwargs(self):
        c1 = City(name="idan")
        self.assertEqual(c1.name, "idan")


if __name__ == "__main__":
   unittest.main()
