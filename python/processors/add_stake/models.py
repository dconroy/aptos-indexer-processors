from utils.models.annotated_types import StringType
from utils.models.annotated_types import (
    BooleanType,
    StringPrimaryKeyType,
    BigIntegerType,
    BigIntegerPrimaryKeyType,
    InsertedAtType,
    TimestampType,
    StringType,
    NumericType
)
from utils.models.general_models import Base
from utils.models.schema_names import ADD_STAKE_SCHEMA_NAME


class AddStakeEvent(Base):
    __tablename__ = "add_stake_events"
    __table_args__ = ({"schema": ADD_STAKE_SCHEMA_NAME},)

    sequence_number: BigIntegerPrimaryKeyType
    creation_number: BigIntegerPrimaryKeyType
    pool_address: StringType
    delegator_address: StringType
    amount_added: BigIntegerType
    add_stake_fee: BigIntegerType
    transaction_version: BigIntegerType
    transaction_timestamp: TimestampType
    inserted_at: InsertedAtType
    event_index: BigIntegerType
