from favorite_things.tests.base_config import BaseConfiguration
from favorite_things.tests.test_fixtures.favorite_query import (
    create_favorite_query, update_favorite_query, delete_favorite_query,
    all_favorites, single_favorite, all_audit_log
)


class TestFavorite(BaseConfiguration):
    """
    Testing Favorite schema
    """

    def setUp(self):
        super().setUp()
        self.new_favorite_data = {
            'title': 'Apples',
            'description': 'Test',
            'category': self.category,
            'ranking': 2
        }

    def test_create_favorite(self):
        """
        test create favorite
        """
        resp = self.query(
            create_favorite_query.format(**self.new_favorite_data))
        self.assertIn('data', resp)
        self.assertEqual(resp['data']['createFavorite']['errors'], None)
        self.assertEqual(resp['data']['createFavorite']
                         ['favorite']['title'],
                         self.new_favorite_data['title'])

    def test_empty_favorite(self):
        """ test empty favorite"""
        self.new_favorite_data['title'] = ''
        resp = self.query(
            create_favorite_query.format(**self.new_favorite_data))
        self.assertIn('errors', resp)
        self.assertEqual(
            resp['errors'][0]['message'], "['Title cannot be empty']")

    def test_update_favorite(self):
        """
        test update favorite
        """
        self.new_favorite_data['id'] = self.favorite2.id
        resp = self.query(
            update_favorite_query.format(**self.new_favorite_data))
        self.assertIn('data', resp)
        self.assertEqual(resp['data']['updateFavorite']['errors'], None)
        self.assertEqual(resp['data']['updateFavorite']
                         ['favorite']['title'],
                         self.new_favorite_data['title'])

    def test_delete_favorite(self):
        """
        test delete favorite
        """
        data = {
            'id': self.favorite2.id
        }
        resp = self.query(
            delete_favorite_query.format(**data))
        self.assertIn('data', resp)
        self.assertEqual(resp['data']['deleteFavorite']
                         ['favorite']['title'],
                         self.favorite_data2['title'])

    def test_all_favorite(self):
        """test to return all favorites"""
        resp = self.query(
            all_favorites)
        self.assertIn('data', resp)
        self.assertNotIn("errors", resp)

    def test_single_favorite(self):
        """ Test to return single favorite"""
        data = {
            'id': self.favorite2.id
        }
        resp = self.query(
            single_favorite.format(**data))
        self.assertIn('data', resp)
        self.assertNotIn("errors", resp)

    def test_all_audit_log(self):
        """ test to return all audit log"""
        resp = self.query(
            all_audit_log)
        self.assertIn('data', resp)
        self.assertNotIn("errors", resp)

    def test_invalid_favorite_data(self):
        """ test to single favorite with invalid data"""
        data = {
            'id': ''
        }
        resp = self.query(
            single_favorite.format(**data))
        self.assertIn('data', resp)
        self.assertIn('errors', resp)
