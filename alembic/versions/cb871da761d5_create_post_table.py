"""create post table

Revision ID: cb871da761d5
Revises: bd52b9a1624e
Create Date: 2024-09-26 11:28:04.151656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb871da761d5'
down_revision: Union[str, None] = 'bd52b9a1624e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
