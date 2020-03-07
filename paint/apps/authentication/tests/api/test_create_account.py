from django.test import Client,TestCase
from rest_framework.response import Response

class TestCreateAccountRoute(TestCase):

    def test_creating_an_account_should_return_201(self):
        c: Client = Client()
        resp: Response = c.post('/v2/auth/register/', {'identifier': 'abc', 'password': 'agoodpw1234@'})

        self.assertEqual(resp.status_code, 201)

    def test_short_password_should_return_400(self):
        c: Client = Client()
        resp: Response = c.post('/v2/auth/register/', {'identifier': 'abc', 'password': 'abc'})

        self.assertEqual(resp.status_code, 400)

    def test_common_password_should_return_400(self):
        c: Client = Client()
        resp: Response = c.post('/v2/auth/register/', {'identifier': 'abc', 'password': 'password'})

        self.assertEqual(resp.status_code, 400)
