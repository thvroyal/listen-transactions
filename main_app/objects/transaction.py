from dataclasses import dataclass
from ..utils.helpers import timestamp_to_datetime


@dataclass
class Transaction:
    id: str = None
    blockNumber: int = None
    blockHash: str = None
    timestamp: int = None
    type: str = None
    amountToken: float = None
    amountETH: float = None
    amountRef: float = None
    price: float = None
    priceETH: float = None
    maker: str = None
    date_time: str = None

    def load_from_dict(self, transaction_dict):
        for key, value in transaction_dict.items():
            setattr(self, key, value)
        self.date_time = timestamp_to_datetime(self.timestamp)
    
    def __str__(self) -> str:
        return f"Transaction: {self.id} - {self.date_time} - {self.amountToken} - {self.amountETH} - {self.amountRef} - {self.price} - {self.priceETH} - {self.maker}"