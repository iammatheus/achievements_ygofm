from achievements.classes.achievement_base import AchievementBase
from enums.achievements_id import AchievementsIdEnum
from memory.repositories.card_repository import CardRepository
from memory.entities.card_entity import CardEntity
from memory.enums.card_rarity import CardRarity
from paths import ALL_CARDS_PATH
from typing import List

cardRepository = CardRepository(ALL_CARDS_PATH)
cards_ultra_rare_list: List[CardEntity] = cardRepository.get_by_rarity(CardRarity.ULTRA_RARE)
ultra_rare_ids = {card.id for card in cards_ultra_rare_list}


def ultra_rare_cards_achievement_factory():
  return AchievementBase(
    id=AchievementsIdEnum.ULTRA_RARE,
    key=AchievementsIdEnum.ULTRA_RARE,
    title="Obtenha Todas as Ultra Raras!\n",
    total=len(cards_ultra_rare_list),
    condition=lambda card_id: card_id if card_id in ultra_rare_ids else None
  )