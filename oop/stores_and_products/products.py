class Product:

  def __init__(self, name, price, category, id):

    self.name = name
    self.price = price
    self.cat = category
    self.id = id

  def update_price(self, percent_change, is_increased):
    
    if is_increased == True:
      self.price *= (1+(percent_change/100))
    
    elif is_increased == False:
      self.price *= (1-(percent_change/100))
    
    else:
      print("Type 'True' for increase or 'False' for decrease")
  
  def print_info(self):
    print(f'Producto: {self.name} \nCategoría: {self.cat} \nPrecio: {self.price}')

  def __repr__(self) -> str:
      return f'{self.name}, de id: {self.id}'
