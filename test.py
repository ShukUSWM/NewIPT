import unittest
from flask import Flask
from api import app

class TestStaffEndpoints(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_get_staff(self):
        response = self.app.get("/staff")
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the response data if needed

    def test_get_staff_by_id(self):
        response = self.app.get("/staff/1")
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the response data if needed

if __name__ == "__main__":
    unittest.main()
