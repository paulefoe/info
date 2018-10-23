from graphene.relay import Node

from info.api.queries.reviews import ReviewsQuery


class Query(ReviewsQuery):
    """
    The main GraphQL query point.
    """
    node = Node.Field()
