from .starchips.starchips_achievement_factory import (
  ten_thousand_starchips_achievement,
  fifty_thousand_starchips_achievement,
  one_hundred_thousand_starchips_achievement,
  five_hundred_thousand_starchips_achievement
)

from .cards import (
  secret_rare_cards_achievement_factory,
  ultra_rare_cards_achievement_factory,
  rare_cards_achievement_factory,
)

ALL_ACHIEVEMENTS_FACTORIES = [
  ten_thousand_starchips_achievement,
  fifty_thousand_starchips_achievement,
  one_hundred_thousand_starchips_achievement,
  five_hundred_thousand_starchips_achievement,
  secret_rare_cards_achievement_factory,
  ultra_rare_cards_achievement_factory,
  rare_cards_achievement_factory
]