import json
from typing import List, Dict
from memory.entities.duelist_entity import DuelistEntity

class DuelistRepository: 
  def __init__(self, json_path: str):
    self._duelists: List[DuelistEntity] = []
    self._duelist_by_id: Dict[int, DuelistEntity] = {}
    
    self._load(json_path)

  def _load(self, json_path: str):
    with open(json_path, encoding="utf-8") as duelists:
      raw_duelists = json.load(duelists)

    self._duelists = [
      DuelistEntity(**duelist)
      for duelist in raw_duelists
    ] 

    self._duelist_by_id = {
      duelist.id: duelist for duelist in self._duelists
    }

  def get_all(self) -> List[DuelistEntity]:
    return self._duelists
  
  def get_by_id(self, duelist_id: int) -> DuelistEntity | None:
    return self._duelist_by_id.get(duelist_id)
  
   