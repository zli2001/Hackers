"""empty message

Revision ID: 2b89a4afd0d0
Revises: 87ca08b34a71
Create Date: 2018-09-23 16:29:48.922607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b89a4afd0d0'
down_revision = '87ca08b34a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('album', sa.Column('power', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('album', 'power')
    # ### end Alembic commands ###