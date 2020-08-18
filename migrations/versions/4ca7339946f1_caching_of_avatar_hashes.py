"""caching of avatar hashes

Revision ID: 4ca7339946f1
Revises: f39b4b14b8aa
Create Date: 2020-08-18 16:23:38.640240

"""

# revision identifiers, used by Alembic.
revision = '4ca7339946f1'
down_revision = 'f39b4b14b8aa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
