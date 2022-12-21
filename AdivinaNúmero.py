import random
import os
from time import *
print("\n[\033[1;34m~\033[1;39m] Adivina el número by -H3llo2005-\n")
sleep(2)
def main():
    try:
        TNM = int(input("Estoy pensando un número del 1 al 10 a ver si adivinas: "))
    except ValueError:
        print("Haber no intentes petar el programa y escribe un número")
        sleep(2)
        os.system("cls")
        main()
    MNM = random.randint(1, 10)
    if MNM == TNM:
        print("¡Has acertado!")
        sleep(2)
        input("Enter para salir: ")
    elif MNM != TNM:
        print("Ese no era el número:( ¡Sigue intentandolo!")
        sleep(2)
        os.system("cls")
        main()
if __name__ == '__main__':
    main()
