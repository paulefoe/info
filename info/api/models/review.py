import graphene
from aiopg.sa.result import RowProxy
from graphql import ResolveInfo

class Review(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
