"""more topology data

Revision ID: 1a5eb7069f9a
Revises: 49e7c02579db
Create Date: 2024-09-03 16:24:25.791272

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "1a5eb7069f9a"
down_revision = "49e7c02579db"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("topologyservice", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("ip_address", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
        )
        batch_op.add_column(
            sa.Column("mac_address", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
        )
        batch_op.add_column(
            sa.Column("category", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
        )
        batch_op.add_column(
            sa.Column("manufacturer", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("topologyservice", schema=None) as batch_op:
        batch_op.drop_column("manufacturer")
        batch_op.drop_column("category")
        batch_op.drop_column("mac_address")
        batch_op.drop_column("ip_address")
    # ### end Alembic commands ###