"""create items

Revision ID: 9fc2bb0d905c
Revises: a2ec7eb2c1c8
Create Date: 2021-07-10 15:41:27.495473

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '9fc2bb0d905c'
down_revision = 'a2ec7eb2c1c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp'), nullable=False),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp on update current_timestamp'), nullable=False),
    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###
