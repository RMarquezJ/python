from stores import Store

from products import Product

pan = Product('pan blanco', 1000, 'abarrotes',1)
te = Product('caja de te', 1000, 'abarrotes',2)
galletas = Product('paquete de galletas', 500, 'snacks',3)
jugo = Product('jugo 1L', 800, 'bebidas',4)
cerveza = Product('sixpack cerveza', 3500, 'bebidas',5)
jabon = Product('jabon 750ml', 1000, 'higiene',6)

donluchito = Store('Don Luchito')

donluchito.add_product(te)

te.update_price(30,True)

te.print_info()

donluchito.add_product(jugo)
donluchito.add_product(pan)
donluchito.sell_product(1)

donluchito.inflation(20)

te.print_info()

te.print_info()
