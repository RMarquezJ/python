import random
def randInt(min=0, max=100):
  if min>=max:
    return False
  #elif max<=0:
    #return False
  num = round(random.random()*(max-min)+min)
  return num
print(randInt(7,1500))

def getCarton():
  carton=[]
  while True:
    bolita = randInt(1,36)
    if bolita in carton:
      continue
    carton.append(bolita)
    if len(carton) == 6:
      break
  return carton
print(getCarton())

def loto():
  while True:
    eleccion=input('ingrese 1 para jugar o si no terminará el juego/n')
    if eleccion != '1':
      break
    carton_usuario=getCarton()
    carton_casa=getCarton()
    aciertos=0
    print('Su carton es:', carton_usuario)
    print('las bolitas que salieron son', carton_casa)
    for bolita in carton_usuario:
      if bolita in carton_casa:
        aciertos +=1
    if aciertos==3:
      print('Usted Ganó $1000')
    elif aciertos==4:
      print('Usted ganó $30000')
    elif aciertos==5:
      print('Usted ganó $1500000')
    elif aciertos==6:
      print('Usted ganó 300.000.000')
  print('Gracias por jugar al Loto')