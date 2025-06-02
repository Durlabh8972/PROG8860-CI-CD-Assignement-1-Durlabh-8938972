import unittest
from app import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Enhanced CI/CD Flask App!", response.data)

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Service is healthy", response.data)

    def test_invalid_url(self):
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
