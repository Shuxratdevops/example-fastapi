"""create post table

Revision ID: 80e24d8cd2ba
Revises: c28468573c91
Create Date: 2024-09-26 11:48:25.497725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80e24d8cd2ba'
down_revision: Union[str, None] = 'c28468573c91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
