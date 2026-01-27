from emulator.epsxe_process import get_epsxe_process

class BaseMemoryReader:
  def __init__(self):
    self.pm = get_epsxe_process()

  def _read_int(self, address: int) -> int:
    return self.pm.read_int(address)

