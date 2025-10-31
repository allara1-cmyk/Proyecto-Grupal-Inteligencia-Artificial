from BFS import *
import time
import os
    
def menuprincipal():
    print("============== MENU PRINCIPAL =============")
    print("=========== BUSQUEDA EN ANCHURA ===========")
    print("1. Agregar una palabra al txt")
    print("2. Recorrer palabras en Arbol")
    print("3. Realizar busqueda BFS por inicio y fin")
    print("4. Realizar busqueda BFS por valor ASCII")
    print("5. Salir")
    opc = int(input("Ingrese una opcion: "))
    return opc

if __name__ == "__main__":
    ruta = "Archivos/palabras_1000.txt"
    Arbol = cargar_palabras_en_arbol(ruta)
    os.system('cls')
    print("============== PROYECTO U1 =================")
    print("Realizado por Anderson Lara y Juan Jiménez")
    time.sleep(3)
    os.system('cls')
    while True:
        os.system('cls')
        opc = menuprincipal()
        os.system('cls')
        match opc:
            case 1:
                nueva_palabra = input("Ingrese la nueva palabra: ").strip()
                significado = input("Ingrese el significado de la palabra: ").strip()
                with open(ruta, "a", encoding="utf-8") as f:
                    f.write(f"\n{nueva_palabra}:{significado}")
                Arbol.insertar(nueva_palabra, significado)
                print("\n¡Palabra agregada exitosamente!")
                input("Presiona ENTER para continuar...")
            case 2:
                Arbol.imprimir_inorder()
                input("Presiona ENTER para continuar...")
            case 3:
                inicio = input("Ingrese el nodo inicial de la busqueda: ")
                fin = input("Ingrese el nodo final de la busqueda: ")
                print(buscar_camino_entre_palabras(Arbol, inicio, fin))
                input("Presiona ENTER para continuar...")
            case 4:
                palabra = input("Ingrese la palabra para realizar busqueda BFS (por ASCII): ").strip()
                print("\nResultado de la búsqueda por anchura (ASCII):\n")
                resultado = busqueda_anchura_ascii(Arbol, palabra)
                print(resultado)
                input("Presiona ENTER para continuar...")
            case 5:
                print("Saliendo del programa")
                time.sleep(2)
                os.system('cls')
                break
            case _:
                print("Opcion no valida")
                time.sleep(2)
