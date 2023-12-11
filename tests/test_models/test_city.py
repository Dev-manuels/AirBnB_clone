#!/usr/bin/python3
"""
Test module for class City
"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
    TestCity _summary_

    Args:
        unittest (SuperClass): unittest.testcas
    """

    def test_str(self):
        test_obj = City()
        test_obj2 = City()
        self.assertNotEqual(test_obj.__str__(), test_obj2.__str__())

    def test_init(self):
        test_obj = City()
        self.assertIsInstance(test_obj, City)

    def test_to_dict(self):
        test_obj = City()
        self.assertIn("__class__", test_obj.to_dict().keys())
        self.assertIn("id", test_obj.to_dict().keys())

    def test_save(self):
        test_obj = City()
        test_obj.save()
        self.assertNotEqual(test_obj.created_at, test_obj.updated_at)

    def test_init_kwargs(self):
        tmp_dict = {"id": "23822075-f2a7-4a03-af01-28ab47493e42",
                    "created_at": "2023-12-11T14:35:36.196906",
                    "updated_at": "2023-12-11T14:35:36.196906",
                    "name": "test_city",
                    "state_id": "12345test",
                    "__class__": "City"}
        test_obj = City(**tmp_dict)
        for key, value in tmp_dict.items():
            self.assertEqual(test_obj.to_dict()[key], value)
