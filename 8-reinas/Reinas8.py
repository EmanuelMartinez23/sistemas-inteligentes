import random
import math
# Problema de las 8 reinas con algoritmo recocido simulado

#funcion para caqlcular el numero de ataques entre las reinas
def calcularAtaques(estado):
    ataques = 0
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            # si es que se cumplen estan en la misma columna y es una ataque
            if estado[i] == estado[j]:
                ataques += 1
            # de igual manera pero para una diagonal
            if abs(estado[i] - estado[j]) == abs(i - j):
                ataques += 1
    return ataques

# generar un nuevo estadode nuestro tablero intercambiando la posicion de una reina
def generar_vecino(estado):
    n = len(estado)
    nuevoEstado = estado[:]
    fila = random.randint(0, n - 1)
    nuevaColumna = random.randint(0, n - 1)
    nuevoEstado[fila] = nuevaColumna
    return nuevoEstado

# funcion para simular el enfriamento en el algoritmo reduciendo gradualmente la temperatura
def enfriamiento(t):
    return t * 0.99

# Parámetros
tempActual = 1000
tempFinal = 1e-8
iteraciones = 1000

#solucion inicial aleatoria
n = 8
estadoActual = [random.randint(0, n - 1) for _ in range(n)]
costoActual = calcularAtaques(estadoActual)
temperatura = tempActual

# Recocido Simulado
for _ in range(iteraciones):
    # si no hay ataques hemos encontrado una solucion optima
    if costoActual == 0:
        break
    
    vecino = generar_vecino(estadoActual)
    costoVecino = calcularAtaques(vecino)
    print(costoVecino)
    
    deltaCosto = costoVecino - costoActual
    
    if deltaCosto < 0 or random.uniform(0, 1) < math.exp(-deltaCosto / temperatura):
        estadoActual = vecino
        costoActual = costoVecino
    
    temperatura = enfriamiento(temperatura)
    
    if temperatura < tempFinal:
        break

# tablero final
tablero = [["   " for _ in range(n)] for _ in range(n)]
for fila in range(n):
    tablero[fila][estadoActual[fila]] = " x "

for fila in tablero:
    print("|" + "|".join(fila) + "|")
