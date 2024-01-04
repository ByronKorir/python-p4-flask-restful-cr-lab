"""empty message

Revision ID: 23f80afc5bb3
Revises: 0e950d7fdcc5
Create Date: 2024-01-04 17:21:27.656605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23f80afc5bb3'
down_revision = '0e950d7fdcc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))
        batch_op.drop_column('preice')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('preice', sa.FLOAT(), nullable=True))
        batch_op.drop_column('price')

    # ### end Alembic commands ###
