#!/usr/bin/python3
"""
    Test Place unittest module

"""

from datetime import datetime, date
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace_object_instance(unittest.TestCase):
    """
        Test Place class object instance
    """

    def setUp(self):
        print("Testing Place Object Insrtance")

    def test_Place_is_a_subclass_basemodel(self):
        p1 = Place()
        self.assertIsInstance(p1, BaseModel)

    def test_Place_unique_two_id(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_Place_unique_three_ids(self):
        p1 = Place()
        p2 = Place()
        p3 = Place()
        self.assertNotEqual(p2.id, p3.id)

    def test_Place_city_default_id(self):
        p1 = Place()
        self.assertEqual(p1.city_id, "")
        self.assertIn("city_id", dir(p1))

    def test_place_user_id_default_id(self):
        p1 = Place()
        self.assertEqual(p1.user_id, "")

    def test_name_default_value(self):
        p1 = Place()
        self.assertEqual(p1.name, "")

    def test_description_default_value(self):
        p1 = Place()
        self.assertEqual(p1.description, "")

    def test_number_rooms_default_value(self):
        p1 = Place()
        self.assertEqual(p1.number_rooms, 0)

    def test_number_bathrooms_default_value(self):
        p1 = Place()
        self.assertEqual(p1.number_bathrooms, 0)

    def test_max_guest_default_value(self):
        p1 = Place()
        self.assertEqual(p1.max_guest, 0)

    def test_price_by_night(self):
        p1 = Place()
        self.assertEqual(p1.price_by_night, 0)

    def test_latitude_default_value(self):
        p1 = Place()
        self.assertEqual(p1.latitude, 0.0)

    def test_longitude_default_value(self):
        p1 = Place()
        self.assertEqual(p1.longitude, 0.0)

    def test_place_ids_default_value(self):
        p1 = Place()
        self.assertEqual(p1.amenity_ids, [])

    def test_place_object_creation_time(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.created_at, p2.created_at)

    def test_place_object_updated_time(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.updated_at, p2.updated_at)


class TestPlace_Has_attr_BaseModel(unittest.TestCase):

    """
        Test Place for basemodel attributes
    """

    def setUp(self):
        print("Testing if Place has the attributes of BaseModel")

    def test_Place_has_id_attr(self):
        p1 = Place()
        self.assertTrue(p1.id)

    def test_Place_has_created_at_attr(self):
        p1 = Place()
        self.assertTrue(p1.created_at)

    def test_place_has_updated_at_attr(self):
        p1 = Place()
        self.assertTrue(p1.updated_at)
        
    def test_place_has__str__attr(self):
        p1 = Place()
        self.assertTrue(p1.__str__)



if __name__ == "__main__":
    unittest.main()
