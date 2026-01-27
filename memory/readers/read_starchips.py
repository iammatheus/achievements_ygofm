from memory.readers.base_reader import BaseMemoryReader
from const.addresses import STARSHIP_ADDRESS


class StarchipsReader(BaseMemoryReader):
  def read(self) -> int:
    return self._read_int(STARSHIP_ADDRESS)