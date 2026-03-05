import time

from ui.notifications_registry import NOTIFICATIONS
from achievements.factories import ALL_ACHIEVEMENTS_FACTORIES
from enums.achievements_id import AchievementsIdEnum

from achievements.classes.achievement_manager import AchievementManager
from memory.readers import (
    StarchipsReader,
    CardReader
)

# deletar arquivo de achievements local
# if os.path.exists('memory/achievements.json'):
#     os.remove('memory/achievements.json')

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

    # STARCHIPS -> todo: separar em um arquivo futuramente
    manager.check(AchievementsIdEnum.TEN_THOUSAND_STARCHIPS, star)
    manager.check(AchievementsIdEnum.FIFTY_THOUSAND_STARCHIPS, star)
    manager.check(AchievementsIdEnum.ONE_HUNDRED_THOUSAND_STARCHIPS, star)
    manager.check(AchievementsIdEnum.FIVE_HUNDRED_THOUSAND_STARCHIPS, star)

    # CARDS -> todo: separar em um arquivo futuramente
    manager.check(AchievementsIdEnum.SECRET_RARE, card)
    manager.check(AchievementsIdEnum.ULTRA_RARE, card)
    manager.check(AchievementsIdEnum.RARE, card)

    time.sleep(1)
