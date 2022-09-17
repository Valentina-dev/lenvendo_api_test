from dataclasses import dataclass


@dataclass
class Product:
    name: str
    image: str
    price: int
