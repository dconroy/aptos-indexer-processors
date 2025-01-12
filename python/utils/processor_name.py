from enum import Enum


class ProcessorName(Enum):
    EXAMPLE_EVENT_PROCESSOR = "python_example_event_processor"
    EXAMPLE_AMBASSADOR_TOKEN_PROCESSOR = "example_ambassador_token_processor"
    NFT_MARKETPLACE_V1_PROCESSOR = "nft_marketplace_v1_processor"
    NFT_MARKETPLACE_V2_PROCESSOR = "nft_marketplace_v2_processor"
    COIN_FLIP = "coin_flip"
    DELEGATION_POOL = "delegation_pool"
