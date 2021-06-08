# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
def big(arr):
  newbig = []
  for elem in range(0,len(arr),1):
    x=arr[elem]
    if x > 0:
      newbig.append("big")
    else:
      newbig.append(x)
  return newbig
print(big([1,-2,-3,4,1,2,-5,0]))

#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
def count_pos(arr2):
  newcount=arr2
  x=0
  for elem in range(0, len(arr2)-1, 1):
    if elem>0:
      x+=1
  newcount[len(newcount)-1]=x
  return newcount
print(count_pos([-1,-2,1,5,2]))

#Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
def sum_total(arr3):
  sum2=0
  for element in range(0,len(arr3), 1):
    x=arr3[element]
    sum2+=x
  return sum2
print(sum_total([3,4,-5,6]))

#Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
def avg(arr4):
  z=0
  for elements in range(0, len(arr4), 1):
    x=arr4[elements]
    z+=x
  return (z/len(arr4))
print(avg([5,7,2,3,4]))
  
#Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
def span(arr):
  return len(arr)
print(span([1,5,8,2,3]))

#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
def min(arr):
  if len(arr)==0:
    return False
  else:
    x=arr[0]
    for elements in range(0,len(arr), 1):
      if x>arr[elements]:
        x=arr[elements]
  return x
print(min([3,5,2,7,8]))

#Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
def max(arr):
  if len(arr)==0:
    return False
  else:
    x=arr[0]
    for elements in range(0,len(arr), 1):
      if x<arr[elements]:
        x=arr[elements]
  return x
print(max([3,5,2,7,8]))

#Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
def analisys(arr):
  sum=0
  min=arr[0]
  max=arr[0]
  for elements in range(0,len(arr),1):
    x=arr[elements]
    sum+=x
    if min>x:
      min=x
    elif max<x:
      max=x
  return {
    'Total' : sum,
    'Average' : (sum/len(arr)),
    'Minimum' : min,
    'Maximum' : max,
    'Lenght' : len(arr)
  }
print(analisys([1,2,3,4,5,6,7]))

#crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
def rev(arr):
  return list(reversed(arr))
print(rev([1,2,3,4,5]))
