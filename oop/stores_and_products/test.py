import unittest
from products import Product

te = Product('caja de té', 1000, 'abarrotes', 1)

class Prodtest(unittest.TestCase):

  def setUp(self):
    print('Comenzando prueba de productos')

  def testNoStrings(self):
    inp = te.update_price('r', True)
    outp = None
    self.assertEqual(inp,outp)

  def tearDown(self) -> None:
    print('Terminando prueba de productos')
    

if __name__=='__main__':
  unittest.main()