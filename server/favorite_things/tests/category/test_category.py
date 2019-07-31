from favorite_things.tests.base_config import BaseConfiguration
from favorite_things.tests.test_fixtures.category import (
    create_category_query, all_category, single_category
)


class TestCategory(BaseConfiguration):
    """
    Testing Category schema
    """

    def test_category(self):
        """
        test category
        """
        resp = self.query(
            create_category_query.format(**self.category_data_2))
        self.assertIn('data', resp)
        self.assertEqual(resp['data']['createCategory']['errors'], None)
        self.assertEqual(resp['data']['createCategory']
                         ['category']['name'],
                         self.category_data_2['name'])

    def test_category_invalid_data(self):
        """
        test invalid data
        """
        self.category_data_2['name'] = ''
        resp = self.query(
            create_category_query.format(**self.category_data_2))
        self.assertIn('data', resp)
        self.assertIn('errors', resp)
        self.assertEqual(
            resp['errors'][0]['message'], 'Category name cannot be empty')

    def test_all_category(self):
        """ test to return all category"""
        resp = self.query(
            all_category)
        self.assertIn('data', resp)
        self.assertNotIn("errors", resp)

    def test_single_category(self):
        """ test to single category"""
        data = {
            'id': self.category.id
        }
        resp = self.query(
            single_category.format(**data))
        self.assertIn('data', resp)
        self.assertNotIn("errors", resp)

    def test_invalid_category_data(self):
        """ test to single category with invalid data"""
        data = {
            'id': ''
        }
        resp = self.query(
            single_category.format(**data))
        self.assertIn('data', resp)
        self.assertIn('errors', resp)
