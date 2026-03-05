from achievements.classes.achievement_base import AchievementBase
from .show_card_progress_achievement_base import show_card_progress_achievement_base

def show_secret_rare_card_progress_achievement(achievement: AchievementBase, card_id: int):
    show_card_progress_achievement_base(achievement, card_id, "Você Obteve Todas as 82 Raras!")