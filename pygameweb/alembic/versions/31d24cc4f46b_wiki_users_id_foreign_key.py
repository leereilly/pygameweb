"""wiki users_id foreign key

Revision ID: 31d24cc4f46b
Revises: 8d334297f83a
Create Date: 2017-03-07 01:19:50.945932

"""

# revision identifiers, used by Alembic.
revision = '31d24cc4f46b'
down_revision = '8d334297f83a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('wiki_user_id_fkey', 'wiki', 'users', ['users_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('wiki_user_id_fkey', 'wiki', type_='foreignkey')
    # ### end Alembic commands ###
