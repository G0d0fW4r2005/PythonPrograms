import random
print("\n♦ Ruleta Rusa by ~G0d0fW4r2005~\n")
a = input("\n♥ Presiona Enter para meter la bala...\n")
Bala = random.randint(1,6)
Hueco_Dead = random.randint(1,6)
input("\n♠ Presiona Enter para darle vueltas al cargador y disparar\n")
if a == "666":
    print("\n• Satanas aparece ante tí, por haberle llamado incordiandole te atraviesa con una lanza perforandote el corzaón de lado a lado\n")
elif Bala == Hueco_Dead:
    print("\nX Caes de rodillas al suelo para luego desbanecerte debido al balazo que has recibido...\n")
    input("\nX Enter para cerrar esta vida...\n")
    exit()
elif Bala != Hueco_Dead:
    print("\n+ Estas vivo, la pistola se te cae de las manos y sales corriendo de la habitación... \n")
    input("+ Enter para vivir tu vida normal...")
    exit()
