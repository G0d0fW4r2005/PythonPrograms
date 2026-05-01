import math

print("\n♦ Pendulo Balistico by ~G0d0fW4r2005~\n")
print("Hola! Bienvenido al simulador de péndulo balístico.")
print("NOTA IMPORTANTE: Para introducir decimales se debe usar el (.) no la (,).")
print("Las simulaciones están calculadas para casos ideales sin perdidas de energia.")

# Datos que se deben introducir
masa_proyectil = float(input("Introduzca la masa del proyectil (kg): "))
masa_balistica = float(input("Introduzca la masa del cuerpo balístico (kg): "))
L_pendulo = float(input("Introduzca la longitud del péndulo (m): "))
gravedad = 9.81

masa_total = masa_proyectil + masa_balistica

# Datos opcionales
print("\n¿Qué quieres introducir?")
print("1 - Velocidad inicial del proyectil")
print("2 - Altura máxima del péndulo")

opcion = int(input("Elige 1 o 2: "))

# Opción velocidad inicial
if opcion == 1:
    velocidad_proyectil = float(input("Introduzca la velocidad del proyectil (m/s): "))
    
    # Conservación de la cantidad de movimiento
    velocidad_final = (masa_proyectil * velocidad_proyectil) / masa_total
    
    # Altura máxima
    altura = (velocidad_final ** 2) / (2 * gravedad)
    
    # Angulo que alcanza
    if altura > L_pendulo:
        print("Error: altura no válida (supera la longitud del péndulo).")
    else:
        angulo_rad = math.acos(1 - altura / L_pendulo)
        rad_grados = math.degrees(angulo_rad)
        
        print("\n___RESULTADOS___")
        print("Velocidad después del impacto: ", round(velocidad_final, 3), "m/s")
        print("Altura máxima :", round(altura, 3), "m")
        print("Ángulo máximo: ", round(theta_grados, 2), "grados")

# Opción altura final
elif opcion == 2:
    altura = float(input("Introduzca la altura máxima (m): "))
    
    # Velocidad despues del choque
    velocidad_final = math.sqrt(2 * gravedad * altura)
    
    # Velocidad inicial del proyectil
    velocidad_proyectil = (masa_total * velocidad_final) / masa_proyectil
    
    # Angulo final
    if altura > L_pendulo:
        print("Error: altura no válida (supera la longitud del péndulo).")
    else:
        angulo_rad = math.acos(1 - altura / L_pendulo)
        rad_grados = math.degrees(angulo_rad)
        
        print("\n___RESULTADOS___")
        print("Velocidad después del impacto: ", round(velocidad_final, 3), "m/s")
        print("Velocidad inicial del proyectil: ", round(velocidad_proyectil, 3), "m/s")
        print("Ángulo máximo: ", round(theta_grados, 2), "grados")

else:
    print("Opción no válida. Reinicia el programa.")
