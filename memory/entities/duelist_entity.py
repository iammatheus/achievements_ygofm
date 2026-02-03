from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class DuelistEntity:
  id: int
  name: str
  hex_address: str