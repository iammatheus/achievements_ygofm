from achievements.classes.achievement_base import AchievementBase
from enums.achievements_id import AchievementsIdEnum
from enums.starchips_tier import StarchipsTierEnum
import uuid

def starchips_achievement_factory(key: str, title: str, msg: str, condition: function):
  return AchievementBase(
    id=uuid.uuid4(), 
    key=key,
    title=title,
    condition=condition,
    msg=msg
  )

def ten_thousand_starchips_achievement():
  return starchips_achievement_factory(
    AchievementsIdEnum.TEN_THOUSAND_STARCHIPS,
    'Duelista Ambicioso!', 
    'Obtenha 10.000,00 Starchips.', 
    lambda star: star >= StarchipsTierEnum.TEN_THOUSAND
  )

def fifty_thousand_starchips_achievement():
  return starchips_achievement_factory(
    AchievementsIdEnum.FIFTY_THOUSAND_STARCHIPS,
    'Duelista de Elite!', 
    'Obtenha 50.000,00 Starchips.', 
    lambda star: star >= StarchipsTierEnum.FIFTY_THOUSAND
  )

def one_hundred_thousand_starchips_achievement():
  return starchips_achievement_factory(
    AchievementsIdEnum.ONE_HUNDRED_THOUSAND_STARCHIPS,
    'Mestre das Starchips!', 
    'Obtenha 100.000,00 Starchips.', 
    lambda star: star >= StarchipsTierEnum.ONE_HUNDRED_THOUSAND
  )

def five_hundred_thousand_starchips_achievement():
  return starchips_achievement_factory(
    AchievementsIdEnum.FIVE_HUNDRED_THOUSAND_STARCHIPS,
    'Lenda do Coliseu!', 
    'Obtenha 500.000,00 Starchips.', 
    lambda star: star >= StarchipsTierEnum.FIVE_HUNDRED_THOUSAND
  )