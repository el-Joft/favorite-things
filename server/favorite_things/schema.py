import graphene
from favorite_things.apps.favorite.schema import (
    favorite_query, favorite_mutation
)


class Query(favorite_query.Query, graphene.ObjectType):
    pass


class Mutation(favorite_mutation.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)
