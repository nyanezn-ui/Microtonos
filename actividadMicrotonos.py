import winsound # Libreria que permite activar sonidos
import time
print("=== Simulador de microtonos ===")
maximo_microtonos = 25
microtonos_libres = 25
microtonos_activos = 0
ejecutando = True
while ejecutando:
    print("\n=== Panel de microtonos ===")
    print("1.- Ver cuántos microtonos quedan libres")
    print("2.- Activar microtonos (Activación de sonido)")
    print("3.- Recuperar microtonos")
    print("4.- Monitorear el sonido actual")
    print("5.- Salir")
    opcion = int(input("Elige una opción(1-5): "))
    if opcion == 1:
        print(f"\n[INFO] Tienes {microtonos_libres} microtonos disponibles para usar")
    elif opcion == 2:
        print(f"\n ACTIVAR MICROTONOS (Disponibles: {microtonos_libres})")
        if microtonos_libres == 0:
            print("Ya no se pueden emitir más microtonos, sonido al limite")
        else: 
            try:
                cantidad =int(input("¿Cuántos microtonos quieres activar?: "))
                if cantidad <= 0:
                    print("Tienes que activar al menos 1 microtono")
                elif cantidad > microtonos_libres:
                    print(f"Solo puedes activar hasta {microtonos_libres}")
                else:
                    microtonos_libres = cantidad 
                    microtonos_activos = cantidad
                    print("Reproduciendo")
                    #for i in range (1,cantidad +1):
                    #   print(f"Microtono {i} activado...")
                    #   winsound.Beep(440,300) # 440 HZ por 300milesimas de segundo
                    #   time.sleep(0.05)
                    frecuencias = [440,440,440,587,880,784,740,659]
                    duraciones = [300,300,300,700,700,200,200,200]
                    for i in range (1, cantidad +1):
                        nota_actual = frecuencias[(i-1) % len(frecuencias)]
                        duracion_actual = duraciones[(i -1) % len(duraciones)]
                        winsound.Beep(nota_actual,duracion_actual)
                        time.sleep(0.05)
            except ValueError:
                    print("Error")
    elif opcion == 3:
        try:
            print(f"\n Recuperar microtonos, actualmente hay {microtonos_activos} microtonos activos")
            cantidad = int(input("¿Cuántos tonos quieres recuperar?: "))
            if cantidad <= 0:
                print("Error, la contidad de microtonos a recuperar debe ser mayor a 0")
            elif microtonos_libres + cantidad > maximo_microtonos:
                print("Error: no puedes apagar tantos microtonos porque el máximo es {maximo_microtonos}") 
            else:
                microtonos_libres += cantidad
                microtonos_activos -= cantidad
                print(f"Recuperaste {cantidad} de microtonos para ser usados en otro momento")
                winsound.Beep(440,150)
        except ValueError:
            print("Error, debes colocar un número entero") 
    else:
        print("Error")