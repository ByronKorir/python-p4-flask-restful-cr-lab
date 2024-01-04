"""empty message

Revision ID: 0e950d7fdcc5
Revises: f5d596740ce5
Create Date: 2024-01-04 17:20:26.418281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e950d7fdcc5'
down_revision = 'f5d596740ce5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('preice', sa.Float(), nullable=True))
        batch_op.drop_column('pice')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pice', sa.FLOAT(), nullable=True))
        batch_op.drop_column('preice')

    # ### end Alembic commands ###
