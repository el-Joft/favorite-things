from favorite_things.tests.base_config import BaseConfiguration
from favorite_things.apps.favorite.models import (
    Favorite, AuditLog, MetaData
)


class FavoriteTestCase(BaseConfiguration):
    """Category Model test case."""

    def test_models_can_create_favorite(self):
        """Test creation of favorite"""
        old_count = Favorite.objects.count()
        self.favorite.save()
        new_count = Favorite.objects.count()
        self.assertEqual(new_count, old_count + 1)

    def test_models_return_favorite_string_representation(self):
        """ Test category string representation """
        favorite = self.favorite
        self.assertEqual(str(favorite), 'Grapes')

    def test_favorite_model_property(self):
        """ Test favorite properties"""
        favorite = self.favorite
        self.assertEqual(favorite.title, 'Grapes')
        self.assertEqual(favorite.description, 'Grapes description')
        self.assertEqual(favorite.category_id, self.category.id)

    def test_models_audit_log(self):
        """ Test auditlog creation"""
        old_count = AuditLog.objects.count()
        AuditLog.objects.create(
            table_name='Dummy Table',
            table_fields={"dummy": "dummy"},
            action='Created a new Favorite'
        )
        new_count = AuditLog.objects.count()
        self.assertEqual(new_count, old_count + 1)

    def test_models_meta_data(self):
        """ Test metadata creation"""
        old_count = MetaData.objects.count()
        metadata = MetaData.objects.create(
            key='Dummy key',
            value="Dummy value",
            favorite=self.favorite2
        )
        new_count = MetaData.objects.count()
        self.assertEqual(new_count, old_count + 1)
        self.assertEqual(str(metadata), 'Dummy key')
        self.assertEqual(metadata.key, 'Dummy key')
