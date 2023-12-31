"""create priority table

Revision ID: f419632cbba6
Revises: d299e6bb8017
Create Date: 2023-10-09 13:49:01.302618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f419632cbba6'
down_revision = 'd299e6bb8017'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('priority',
    sa.Column('priority_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('priority_id')
    )
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('priority_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_priority', 'priority', ['priority_id'], ['priority_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_constraint('fk_priority', type_='foreignkey')
        batch_op.drop_column('priority_id')

    op.drop_table('priority')
    # ### end Alembic commands ###
