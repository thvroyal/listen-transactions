from dataclasses import dataclass
from ..utils.helpers import timestamp_to_datetime


@dataclass
class Transaction:
    id: str
    blockNumber: int
    blockHash: str
    timestamp: int
    type: str
    amountToken: float
    amountETH: float
    amountRef: float
    price: float
    priceETH: float
    maker: str

    def __post_init__(self, transaction_dict):
        for key, value in transaction_dict.items():
            setattr(self, key, value)
        self.date_time = timestamp_to_datetime(self.timestamp)
    
    def __str__(self):
        return f'{self.date_time} {self.id} {self.type} {self.amountToken} {self.amountETH} {self.amountRef} {self.price} {self.priceETH} {self.maker}'