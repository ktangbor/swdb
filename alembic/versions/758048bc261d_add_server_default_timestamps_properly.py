"""add server default timestamps properly

Revision ID: 758048bc261d
Revises: 6781827e73ce
Create Date: 2025-09-11 17:07:45.699867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '758048bc261d'
down_revision: Union[str, Sequence[str], None] = '6781827e73ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('characters', 'created',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=False,
                    server_default=sa.text("now()"),
                    nullable=False)
    op.alter_column('characters', 'edited',
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=False,
                    server_default=sa.text("now()"),
                    nullable=False)
    op.alter_column('films', 'created',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=False,
               server_default=sa.text("now()"),
               nullable=False)
    op.alter_column('films', 'edited',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=False,
               server_default=sa.text("now()"),
               nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    pass
