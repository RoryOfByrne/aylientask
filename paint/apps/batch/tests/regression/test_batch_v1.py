from django.test import Client, TestCase
from rest_framework.response import Response

class BatchV1Test(TestCase):

    def test_returns_impossible_on_if_batch_cannot_be_created(self):
        """When given requirements that cannot be met, the API should return 'IMPOSSIBLE'"""
        c: Client = Client()
        resp: Response = c.get('/v1/?input={%22colors%22:1,%22customers%22:2,%22demands%22:[[1,1,1],[1,1,0]]}')
        self.assertEqual(resp.json(), 'IMPOSSIBLE')

    def test_returns_a_well_formed_batch_when_correct_input_is_given(self):
        """When given valid requirements, the API should return a well-formed batch"""
        c: Client = Client()
        resp: Response = c.get('/v1/?input={%22colors%22:5,%22customers%22:3,%22demands%22:[[1,1,1],[2,1,0,2,0],[1,5,0]]}')
        self.assertEqual(resp.json(), '1 0 0 0 0')