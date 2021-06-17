import math

class Store:
  
  def __init__(self,name):
      self.name = name
      self.list = []
  
  def add_product(self, newproduct):
    self.list.append(newproduct)
    return self
  
  def sell_product(self, id):
    print('Se ha vendido 1 ' + str(self.list[id].name))
    self.list.pop(id)
    return self
  
  def inflation(self, percent):
    for elem in self.list:
      elem.price *= (1 + (percent/100))
    return self
  
  def set_clearance(self, category, percent):
    for elem in self.list:
      if elem.cat==category:
        elem.price *= (1+ (percent/100))
      else:
        continue
    return self