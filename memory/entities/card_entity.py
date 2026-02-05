from dataclasses import dataclass
from typing import Optional
from memory.enums import (
  CardType,
  CardRarity,
  MonsterType
)

@dataclass(frozen=True, slots=True)
class CardEntity: 
  id: int
  name: str
  level: int
  cardType: CardType
  rarity: CardRarity
  isSingleDrop: bool # Se a carta dropa somente em um duelista.

  image: Optional[str] = None
  type: Optional[MonsterType] = None
  ATK: Optional[int] = None
  DFD: Optional[int] = None