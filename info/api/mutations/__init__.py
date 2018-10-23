import graphene

from info.api.mutations.reviews import WriteReview


class Mutations(graphene.ObjectType):
    """
    All created mutations
    """
    create_review = WriteReview.Field(
        description='Review for a book'
    )
