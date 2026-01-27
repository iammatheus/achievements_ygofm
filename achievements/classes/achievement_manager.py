import json
import os

class AchievementManager:
    def __init__(self, achievements, notifications, save_file="memory/achievements.json"):
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

    def check(self, key, value):
        ach = self.achievements.get(key)
        if not ach:
            return

        result = ach.check(value)
        if not result:
            return

        for fn in self.notifications.get(key, {}).get("on_progress", []):
            fn(ach, result["result"])

        if result["unlocked"]:
            for fn in self.notifications.get(key, {}).get("on_unlock", []):
                fn(ach)

        self.save()