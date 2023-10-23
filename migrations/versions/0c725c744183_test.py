"""test

Revision ID: 0c725c744183
Revises: 6b893f4e8b5a
Create Date: 2023-10-23 07:18:25.517448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0c725c744183'
down_revision: Union[str, None] = '6b893f4e8b5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('files', sa.Column('verbose_name', sa.String(), nullable=False))
    op.alter_column('files', 'user',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('files', 'nodes',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('files', 'nodes',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('files', 'user',
               existing_type=sa.UUID(),
               nullable=True)
    op.drop_column('files', 'verbose_name')
    # ### end Alembic commands ###
