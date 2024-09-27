"""create post table

Revision ID: c28468573c91
Revises: b2461c817cd4
Create Date: 2024-09-26 11:45:29.423272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c28468573c91'
down_revision: Union[str, None] = 'b2461c817cd4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
