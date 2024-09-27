"""create post table

Revision ID: b2461c817cd4
Revises: cb871da761d5
Create Date: 2024-09-26 11:44:58.462415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2461c817cd4'
down_revision: Union[str, None] = 'cb871da761d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
