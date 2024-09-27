"""create post table

Revision ID: 3b6a1c2d612f
Revises: 80e24d8cd2ba
Create Date: 2024-09-26 11:50:00.056618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b6a1c2d612f'
down_revision: Union[str, None] = '80e24d8cd2ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
