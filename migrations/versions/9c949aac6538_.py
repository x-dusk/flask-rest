"""empty message

Revision ID: 9c949aac6538
Revises: f98081943ff3
Create Date: 2019-08-15 15:07:22.644449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c949aac6538'
down_revision = 'f98081943ff3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attr',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a', sa.Float(), nullable=True, comment='特征A'),
    sa.Column('b', sa.Float(), nullable=True, comment='特征B'),
    sa.Column('c', sa.Float(), nullable=True, comment='特征C'),
    sa.Column('d', sa.Float(), nullable=True, comment='特征D'),
    sa.Column('e', sa.Float(), nullable=True, comment='特征E'),
    sa.Column('y', sa.Float(), nullable=True, comment='目标Y'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attr')
    # ### end Alembic commands ###