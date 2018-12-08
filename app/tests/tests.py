import unittest
from app import app


class TestViews(unittest.TestCase):

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)

    #ensures login page behaves correctly
    def test_login(self):
        tester = app.test_client(self)
        resp = tester.get('/login', content_type ='html/text')
        self.assertEqual(resp.status_code, 200)

    #ensure register page behaves correctly
    def test_register(self):
        tester = app.test_client(self)
        resp = tester.get('/register', content_type ='html/text')
        self.assertTrue(b'Register for an Account' in resp.data)


if __name__ == '__main__':
    unittest.main()
