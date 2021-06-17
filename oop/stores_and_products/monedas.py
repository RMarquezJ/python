import unittest

def sencillar(num):
  try:
    num = int(num)

  except ValueError:
    return None

  monedas500=num//500
  num = num % 500

  monedas100=num//100
  num = num % 100

  monedas50=num//50
  num = num % 50

  monedas10 = num//10

  retorno = {}

  if monedas10>0:
    retorno['10'] = monedas10
  
  elif monedas50>0:
    retorno['50'] = monedas50

  elif monedas100>0:
    retorno['100'] = monedas100

  elif monedas500>0:
    retorno['500'] = monedas500
  
  return retorno

class Sencillartests(unittest.TestCase):

  def setUp(self):
    print('Comenzando las pruebas')
  
  def testTreinta(self):
    resultado = sencillar(30)
    esperado={
      '10' : 3
    }
    self.assertEqual(resultado,esperado)

  def testMonedas(self):
    resultado = sencillar(990)
    esperado = {
      '10': 4,
      '50': 1,
      '100': 4,
      '500':1,
      'luca':0
    }
    self.assertEqual(resultado,esperado)

  def testNoStrings(self):
    resultado=sencillar('mucha plata')
    self.assertIsNone(resultado)
  
  def tearDown(self):
    print('Terminando pruebas')

if __name__== '__main__':
  unittest.main()