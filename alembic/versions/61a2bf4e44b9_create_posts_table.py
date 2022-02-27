"""create posts table

Revision ID: 61a2bf4e44b9
Revises: 
Create Date: 2022-02-14 14:00:15.093345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61a2bf4e44b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
