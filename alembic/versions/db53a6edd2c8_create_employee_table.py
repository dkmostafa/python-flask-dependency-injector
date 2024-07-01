"""create employee table

Revision ID: db53a6edd2c8
Revises: 
Create Date: 2024-06-21 14:23:33.054977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db53a6edd2c8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'employee',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('username', sa.String(50), nullable=False , unique=True),
        sa.Column('email', sa.String(50), nullable=False , unique=True),
    )

    pass


def downgrade() -> None:
    pass
