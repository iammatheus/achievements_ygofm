import json
import os
from enums.achievements_id import AchievementsIdEnum
from .achievement_base import AchievementBase

class AchievementManager:
    def __init__(self, achievements, notifications, save_file="memory/data/achievements.json"):
        self.achievements = {a.key: a for a in achievements}
        self.notifications = notifications
        self.save_file = save_file
        self.load()

    def load(self):
        if not os.path.exists(self.save_file):
            return

        with open(self.save_file, "r") as f:
            data = json.load(f)

        for key, ach_data in data.items():
            if key in self.achievements:
                self.achievements[key].load_from_dict(ach_data)

    def save(self):
        with open(self.save_file, "w") as f:
            json.dump(
                {k: a.to_dict() for k, a in self.achievements.items()},
                f,
                indent=2
            )
    
    def __run_notifications(self, key: AchievementsIdEnum, event: str, achievement: AchievementBase, extra=None):
        config = self.notifications.get(key, {})

        callbacks: function = (
            config.get("on_all", []) +
            config.get(event, [])
        )

        for fn in callbacks:
            fn(achievement, extra)

    def check(self, key: AchievementsIdEnum, value: int):
        ach = self.achievements.get(key)

        if not ach:
            return

        result = ach.check(value)

        if not result:
            return

        # desbloqueio
        if result["unlocked"]:
            self.__run_notifications(
                key,
                "on_unlock",
                ach,
            )

        # progresso
        self.__run_notifications(
            key,
            "on_progress",
            ach,
            result["result"]
        )

        self.save()