import json 
from typing import Dict, List
from memory.enums.card_rarity import CardRarity

from memory.entities.card_entity import CardEntity

class CardRepository:
    def __init__(self, json_path: str):
        self._cards: List[CardEntity] = []
        self._cards_by_id: Dict[int, CardEntity] = {}

        self._load(json_path)

    def _load(self, json_path: str):
        with open(json_path, encoding="utf-8") as f:
            raw_cards = json.load(f)

        self._cards = [
            CardEntity(**card)
            for card in raw_cards
        ]

        self._cards_by_id = {
            card.id: card for card in self._cards
        }

    def get_all(self) -> List[CardEntity]:
        return self._cards
    
    def get_by_id(self, card_id: int) -> CardEntity | None:
        return self._cards_by_id.get(card_id)
    
    def get_by_rarity(self, rarity: CardRarity) -> list[CardEntity]:
        if not isinstance(rarity, CardRarity):
            raise ValueError("Raridade não encontrada, tente: secret_rare, ultra_rare, rare, common")
        
        return [card for card in self._cards if card.rarity == rarity.value]
    


    