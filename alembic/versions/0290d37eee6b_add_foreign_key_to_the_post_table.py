"""add foreign-key to the post table

Revision ID: 0290d37eee6b
Revises: f5a1e4d662fd
Create Date: 2022-02-26 22:21:42.455123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0290d37eee6b'
down_revision = 'f5a1e4d662fd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
