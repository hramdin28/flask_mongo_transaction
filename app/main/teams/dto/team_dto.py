from dataclasses import dataclass, field


@dataclass
class TeamDto:
    id: str
    name: str
    value: float
    players: list[str] = field(default_factory=list)
    current_tax_payed: float = field(default=0)
