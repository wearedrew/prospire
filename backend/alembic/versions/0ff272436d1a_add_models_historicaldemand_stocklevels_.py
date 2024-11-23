"""Add models: HistoricalDemand, StockLevels, PredictionParameters, PredictionResults

Revision ID: 0ff272436d1a
Revises: 6c761e5e3e1d
Create Date: 2024-11-22 22:16:22.955249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = '0ff272436d1a'
down_revision: Union[str, None] = '6c761e5e3e1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear tabla HistoricalDemand
    op.create_table(
        'historical_demand',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('item_id', UUID(as_uuid=True), sa.ForeignKey('items.id', ondelete='CASCADE'), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False)
    )

    # Crear tabla StockLevels
    op.create_table(
        'stock_levels',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('item_id', UUID(as_uuid=True), sa.ForeignKey('items.id', ondelete='CASCADE'), nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False)
    )

    # Crear tabla PredictionParameters
    op.create_table(
        'prediction_parameters',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('business_unit_id', UUID(as_uuid=True), sa.ForeignKey('business_units.id', ondelete='CASCADE'), nullable=False),
        sa.Column('parameter_name', sa.String, nullable=False),
        sa.Column('parameter_value', sa.Float, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False)
    )

    # Crear tabla PredictionResults
    op.create_table(
        'prediction_results',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('item_id', UUID(as_uuid=True), sa.ForeignKey('items.id', ondelete='CASCADE'), nullable=False),
        sa.Column('predicted_date', sa.Date, nullable=False),
        sa.Column('predicted_quantity', sa.Integer, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False)
    )


def downgrade() -> None:
    # Eliminar tablas en orden inverso
    op.drop_table('prediction_results')
    op.drop_table('prediction_parameters')
    op.drop_table('stock_levels')
    op.drop_table('historical_demand')