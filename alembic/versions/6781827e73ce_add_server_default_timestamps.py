"""add server default timestamps

Revision ID: 6781827e73ce
Revises: 6c2888ec20a9
Create Date: 2025-09-11 16:57:02.881726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6781827e73ce'
down_revision: Union[str, Sequence[str], None] = '6c2888ec20a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
