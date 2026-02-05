from achievements.classes.achievement_base import AchievementBase
from enums.achievements_id import AchievementsIdEnum
from memory.repositories.card_repository import CardRepository
from memory.entities.card_entity import CardEntity
from memory.enums.card_rarity import CardRarity
from paths import ALL_CARDS_PATH
from typing import List

cardRepository = CardRepository(ALL_CARDS_PATH) # todo, adaptar função para pegar dessa lista e colocar ali no lambda
cards_secret_rare_list: List[CardEntity] = cardRepository.get_by_rarity(CardRarity.SECRET_RARE)
secret_rare_ids = {card.id for card in cards_secret_rare_list}


def secret_rare_cards_achievement_factory():
    return AchievementBase(
        id=AchievementsIdEnum.SECRET_RARE,
        key=AchievementsIdEnum.SECRET_RARE,
        title="OBTENHA TODAS AS 82 RARAS!\n",
        total=len(cards_secret_rare_list),
        condition=lambda card_id: card_id if card_id in secret_rare_ids else None
    )