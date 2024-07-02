#moulo1.py
class Nodo:
  
  def __init__(self, value ) -> None:
      self.value = value
      self.next =  None
  def __str__(self) -> str:
     return str(self.value)
 