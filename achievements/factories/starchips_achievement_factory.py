from achievements.classes.achievement_base import AchievementBase

def starchips_achievement_factory():
  return AchievementBase(
    id="starchips", 
    key="star",
    title="Rico!",
    total=0,
    condition=lambda star: star >= 10
  )