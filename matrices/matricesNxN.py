import numpy as np
import random
import math

# Calcular la suma de un cuadrado para la fila, columna y diagonal 
def calcularSuma(n):
    return n * (n**2 + 1) // 2

# Funcion para calcular el costo, mas bao indica que no tiene tantas penalizaciones
def calcularCosto(matriz, suma):
    #Dimasion de la matriz
    n = len(matriz)
    costo = 0
    #Recorremos la fila y la columna de la matriz
    for i in range(n):
        # almacenamos el costo
        costo += abs(sum(matriz[i]) - suma)
        costo += abs(sum(matriz[:, i]) - suma)
    #Añadimos el de las diagonales
    costo += abs(sum(matriz.diagonal()) - suma)
    costo += abs(sum(np.fliplr(matriz).diagonal()) - suma)
    #Devolvemos el costo total de la matriz
    return costo

# funcion para generar una matriz vecina intercambiando dos elementos aleatorios en la matriz actual.
def generarVecino(matriz):
    n = len(matriz)
    i, j = random.sample(range(n), 2)
    k, l = random.sample(range(n), 2)
    vecino = matriz.copy()
    vecino[i, j], vecino[k, l] = vecino[k, l], vecino[i, j]
    return vecino

def recocidoSimulado(n, temperaturaInicial, tasaEnfriamiento, iteraciones):
    #Generamos una matriz n x n con los numeros del 1 al n^2 en un orden aleatorio.
    matriz = np.arange(1, n*n + 1).reshape(n, n)
    # mezclamos los elemento de la raiz
    np.random.shuffle(matriz)
    
    suma = calcularSuma(n)
    mejorMatriz = matriz.copy()
    mejorCosto = calcularCosto(matriz, suma)
    #temperatura
    temperatura = temperaturaInicial
    for _ in range(iteraciones):
        vecino = generarVecino(matriz)
        costoActual = calcularCosto(matriz, suma)
        costoVecino = calcularCosto(vecino, suma)
        #Decidimos si aceptar la nueva matriz vecina.
        if costoVecino < mejorCosto or random.random() < math.exp((costoActual - costoVecino) / temperatura):
            #aceptamos la matriz vecina
            matriz = vecino
            # si es mejor el costo de la matriz vecina que la guarde como la mejor  
            if costoVecino < mejorCosto:
                mejorMatriz = vecino
                mejorCosto = costoVecino
        #reducimosla temperatura 
        temperatura *= tasaEnfriamiento

    return mejorMatriz

# funcion quepara la suma de cada fila, columna y diagonales de la matriz.
def imprimirSumas(matriz):
    n = len(matriz)
    #calcular la suma de  cada fila, columna y diagonales.
    sumaFilas = [sum(fila) for fila in matriz]
    sumacolumnas = [sum(matriz[:, i]) for i in range(n)]
    sumaDiagonalPrincipal = sum(matriz.diagonal())
    sumaDiagonalSecundaria = sum(np.fliplr(matriz).diagonal())
    
    # Imprimimos 
    print("Suma de cada fila :", sumaFilas)
    print("Suma de cada columna :", sumacolumnas)
    print("Suma de  la diagonal principal :", sumaDiagonalPrincipal)
    print("Suma de la diagonal secundaria :", sumaDiagonalSecundaria)

# Ejemplo con una matriz 4x4.
n = 4
#Valores iniciales
temperaturaInicial = 100000  
tasaEnfriamiento = 0.999
iteraciones = 50000
mejorMatriz = recocidoSimulado(n, temperaturaInicial, tasaEnfriamiento, iteraciones)
print("Mejor matriz encontrada:")
print(mejorMatriz)
imprimirSumas(mejorMatriz)
