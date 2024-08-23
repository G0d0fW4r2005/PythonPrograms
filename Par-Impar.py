print("\n[\033[1;34m~\033[1;39m] Par-Impar by -G0d0fW4r2005-\n")
def main():
    try:
        TN = int(input("\n[\033[1;34m+\033[1;39m] Dime un número entero: "))
    except ValueError:
        print("Inteligente un número entero no puede tener decimales y si has escrito letras pues es no funciona:(")
        input("Enter para terminar: ")

    if TN % 2 == 0:
        print("El número es par")
        input("Enter para terminar: ")
    elif TN % 2 != 0:
        print("El número es impar")
        input("Enter para terminar: ")

if __name__ == '__main__':
    main()
