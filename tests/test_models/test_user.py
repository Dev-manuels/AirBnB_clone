#!/usr/bin/python3
"""
Test module for class User
"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    TestUser -  tests User Class

    Args:
        unittest (SuperClass): _description_
    """
    def test_str(self):
        test_obj = User()
        test_obj2 = User()
        self.assertNotEqual(test_obj.__str__(), test_obj2.__str__())

    def test_init(self):
        test_obj = User()
        self.assertIsInstance(test_obj, User)

    def test_to_dict(self):
        test_obj = User()
        self.assertIn("__class__", test_obj.to_dict().keys())
        self.assertIn("id", test_obj.to_dict().keys())

    def test_save(self):
        test_obj = User()
        test_obj.save()
        self.assertNotEqual(test_obj.created_at, test_obj.updated_at)

    def test_init_kwargs(self):
        tmp_dict = {"id": "23822075-f2a7-4a03-af01-28ab47493e42",
                    "created_at": "2023-12-11T14:35:36.196906",
                    "updated_at": "2023-12-11T14:35:36.196906",
                    "email": "test@gmail.com",
                    "password": "test",
                    "first_name": "test",
                    "last_name": "test",
                    "__class__": "User"}
        test_obj = User(**tmp_dict)
        for key, value in tmp_dict.items():
            self.assertEqual(test_obj.to_dict()[key], value)

        
