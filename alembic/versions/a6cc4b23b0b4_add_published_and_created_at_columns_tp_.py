"""add published and created_at columns tp post table

Revision ID: a6cc4b23b0b4
Revises: 0290d37eee6b
Create Date: 2022-02-26 22:34:54.920454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6cc4b23b0b4'
down_revision = '0290d37eee6b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', 
            sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', 
            sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
