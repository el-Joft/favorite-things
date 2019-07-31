import json

from django.test import Client, TestCase

from favorite_things.apps.favorite.models import (
    Category, Favorite
)


class BaseConfiguration(TestCase):
    """
    Base configuration file for all tests.
    """

    @classmethod
    def setUpClass(cls):
        # We need to first run setUpClass function that we
        # inherited from TestCase.
        super(BaseConfiguration, cls).setUpClass()

        # Set up test client for all test classes
        # that will inherit from this class.
        cls.client = Client()

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        body = dict()
        body['query'] = query
        response = cls.client.post(
            '/favorite/', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

    def setUp(self):
        """
        Configurations to be made available before each
        individual test case inheriting from this class.
        """
        self.category_data = {
            'name': 'Person'
        }
        self.category_data_2 = {
            'name': 'Food'
        }
        self.category = Category(**self.category_data)
        self.category2 = Category(**self.category_data_2)
        self.category.save()
        self.favorite_data = {
            "title": "Grapes",
            "description": "Grapes description",
            "metadata": {
                "kg": "230"
            },
            "category_id": self.category.id,
            "ranking": 2
        }
        self.favorite_data2 = {
            "title": "Grapes",
            "description": "Grapes description",
            "metadata": {
                "kg": "230"
            },
            "category_id": self.category.id,
            "ranking": 2
        }
        self.favorite = Favorite(**self.favorite_data)
        self.favorite2 = Favorite(**self.favorite_data2)
        self.favorite2.save()

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        self.assertNotIn("errors", resp, "Response had errors")
        self.assertEqual(resp["data"], expected, "Response has correct data")
