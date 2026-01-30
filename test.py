# Arquivo para testes de funções de modo geral

from memory.repositories.card_repository import CardRepository
from memory.entities.card_entity import CardEntity
from memory.enums.card_rarity import CardRarity
from paths import ALL_CARDS_PATH

cardRepository = CardRepository(ALL_CARDS_PATH)

cards = cardRepository.get_all()
secret_rare: CardEntity = cardRepository.get_by_rarity(CardRarity.SECRET_RARE)

print(len(secret_rare))