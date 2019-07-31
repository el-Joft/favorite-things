from favorite_things.tests.base_config import BaseConfiguration
from favorite_things.apps.favorite.models import Category


class CategoryTestCase(BaseConfiguration):
    """Category Model test case."""

    def test_models_can_create_category(self):
        """Test creation of category"""
        old_count = Category.objects.count()
        self.category2.save()
        new_count = Category.objects.count()
        self.assertEqual(new_count, old_count + 1)

    def test_models_return_category_string_representation(self):
        """ Test category string representation """
        category = self.category
        self.assertEqual(str(category), 'Person')

    def test_category_model_property(self):
        """ Test category fields"""
        category = self.category
        self.assertEqual(category.name, 'Person')
