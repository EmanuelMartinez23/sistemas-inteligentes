/*
Author: Emanuel
Date: 05/08/2024
*/

import java.util.*;

public class DFS {
    /**
     * Encuentra el camino más corto desde el nodo de inicio hasta el nodo objetivo
     * utilizando el algoritmo de Búsqueda en Profundidad(DFS).
     *
     * @param map El mapa de Rumania representado como un grafo.
     * @param start El nodo de inicio.
     * @param goal El nodo objetivo.
     * @return La lista de nodos que forman el camino más corto desde el inicio hasta el objetivo.
     */

    public static List<String> buscarRutaDFS(ExtendableMap map, String start, String goal) {
        // Pila para mantener el frente de búsqueda en DFS
        Stack<String> frontier = new Stack<>();
        // Mapa para rastrear el camino tomado para llegar a cada nodo
        Map<String, String> cameFrom = new HashMap<>();
        // Conjunto para rastrear los nodos ya visitados
        Set<String> visited = new HashSet<>();

        // Inicializa el algoritmo agregando el nodo de inicio a la pila
        frontier.push(start);
        // Marca el nodo de inicio como visitado
        cameFrom.put(start, null);

        // Bucle principal del algoritmo DFS
        while (!frontier.isEmpty()) {
            // Saca el nodo más reciente de la pila
            String current = frontier.pop();

            // Si el nodo actual es el objetivo, termina el bucle
            if (current.equals(goal)) {
                break;
            }

            // Si el nodo actual no ha sido visitado aún
            if (!visited.contains(current)) {
                // Marca el nodo actual como visitado
                visited.add(current);
                // Itera sobre los vecinos del nodo actual
                for (String neighbor : map.getPossibleNextLocations(current)) {
                    // Si el vecino no ha sido visitado ni añadido al camino
                    if (!cameFrom.containsKey(neighbor)) {
                        // Agrega el vecino a la pila para explorarlo
                        frontier.push(neighbor);
                        // Marca el nodo desde el cual se llegó al vecino
                        cameFrom.put(neighbor, current);
                    }
                }
            }
        }

        // Lista para almacenar el camino encontrado
        List<String> path = new ArrayList<>();
        // Reconstruye el camino desde el objetivo hasta el inicio
        for (String at = goal; at != null; at = cameFrom.get(at)) {
            path.add(at);
        }
        // Reversa la lista para obtener el camino desde el inicio al objetivo
        Collections.reverse(path);
        // Devuelve el camino encontrado
        return path;
    }
    public static void main(String[] args) {
        ExtendableMap map = new SimplifiedRoadMapOfRomania();

        // Ttiempo de incio
        long tiempoDeIncio = System.nanoTime();

        // Buscar la ruta de  Arad to Bucharest usando DFS
        List<String> ruta = buscarRutaDFS(map, SimplifiedRoadMapOfRomania.ARAD, SimplifiedRoadMapOfRomania.BUCHAREST);

        // Tiempo final
        long tiempoDeFinal = System.nanoTime();

        // Calcular tiempo tomado
        long duracion = (tiempoDeFinal - tiempoDeIncio) / 1000000;

        // Calcular la memoria usada
        Runtime runtime = Runtime.getRuntime();
        runtime.gc();
        long memoriaUsada = runtime.totalMemory() - runtime.freeMemory();

        System.out.println("Ruta de Arad to Bucharest usando DFS: " + ruta);
        System.out.println("Tiempo tomado: " + duracion + " ms");
        System.out.println("Memoria usada: " + memoriaUsada + " bytes");
    }
}
