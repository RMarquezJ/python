import unittest
from products import Product

def prod():
  pass

class ProdTest(unittest.TestCase):

  def setUp(self):
    print('Comenzando prueba de productos')

  def testNum(self):
    pass

  def tearDown(self) -> None:
    print('Terminando prueba de productos')
    

if __name__=='__main__':
  unittest.main()