"""Initial migration with companies, business_units, users, and user_business_unit_roles

Revision ID: 6c761e5e3e1d
Revises: 79de49ecce74
Create Date: 2024-11-22 21:01:11.820179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '6c761e5e3e1d'
down_revision: Union[str, None] = '79de49ecce74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear tabla `users`
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=sa.text('uuid_generate_v4()')),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.text('NOW()'), onupdate=sa.text('NOW()'), nullable=False)
    )

    # Crear tabla `companies`
    op.create_table(
        'companies',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=sa.text('uuid_generate_v4()')),
        sa.Column('name', sa.String, nullable=False)
    )

    # Crear tabla `business_units`
    op.create_table(
        'business_units',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=sa.text('uuid_generate_v4()')),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('company_id', UUID(as_uuid=True), sa.ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)
    )

    # Crear tabla `user_business_unit_roles`
    op.create_table(
        'user_business_unit_roles',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=sa.text('uuid_generate_v4()')),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('business_unit_id', UUID(as_uuid=True), sa.ForeignKey('business_units.id', ondelete='CASCADE'), nullable=False),
        sa.Column('role', sa.Enum('ADMIN', 'EDITOR', 'VIEWER', 'BILLING', 'DEMAND_MANAGER', name='roleenum'), nullable=False)
    )


def downgrade() -> None:
    # Eliminar tabla `user_business_unit_roles`
    op.drop_table('user_business_unit_roles')

    # Eliminar tabla `business_units`
    op.drop_table('business_units')

    # Eliminar tabla `companies`
    op.drop_table('companies')

    # Eliminar tabla `users`
    op.drop_table('users')