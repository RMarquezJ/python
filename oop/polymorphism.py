class Vehicle:
  def __init__(self, brand, model, engine, performance):
    
    self.brand = brand
    self.model = model
    self.engine = engine
    self.performance = performance
  
  def consumption(self, kms):
    return kms / self.performance
  
class Schoolbus(Vehicle):
  def __init__(self, brand, model, engine, performance, seatnum, fee):
      super().__init__(brand, model, engine, performance)
      self.seatnum = seatnum
      self.fee = fee
      
  def feecalc(self, distance):
    return distance * self.fee

class Emergencyveh(Vehicle):
  def __init__(self, brand, model, engine, performance, equipment, beacon=True):
      super().__init__(brand, model, engine, performance)
      self.beacon = beacon
      self.equipment = equipment


yaris=Vehicle('Toyota', 'Yaris', 1600, 17)
moto=('Honda', 'CB500X', 500, 27)
furgon=Schoolbus('Hyundai', 'AX101', 2500, 10, 7, 7200)

class Contribuyente:
  def __init__(self, nombre, rut, oficio):
    self.nombre=nombre
    self.rut=rut
    self.oficio=oficio
    self.bienes=[]
  
  def add_bien(self, descr, precio, esMueble=False):
    self.bienes.append({
      'descr' : descr,
      'precio' : precio,
      'es Muele': esMueble
    })

  def pagarImpuestos(self,ganancia):
    raise NotImplementedError

class Independiente(Contribuyente):
  def __init__(self, nombre, rut, oficio):
      super().__init__(nombre, rut, oficio)
  
  def pagarImpuestos(self, ganancia):
      return ganancia * 0,115

class Asalariado(Contribuyente):
  def __init__(self, nombre, rut, oficio):
      super().__init__(nombre, rut, oficio)
  
  def pagarImpuestos(self, ganancia):
      return ganancia*0.27