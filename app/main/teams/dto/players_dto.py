from dataclasses import dataclass


@dataclass
class PlayersDto:
    id: str
    name: str
    age: int
    salary: float
