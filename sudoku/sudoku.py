import random
import math
import copy
# tamaño del tablero de sudoku 9 x 9
N = 9

# Calula las penalizaciones de un tablero del sudoku
def calcularPenalizacion(tablero):
    penalizacion = 0
    for i in range(N):
        # conjuuntop para verificar el duplicado en las filas 
        fila = set()
        # conjunto para verificar el duplicado en las columnas
        col = set()
        # iteramos 
        for j in range(N):
            # penalizacion duplicado en las filas 
            if tablero[i][j] in fila:
                penalizacion += 1
            # penalizacion duplicados en las columnas
            if tablero[j][i] in col:
                penalizacion += 1
            fila.add(tablero[i][j])
            col.add(tablero[j][i])
    
    return penalizacion

# funcion para llenar los espacios con numeros aleatorios  en cada subcuadro de 3 x 3 
def inicializarTablero(tablero):
    # recorremos los subcuadros de 3 x 3 en el tablero
    for x in range(0, N, 3):
        for y in range(0, N, 3):
            # numeros del 1 al 9 
            numerosFaltantes = list(range(1, N+1))
            # mezclamos los numeros para que sean aleatorios
            random.shuffle(numerosFaltantes)
            for i in range(3):
                for j in range(3):
                    # si la celda estqa vacia la llenamos con un numero vacio 
                    if tablero[x+i][y+j] == 0:
                        tablero[x+i][y+j] = numerosFaltantes.pop()
    return tablero

# Aplica el algoritmo de recocido simulado para resolver el Sudoku
def recocidoSimulado(tablero):
    # obtenemos el tablero inicial
    mejorTablero = inicializarTablero(copy.deepcopy(tablero))
    # calculamos las penalizaciones del tablero inicial 
    mejorPenalizacion = calcularPenalizacion(mejorTablero)
    # temperatura inicial
    temperatura = 1.0
    # Tasa en la que va ir decrementamndo
    tasa_enfriamiento = 0.9999

    # se ejecute mientars que tengamos penalizaciones y la temeratura sea alta 
    while temperatura > 0.001 and mejorPenalizacion > 0:
        # creamos una copia del tablero actual
        nuevoTablero = copy.deepcopy(mejorTablero)
        # seleccionamos un subcuadro de 3 x 3 y tomamos dos posiciones dentro de el para intercambiar 
        x = random.randint(0, 2) * 3
        y = random.randint(0, 2) * 3
        fila1, col1 = random.randint(0, 2), random.randint(0, 2)
        fila2, col2 = random.randint(0, 2), random.randint(0, 2)
        # nos aseguramos que las posiciones a intercambiar esten vacias 
        while nuevoTablero[x+fila1][y+col1] == 0:
            fila1, col1 = random.randint(0, 2), random.randint(0, 2)
        while nuevoTablero[x+fila2][y+col2] == 0:
            fila2, col2 = random.randint(0, 2), random.randint(0, 2)

        #Intercambiamos los valores en las dos posiciones seleccionadas
        nuevoTablero[x+fila1][y+col1], nuevoTablero[x+fila2][y+col2] = nuevoTablero[x+fila2][y+col2], nuevoTablero[x+fila1][y+col1]
        # calculamos las penalizaciones del nuevo tablero
        nuevaPenalizacion = calcularPenalizacion(nuevoTablero)  
        #aceptamos el nuevo tablero si es  mejor a  la penalización o aleatoriamente basado en la temperatura
        if nuevaPenalizacion < mejorPenalizacion or random.uniform(0, 1) < math.exp((mejorPenalizacion - nuevaPenalizacion) / temperatura):
            mejorTablero = nuevoTablero
            mejorPenalizacion = nuevaPenalizacion
        # reducimos la temperatura
        temperatura *= tasa_enfriamiento

    return mejorTablero, mejorPenalizacion

# Funcion para mostrar el tablero
def mostrarTablero(tablero):
    for i in range(N):
        if i % 3 == 0 and i != 0:
            # Separador entre bloques de 3 x 3
            print("-" * 21)
        fila = ""
        for j in range(N):
            if j % 3 == 0 and j != 0:
                #Separador entre columnas de 3
                fila += "| "
            fila += str(tablero[i][j]) + " "
        print(fila)

#generar el tablero con los 16 valores iniciales validos
def generarTableroInicial():
    #Incializamos un tablero vacio
    tablero = [[0]*N for _ in range(N)]
    # colocamos los 16 valores iniciales
    for _ in range(16):
        fila = random.randint(0, N-1)
        col = random.randint(0, N-1)
        # que encuentre una celda vaciaa
        while tablero[fila][col] != 0:
            fila = random.randint(0, N-1)
            col = random.randint(0, N-1)
        num = random.randint(1, N)
        #asegurmaos que el numero sea valido
        while not esValido(tablero, fila, col, num):
            num = random.randint(1, N)
        #colocamos el numero en la celda del tablero
        tablero[fila][col] = num
    return tablero

# validamos si el numero puede estar en esa fila, col de acuerdo a las restricciones
def esValido(tablero, fila, col, num):
    for i in range(N):
        #verificamos las filas y columnas
        if tablero[fila][i] == num or tablero[i][col] == num:
            return False
    
    #Verificamos el subcuadro 3 x 3
    inicioFila, inicioCol = 3 * (fila // 3), 3 * (col // 3)
    for i in range(inicioFila, inicioFila + 3):
        for j in range(inicioCol, inicioCol + 3):
            if tablero[i][j] == num:
                return False
    return True

# principal
#generamos un tablero inicial
tableroIncial = generarTableroInicial()
#Resolvemos el tablero con el algoritmo
tableroResuelto, penalizacion = recocidoSimulado(tableroIncial)
#Imprimimos los resultados 
print("Tablero Inicial:")
mostrarTablero(tableroIncial)
print("\nTablero Resuelto:")
mostrarTablero(tableroResuelto)
print(f"\nPenalizaciones: {penalizacion}") 