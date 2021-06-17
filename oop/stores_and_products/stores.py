class Store:

  def __init__(self, name):

      self.name = name
      self.productList = []
      
  def add_product(self, new_product):

    self.productList.append(new_product)
  
  def sell_product(self, id):   
    self.productList.pop(id)
    print('Se vendió: ' + str(self.productList[id]))

  def inflation(self, percent_increase):
    for element in self.productList:
      element.price *= (1 + (percent_increase/100))


  # def set_clearence(self, cat, percent_discount):
  #   for element.cat in self.productList:
  #         element.price *= (1-(percent_discount/100))