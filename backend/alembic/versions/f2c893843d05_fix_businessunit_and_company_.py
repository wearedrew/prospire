"""Fix BusinessUnit and Company relationship

Revision ID: f2c893843d05
Revises: 0ff272436d1a
Create Date: 2024-11-22 22:50:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f2c893843d05'
down_revision = '0ff272436d1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Crear tablas nuevamente
    op.create_table(
        'business_units',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('company_id', sa.UUID(as_uuid=True), sa.ForeignKey('companies.id', ondelete='CASCADE'))
    )

    op.create_table(
        'user_business_unit_roles',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', sa.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE')),
        sa.Column('business_unit_id', sa.UUID(as_uuid=True), sa.ForeignKey('business_units.id', ondelete='CASCADE')),
        sa.Column('role', sa.String(length=255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('user_business_unit_roles')
    op.drop_table('business_units')