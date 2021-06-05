#1 Basico - imprime todos los enteros del 1 al 150:
for x in range(1,151):
  print(x)

#2 últiplos de 5 - imprime todos los multiplos de 5 en 5 hasta 1000:
for y in range(5,1001,5):
  print(y)

#3 Contar, Dojo way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for z in range(1,101):
  if z%10==0:
    print('Coding Dojo')
  elif z%5==0:
    print('Coding')
  else:
    print(z)

#4 ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
i = 0
for j in range(1,500001,2):
  i=i+j
print (i)

#5 Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for p in range(2018, -1, -4):
  print(p)

#6 Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas).
lowNum=0
highNum=11
mult=2
for r in range(lowNum, highNum+1):
  if r%2==0:
    print(r)

#7 BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?.

def primo(num):
  for t in range (2,num):
    if num%t==0:
      return False
  return True

primos1000 = [x for x in range(2, 1001) if primo(x)]
print(primos1000)