from enums.achievements_id import AchievementsIdEnum

class AchievementBase:
    def __init__(self, id: str, key: AchievementsIdEnum, title: str, condition: function, msg: str = '', total: int = 0):
        self.id = id
        self.key = key
        self.title = title
        self.msg = msg
        self.total = total
        self.condition = condition
        self.progress = set()
        self.unlocked = False

    def to_dict(self):
        data = {"unlocked": self.unlocked}

        if self.progress:
            data["progress"] = list(self.progress)

        return data

    def load_from_dict(self, data):
        self.unlocked = data.get("unlocked", False)
        self.progress = set(data.get("progress", []))

    def check(self, value):
        if self.unlocked:
            return None

        result = self.condition(value)

        if not result or result in self.progress:
            return None

        # achievement SEM progresso
        if not self.total:
            self.unlocked = True
            return {
                "result": None,
                "unlocked": True
            }

        # achievement COM progresso
        self.progress.add(result)
        unlocked_now = False
        
        if len(self.progress) >= self.total:
            self.unlocked = True
            unlocked_now = True

        return {
            "result": result,
            "unlocked": unlocked_now
        }