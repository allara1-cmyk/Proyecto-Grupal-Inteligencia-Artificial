from Clases.arbol_binario import ArbolBinario
from Clases.nodo import Nodo
from Clases.palabra import Palabra
from Clases.cola import Cola

# Funcion para cargar las palabras del TXT en el arbol
def cargar_palabras_en_arbol(ruta_txt):
    arbol = ArbolBinario()
    with open(ruta_txt, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(":")
            if len(partes) == 2:
                palabra, significado = partes
                arbol.insertar(palabra.strip(), significado.strip())
    return arbol

# Función de busqueda por anchura, por medio del equivalente de la palabra en Ascii
def busqueda_anchura_ascii(arbol, palabra_fin):
    if arbol.raiz is None:
        print("El árbol está vacío.")
        return None

    objetivo = Palabra(palabra_fin)  # Inicializar la clase Palabra
    recorrido_general = []           # Guardar todos los recorridos realizados
    intentos = 0                     # Contador de intentos de búsqueda

    while True:
        intentos += 1
        cola = Cola()                # Usamos nuestra clase Cola
        cola.encolar(arbol.raiz)
        recorrido = []

        print(f"\nIntento {intentos} - ASCII objetivo = {objetivo.totalAscii}")

        while not cola.esta_vacia():
            nodo = cola.desencolar()
            recorrido.append(nodo.palabra)

            # Coincidencia en ASCII
            if nodo.totalAscii == objetivo.totalAscii:
                if nodo.palabra.lower() == palabra_fin.lower():
                    print("\nPalabra encontrada")
                    print(f"Palabra: {nodo.palabra}")
                    print(f"Significado: {nodo.significado}")
                    print(f"Total ASCII: {nodo.totalAscii}")
                    print(f"\nRecorrido BFS: {recorrido}")
                    return recorrido

            # Agregar los hijos a la cola si existen
            if nodo.izq:
                cola.encolar(nodo.izq)
            if nodo.der:
                cola.encolar(nodo.der)

        recorrido_general.extend(recorrido)

        # Si no se encontró, intentar ajustar el valor ASCII
        if objetivo.indice_ascii < len(objetivo.texto):
            objetivo.sumar_siguiente_ascii()
            print(f"Ajustando ASCII: nuevo total = {objetivo.totalAscii}")
        else:
            print(f"\nNo se encontró la palabra '{palabra_fin}' tras ajustar todas las letras posibles.")
            print(f"Recorrido completo: {recorrido_general}")
            return None

def buscar_camino_entre_palabras(arbol, palabra_inicial, palabra_final):
    if arbol.raiz is None:
        print("El árbol está vacío.")
        return None
    nodo_inicial = None
    cola_busqueda = Cola()
    cola_busqueda.encolar(arbol.raiz)
    while not cola_busqueda.esta_vacia():
        nodo = cola_busqueda.desencolar()
        if nodo.palabra.lower() == palabra_inicial.lower():
            nodo_inicial = nodo
            break
        if nodo.izq:
            cola_busqueda.encolar(nodo.izq)
        if nodo.der:
            cola_busqueda.encolar(nodo.der)
    if not nodo_inicial:
        print(f"No se encontró la palabra inicial '{palabra_inicial}'")
        return None
    visitados = set()
    cola = Cola()
    cola.encolar(nodo_inicial)
    camino = {}
    camino[nodo_inicial.palabra] = None
    print(f"\nComenzando búsqueda desde: {palabra_inicial}")
    print(f"Buscando: {palabra_final}")
    palabra_encontrada = False
    nodo_final = None
    while not cola.esta_vacia():
        nodo_actual = cola.desencolar()
        if nodo_actual.palabra not in visitados:
            visitados.add(nodo_actual.palabra)
            print(f"Visitando: {nodo_actual.palabra} (ASCII: {nodo_actual.totalAscii})")
            if nodo_actual.palabra.lower() == palabra_final.lower():
                palabra_encontrada = True
                nodo_final = nodo_actual
                break
            for siguiente in [nodo_actual.izq, nodo_actual.der]:
                if siguiente and siguiente.palabra not in visitados:
                    cola.encolar(siguiente)
                    camino[siguiente.palabra] = nodo_actual.palabra
    if palabra_encontrada:
        print("\n¡Palabra encontrada!")
        recorrido = []
        actual = nodo_final.palabra
        while actual is not None:
            recorrido.insert(0, actual)
            actual = camino[actual]
        print("\nCamino encontrado:")
        print(" -> ".join(recorrido))
        return recorrido
    else:
        print(f"\nNo se encontró un camino desde '{palabra_inicial}' hasta '{palabra_final}'")
        print("Palabras visitadas:", list(visitados))
        return None