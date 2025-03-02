from dataclasses import dataclass 

@dataclass
class Item:
    id: int
    name: str
    description: str
    price: float

