class AchievementBase:
    def __init__(self, id: str, key: str, title: str, total: int, condition):
        self.id = id
        self.key = key
        self.title = title
        self.total = total
        self.condition = condition
        self.progress = set()
        self.unlocked = False

    def to_dict(self):
        return {
            "unlocked": self.unlocked,
            "progress": list(self.progress)
        }

    def load_from_dict(self, data):
        self.unlocked = data.get("unlocked", False)
        self.progress = set(data.get("progress", []))

    def check(self, value):
        """
        Retorna:
        - None → nada aconteceu
        - dict → progresso ou desbloqueio
        """
        if self.unlocked:
            return None

        result = self.condition(value)

        if not result or result in self.progress:
            return None

        self.progress.add(result)

        unlocked_now = False
        if len(self.progress) >= self.total:
            self.unlocked = True
            unlocked_now = True

        return {
            "result": result,
            "unlocked": unlocked_now
        }