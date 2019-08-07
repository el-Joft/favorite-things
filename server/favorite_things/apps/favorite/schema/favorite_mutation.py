import graphene

from favorite_things.apps.favorite.models import (
    Category, Favorite, MetaData, AuditLog)
from favorite_things.apps.favorite.schema.favorite_query import (CategoryType,
                                                                 FavoriteType)
from favorite_things.utils.database import get_existing_model, get_model_object
from favorite_things.utils.error_handler import errors
from favorite_things.utils.validation.favorite import favorite_validation


class CreateCategory(graphene.Mutation):
    """
        Mutation to create a Favorite Category
    """
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String(required=True)
    errors = graphene.List(graphene.String)
    message = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        if name.strip() == '':
            errors.custom_message("Category name cannot be empty")
        get_existing_model(Category, 'name', name)
        new_category = Category.objects.create(name=name)
        message = ["Successfully created a Favorite Category"]
        return CreateCategory(message=message, category=new_category)


class CreateFavorite(graphene.Mutation):
    """
      Mutation to create a Favorite
    """
    favorite = graphene.Field(FavoriteType)

    class Arguments:
        title = graphene.String(required=True)
        ranking = graphene.Int(required=True)
        description = graphene.String()
        metadata = graphene.List(graphene.JSONString)
        category = graphene.String(required=True)

    errors = graphene.List(graphene.String)
    message = graphene.List(graphene.String)

    @favorite_validation
    def mutate(self, info, **kwargs):
        metadata = kwargs.get('metadata')
        title = kwargs.get('title')
        category = kwargs.get('category')
        get_existing_model(Favorite, 'title', title)
        category_instance = get_model_object(
            Category, 'name', category)
        favorite = Favorite.objects.create(
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            ranking=kwargs.get('ranking'),
            category=category_instance
        )
        if favorite.ranking == 1:
            for fav in category_instance.favorite.all():
                if favorite == fav:
                    continue
                fav.ranking += 1
                fav.save()

        if metadata:
            for key in metadata:
                metadata_instance = MetaData()
                if key is not None:
                    metadata_instance.key = key['name']
                    metadata_instance.value = key['content']
                metadata_instance.favorite = favorite
                metadata_instance.save()

        message = ["Successfully created a Favorite"]
        return CreateFavorite(message=message, favorite=favorite)


class UpdateFavorite(graphene.Mutation):
    """
      Mutation to create a Favorite
    """
    favorite = graphene.Field(FavoriteType)

    class Arguments:
        id = graphene.String(required=True)
        title = graphene.String()
        ranking = graphene.Int()
        description = graphene.String()
        metadata = graphene.JSONString()
        category = graphene.String()

    errors = graphene.List(graphene.String)
    message = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        id = kwargs.get('id')
        category = kwargs.get('category')
        favorite_instance = get_model_object(
            Favorite, 'id', id)
        for key, value in kwargs.items():
            if key is not None:
                if key == 'category':
                    value = get_model_object(
                        Category, 'name', category)
                setattr(favorite_instance, key, value)
        favorite_instance.save()

        message = ["Successfully updated a Favorite"]
        return UpdateFavorite(message=message, favorite=favorite_instance)


class DeleteFavorite(graphene.Mutation):
    """
      Mutation to create a Favorite
    """
    favorite = graphene.Field(FavoriteType)

    class Arguments:
        id = graphene.String(required=True)

    errors = graphene.List(graphene.String)
    message = graphene.List(graphene.String)

    @favorite_validation
    def mutate(self, info, **kwargs):
        id = kwargs.get('id')
        if id.strip() == '':
            errors.custom_message("Favorite id cannot be empty")
        favorite_instance = get_model_object(
            Favorite, 'id', id)
        favorite_instance.delete()
        AuditLog.objects.create(
            table_name=Favorite.__name__,
            action=f'Deleted a Favorite: {favorite_instance.title}'
        )
        message = ["Deleted a Favorite successfully"]
        return DeleteFavorite(message=message, favorite=favorite_instance)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_favorite = CreateFavorite.Field()
    update_favorite = UpdateFavorite.Field()
    delete_favorite = DeleteFavorite.Field()
