from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITransactionTestCase


from .views import *
from .models import *

#
#   These are not comprehensive tests!!
#

class MyAPI(APITransactionTestCase):

    reset_sequences = True

    def setUp(self):
        fixtures = ('data.json',)

    def test_list_sled(self):
        print("Testing Sled List")
        factory = APIRequestFactory()
        view = SledList.as_view()

        request = factory.get('/api/sleds/')
        response = (view(request)).render()

        self.assertEqual(response.status_code, 200)
        print("Successful Response Code:", response.status_code)

    def test_list_memebers(self):
        print("Testing Member List")
        factory = APIRequestFactory()
        view = MembersList.as_view()

        request = factory.get('/api/members/')
        response = (view(request)).render()

        self.assertEqual(response.status_code, 200)
        print("Successful Response Code:", response.status_code)