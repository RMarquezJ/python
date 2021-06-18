import math

class Product:

  def __init__(self, name, price, category, id):
    self.name = name
    self.price = price
    self.cat = category
    self.id = id

  def update_price(self, percent, increase):
    try:
      percent=int(percent)

    except ValueError:
      return None

    if increase == True:
      self.price *= (1+percent/100)
    
    elif increase == False:
      self.price *= (1-percent/100)
    
    else:
      print('Input True for increment or False for decrement' )
    
    return self
  
  def print_info(self):
    print(f'Producto: {self.name} \nCategoría: {self.cat} \nPrecio: {int(self.price)}')
    return self

  def __repr__(self):
    return repr(f'Producto {self.name}, de id: {self.id}')