import time

from ui.notifications_registry import NOTIFICATIONS
from achievements.factories import ALL_ACHIEVEMENTS_FACTORIES

from achievements.classes.achievement_manager import AchievementManager
from memory.readers import (
    StarchipsReader,
    CardReader
)

manager = AchievementManager(
    achievements=[fn() for fn in ALL_ACHIEVEMENTS_FACTORIES],
    notifications=NOTIFICATIONS,
)

starchips_reader = StarchipsReader()
card_reader = CardReader()

print("🎮 Monitorando Yu-Gi-Oh...")

while True:
    star = starchips_reader.read()
    card = card_reader.read()

    manager.check("star", star)
    manager.check("rare", card)

    time.sleep(1)
