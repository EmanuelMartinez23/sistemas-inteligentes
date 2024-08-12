import numpy as np
import matplotlib.pyplot as plt

# Definir la función dada
def f(x):
    return (np.cos(2*x + 1) +
            2 * np.cos(3*x + 2) +
            3 * np.cos(4*x + 3) +
            4 * np.cos(5*x + 4) +
            5 * np.cos(6*x + 5))

def hillClimbing(f, puntoIncial, tamPaso=0.01, maxIteraciones=1000):
    #inicializamos el punto actual
    puntoActual = puntoIncial
    for _ in range(maxIteraciones):
        # Probar el siguiente punto en la dirección positiva
        puntoSiguiente = puntoActual + tamPaso
        # Vemos si el valor de la funcion en el siguiente punto es mayor movemos a ese punto
        if f(puntoSiguiente) > f(puntoActual):
            puntoActual = puntoSiguiente
        else:
            # Sino probamos el siguiente punto en la dirección negativa
            puntoSiguiente = puntoActual - tamPaso
            # Si el valor de la función en el siguiente punto es mayor, movernos a ese punto
            if f(puntoSiguiente) > f(puntoActual):
                puntoActual = puntoSiguiente
            else:
                #Si no hay mejora en ninguna dirección, detener la búsqueda
                break
    #Regresamos el punto con el máximo encontrado
    return puntoActual

#encontramos los  máximos y mínimos locales en el rango [-10, 10]
valoresDelRango = np.arange(-10, 10, 0.01)
# lista donde se almacenara los minimos y los maximos 
localMaximo = []
localMinimo = []

#para cada valor inicial en el rango encontrar un maximo local
for puntoIncial in valoresDelRango:
    localMax = hillClimbing(f, puntoIncial)
    #verificar si el máximo encontrado es único en la lista
    if not any(np.isclose(localMax, x, atol=1e-2) for x in localMaximo):
        localMaximo.append(localMax)

#clasificar y eliminar duplicados de máximos locales teniendo estos salen los minimos
localMaximo = sorted(list(set(localMaximo)))
#encontramos los minimos locales usando la función negativa
localMinimo = sorted([hillClimbing(lambda x: -f(x), x) for x in localMaximo])

# nos quedamos con los tres maximos y tres minimos más significativos
localMaximo = sorted(localMaximo, key=f, reverse=True)[:3]
localMinimo = sorted(localMinimo, key=f)[:3]

# Graficamos
# Rango de valores de la grafica 
x = np.linspace(-10, 10, 400)
# nuestra función dada
y = f(x)  
plt.plot(x, y, label='f(x)')
plt.scatter(localMaximo, [f(x) for x in localMaximo], color='blue', label='Máximos locales')
plt.scatter(localMinimo, [f(x) for x in localMinimo], color='green', label='Mínimos locales')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Hill Climbing: Máximos y Mínimos Locales')
plt.legend()
plt.grid(True)
plt.show()
