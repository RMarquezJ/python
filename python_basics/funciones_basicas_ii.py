#Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
def regCount(num):
  list = []
  for numbers in range(num,-1, -1):
    list.append(numbers)
  return(list)
print(regCount(10))

#Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
def print_and_return(a,b):
  print(a)
  return(b)
print_and_return(3,5)

#First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
def firstpluslenght(nums):
  firstval=nums[0]
  lengthval=len(nums)
  return(firstval+lengthval)
print (firstpluslenght([1,2,3,4,5]))

#Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False.
def greatsec(list1):
  list2=[]
  if len(list1)<2:
    return False
  else:
    for element in range(0,len(list1),1):
      x=list1[element]
      if x>list1[1]:
        list2.append(x)
      else:
        continue
    print(len(list2))
    return list2 
print(greatsec([1,2,3,4,3,2,1]))
print(greatsec([1]))

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.

def lengthval(span,value):
  list3=[]
  for elem in range(0,span,1):
    list3.append(value)
  return list3
print(lengthval(3,5))