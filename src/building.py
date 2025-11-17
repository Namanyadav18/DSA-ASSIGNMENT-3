from dataclasses import dataclass

@dataclass
class Building:
    id: int
    name: str
    location: str

    def __repr__(self) -> str:
        return f"Building(id={self.id}, name='{self.name}', location='{self.location}')"
