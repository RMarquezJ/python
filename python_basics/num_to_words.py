import math

def n2w(num):
  first15=['cero','uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince']
  decenas=['dieci','veinte','veinti','treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
  centenas=['cien','cientos', 'quinientos','sete','nove']
  dec = math.floor(num/10)
  uni = num - (dec*10)
  cent = math.floor(num/100)

  if num<=15:
    return first15[num]
  
  elif num<=19:
    return decenas[0]+ n2w(num-10)
  
  elif num==20:
    return decenas[1]
  
  elif num<=29:
    return decenas[2] + n2w(num-20)

  elif num<100:
    if uni==0:
      return decenas[dec]
    else:
      return decenas[dec] + ' y ' + n2w(uni)

  elif num<1000:
    if uni==0:
      return centenas[cent]

  else:
    return 'No implementado'

print(n2w(45))