import datetime

import graphene
from graphql import ResolveInfo

from info.api.models.review import Review
from info.reviews.db_utils import create_review


class WriteReview(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
    review = graphene.Field(Review)

    async def mutate(self, info: ResolveInfo, text: str):
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            review_id = await create_review(conn, text)

        return WriteReview(
            review=Review(review_id, text)
        )
