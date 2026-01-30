from enums.achievements_id import AchievementsIdEnum

from ui import (
    show_starchips_achievement,
    show_secret_rare_card_progress_achievement,
)

NOTIFICATIONS = {
    AchievementsIdEnum.TEN_THOUSAND_STARCHIPS: {
        "on_unlock": [show_starchips_achievement],
    },
    AchievementsIdEnum.FIFTY_THOUSAND_STARCHIPS: {
        "on_unlock": [show_starchips_achievement],
    },
    AchievementsIdEnum.ONE_HUNDRED_THOUSAND_STARCHIPS: {
        "on_unlock": [show_starchips_achievement],
    },
    AchievementsIdEnum.FIVE_HUNDRED_THOUSAND_STARCHIPS: {
        "on_unlock": [show_starchips_achievement],
    },
    AchievementsIdEnum.SECRET_RARE: {
        "on_all": [show_secret_rare_card_progress_achievement]
    }
}