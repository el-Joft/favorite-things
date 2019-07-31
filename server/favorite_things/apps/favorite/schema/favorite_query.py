import graphene
from graphene_django import DjangoObjectType

from favorite_things.apps.favorite.models import AuditLog, Category, Favorite
from favorite_things.utils.database import get_model_object
from favorite_things.utils.error_handler import errors


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class AuditLogType(DjangoObjectType):
    class Meta:
        model = AuditLog


class FavoriteType(DjangoObjectType):
    class Meta:
        model = Favorite


class Query(graphene.ObjectType):
    favorites = graphene.List(
        FavoriteType,
    )

    audits = graphene.List(AuditLogType)
    categories = graphene.List(CategoryType)
    category = graphene.Field(
        CategoryType,
        id=graphene.String(required=True)
    )
    favorite = graphene.Field(
        FavoriteType,
        id=graphene.String(required=True))

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_favorites(self, info, **kwargs):
        return Favorite.objects.all()

    def resolve_audits(self, info, **kwargs):
        return AuditLog.objects.all()

    def resolve_favorite(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return get_model_object(Favorite, 'id', id)
        errors.custom_message("Invalid {id} input".format(id))

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return get_model_object(Category, 'id', id)
        errors.custom_message("Invalid {id} input".format(id))
