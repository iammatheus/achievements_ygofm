from achievements.classes.achievement_base import AchievementBase
from const.rare_cards import RARE_CARDS

def rare_cards_achievement_factory():
    return AchievementBase(
        id="rare_cards",
        key="rare",
        title="Colecionador de Cartas Raras",
        total=len(RARE_CARDS),
        condition=lambda card_id: card_id if card_id in RARE_CARDS else None
    )