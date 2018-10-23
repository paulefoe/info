import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from info.migrations import metadata


review = sa.Table(
    'review', metadata,
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('text', sa.String(200), nullable=False),
)
