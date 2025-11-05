"""Increase password column length to 255

Revision ID: c1a2b3d4e5f6
Revises: b9cc89547c62
Create Date: 2025-11-05 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1a2b3d4e5f6'
down_revision = 'b9cc89547c62'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch_alter_table for SQLite compatibility
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
                              existing_type=sa.String(length=100),
                              type_=sa.String(length=255),
                              existing_nullable=False)


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
                              existing_type=sa.String(length=255),
                              type_=sa.String(length=100),
                              existing_nullable=False)
