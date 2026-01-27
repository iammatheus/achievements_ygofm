from memory.readers.base_reader import BaseMemoryReader
from const.addresses import CARD_ADDRESS


class CardReader(BaseMemoryReader):
  def read(self) -> int:
    return self._read_int(CARD_ADDRESS)