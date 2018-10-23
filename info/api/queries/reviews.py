import graphene
from graphql import ResolveInfo
from aiopg.sa.result import RowProxy

from info.api.models.review import Review
from info.reviews.db_utils import select_review_by_id


class ReviewsQuery(graphene.ObjectType):
    review = graphene.Field(
        Review,
        pk=graphene.Argument(graphene.Int),
        description='A review with given id',
    )

    async def resolve_review(self, info: ResolveInfo, pk) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            return await select_review_by_id(conn, pk)
