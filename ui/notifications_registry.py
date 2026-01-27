from ui import (
    show_achievement,
    show_rare_card_progress,
)

NOTIFICATIONS = {
    "star": {
        "on_unlock": [show_achievement],
        "on_progress": []
    },
    "rare": {
        "on_unlock": [show_achievement],
        "on_progress": [show_rare_card_progress]
    }
}