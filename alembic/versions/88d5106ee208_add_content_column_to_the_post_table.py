"""add content column to the post table

Revision ID: 88d5106ee208
Revises: 61a2bf4e44b9
Create Date: 2022-02-26 22:01:04.144251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88d5106ee208'
down_revision = '61a2bf4e44b9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
