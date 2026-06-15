from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    is_available: bool = True
