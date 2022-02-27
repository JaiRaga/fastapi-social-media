"""add users table

Revision ID: f5a1e4d662fd
Revises: 88d5106ee208
Create Date: 2022-02-26 22:10:52.989825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5a1e4d662fd'
down_revision = '88d5106ee208'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),  
                    sa.Column('email', sa.String(), nullable=False), 
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
