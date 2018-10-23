from aiopg.sa import SAConnection as SAConn
from aiopg.sa.result import RowProxy
from info.reviews.tables import review


async def select_review_by_id(conn: SAConn, pk: int) -> RowProxy:
    cursor = await conn.execute(
        review.select().where(review.c.id == pk)
    )
    item = await cursor.fetchone()
    return item

async def create_review(conn: SAConn, text: str) ->RowProxy:
    cursor = await conn.execute(
        review.insert().values(
            {
                'text': text,
            }
        )
    )
    item = await cursor.fetchone()
    return item.id
