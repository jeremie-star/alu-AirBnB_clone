#!/usr/bin/python3
"""Unit testing for the user class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases User class."""

    def test_instance(self):
        """testing if it's instance of User."""
        user = User()
        self.assertIsInstance(user, User)

    def test_is_class(self):
        """test is class."""
        user = User()
        self.assertEqual(str(type(user)),
                         "<class 'models.user.User'>")

    def test_is_subclass(self):
        """test if subclass."""
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_id(self):
        """test the id."""
        my_user = User()
        self.assertIsNotNone(my_user.id)

    def test_email(self):
        """test the email."""
        my_user = User()
        self.assertEqual(my_user.email, "")
        my_user.email = "airbnb@mail.com"
        self.assertEqual(my_user.email, "airbnb@mail.com")

    def test_password(self):
        """test the user password."""
        my_user = User()
        self.assertEqual(my_user.password, "")
        my_user.password = "peoplePower"
        self.assertEqual(my_user.password, "peoplePower")

    def test_first_name(self):
        """test the first name."""
        my_user = User()
        self.assertEqual(my_user.first_name, "")
        my_user.first_name = "Betty"
        self.assertEqual(my_user.first_name, "Betty")

    def test_last_name(self):
        """test the last name."""
        my_user = User()
        self.assertEqual(my_user.last_name, "")
        my_user.first_name = "Bar"
        self.assertEqual(my_user.first_name, "Bar")


if __name__ == "__main__":
    unittest.main()
