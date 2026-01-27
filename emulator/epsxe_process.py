import pymem
import psutil

def get_epsxe_process():
  for p in psutil.process_iter(['pid', 'name']):
    if p.info['name'] == 'ePSXe.exe':
      pm = pymem.Pymem()
      pm.open_process_from_id(p.info['pid'])
      return pm
    
  raise Exception("ePSXe não encontrado.")