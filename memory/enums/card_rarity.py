from enum import Enum

class CardRarity(Enum):
  SECRET_RARE = "secret_rare" # Todas as 82 raras.
  ULTRA_RARE = "ultra_rare" # Drops baixos, exemplo Metalzoa (4 de prob).
  RARE = "rare" # Drops como Blue-eyes White Dragon, Red-eyes, Dark Magician...
  COMMON = "common" # Cartas como Skull Servant, mais fáceis de obter.
