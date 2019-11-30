from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SearchTests(APITestCase):

    def setUp(self):
        self.url = '/google-search/'

    def test_search_post_valid(self):
        """
        Ensure we can are able to search a query.
        """
        data = {'query_param': 'star wars'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data), 0)

    def test_search_post_invalid(self):
        """
        Ensure we can are able to search a query.
        """
        data = {'some_bad_key': 'star wars'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data), 0)

    def test_search_get(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)