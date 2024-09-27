"""add foreign-key to posts table

Revision ID: c52932d90679
Revises: 494613bc1e22
Create Date: 2024-09-26 16:06:41.285306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c52932d90679'
down_revision: Union[str, None] = '494613bc1e22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('post', sa.Column('owner_id' , sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('post', 'owner_id')
    pass
