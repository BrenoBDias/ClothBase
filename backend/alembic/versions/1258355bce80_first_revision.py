"""First Revision

Revision ID: 1258355bce80
Revises: 
Create Date: 2025-02-23 20:24:23.568066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1258355bce80'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('log', sa.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_log_id'), 'log', ['id'], unique=False)
    op.create_table('usertype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usertype_id'), 'usertype', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=50), nullable=False),
    sa.Column('cpf', sa.VARCHAR(length=50), nullable=True),
    sa.Column('cnpj', sa.VARCHAR(length=50), nullable=True),
    sa.Column('user_type', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_type'], ['usertype.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_usertype_id'), table_name='usertype')
    op.drop_table('usertype')
    op.drop_index(op.f('ix_log_id'), table_name='log')
    op.drop_table('log')
    # ### end Alembic commands ###
