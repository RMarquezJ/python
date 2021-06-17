from products import Product
from stores import Store

te = Product('Caja de té 20 uds.', 1500, 'Abarrotes', 1)
galletas = Product('Galletas Chocolate 500g', 700, 'Abarrotes', 2)
jugo = Product('Néctar Naranja 1L', 800, 'Bebestibles', 3)
redbull = Product('RedBull 250ml', 1500, 'Bebestibles', 4)
jabon = Product('Jabón Liquido 1L', 1200, 'Higiene', 5)
shampoo = Product('Shampoo 500ml', 2000, 'Higiene', 6)

donluchito = Store('Don Luchito')

donluchito.add_product(te)

te.print_info().update_price(10,True).print_info()

donluchito.add_product(jugo).add_product(redbull).add_product(galletas).sell_product(2).inflation(20)

te.print_info()

