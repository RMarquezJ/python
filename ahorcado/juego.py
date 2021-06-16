from ahorcado import Ahorcado
import pdb

def main():
  print('Bienvenido al Ahorcado')
  vidas=input('Ingrese el numero de vidas')
  ahorcado=Ahorcado(int(vidas))
  while True:
    dibujar = ahorcado.dibujar()
    letra=input('Ingrese una letra').upper()
    res=ahorcado.jugar(letra)

main()