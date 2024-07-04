class Beneficiary:
  def __init__(self, name, hability, level) -> None:
    self.name = name
    self.hability = hability
    self.level = level
  def setName(self, name):
    self.name = name

  def setHability(self, hability):
    self.hability = hability

  def setLevel(self, level):
    self.level = level

  def getName(self):
    return self.name

  def getHability(self):
    return self.hability

  def getLevel(self):
    return self.level