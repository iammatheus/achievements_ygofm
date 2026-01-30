from achievements.classes.achievement_base import AchievementBase
from const.rare_cards import RARE_CARDS
from enums.achievements_id import AchievementsIdEnum

def secret_rare_cards_achievement_factory():
    return AchievementBase(
        id=AchievementsIdEnum.SECRET_RARE,
        key=AchievementsIdEnum.SECRET_RARE,
        title="🃏 Colecionador Das 82 Impossíveis 🃏",
        total=len(RARE_CARDS),
        condition=lambda card_id: card_id if card_id in RARE_CARDS else None,
    )