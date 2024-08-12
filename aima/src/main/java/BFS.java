/*
Author: Emanuel
Date: 05/08/2024
*/

import java.util.*;

public class BFS {

    /**
     * Encuentra el camino más corto desde el nodo de inicio hasta el nodo objetivo
     * utilizando el algoritmo de Búsqueda en Anchura (BFS).
     *
     * @param map El mapa de Rumania representado como un grafo.
     * @param start El nodo de inicio.
     * @param goal El nodo objetivo.
     * @return La lista de nodos que forman el camino más corto desde el inicio hasta el objetivo.
     */
    public static List<String> buscarRutaCortaBFS(ExtendableMap  map, String start, String goal) {
        // Cola para almacenar los caminos a explorar
        Queue<List<String>> queue = new LinkedList<>();
        //Conjunto para rastrear los nodos visitados
        Set<String> visitado = new HashSet<>();
        // Agregar el nodo de inicio a la cola como el primer camino
        queue.add(Collections.singletonList(start));
        // Marcar el nodo de inicio como visitado
        visitado.add(start);

        // Mientras haya caminos en la cola
        while (!queue.isEmpty()) {
            // Obtener el camino en la parte frontal de la cola
            List<String> ruta = queue.poll();
            // Obtener el último nodo en el camino actual
            String nodoActual = ruta.get(ruta.size() - 1);

            // Si el nodo objetivo es alcanzado, devolver la ruta
            if (nodoActual.equals(goal)) {
                return ruta;
            }

            // Mientras vamos recorriendo
            // Obtener todos los nodos adyacentes al nodo actual
            for (String vecinos : map.getPossibleNextLocations(nodoActual)) {
                // Si el nodo adyacente no ha sido visitado
                if (!visitado.contains(vecinos)) {
                    // Marcar el nodo adyacente como visitado
                    visitado.add(vecinos);
                    // Crear un nuevo camino extendiendo el camino actual con el nodo adyacente
                    List<String> nuevaRuta = new ArrayList<>(ruta);
                    nuevaRuta.add(vecinos);
                    // Agregar el nuevo camino a la cola
                    queue.add(nuevaRuta);
                }
            }
        }
        // Devolver una lista vacía si no se encuentra un camino
        return Collections.emptyList();
    }

    public static void main(String[] args) {
        // Crear el mapa de Rumania
        ExtendableMap map = new SimplifiedRoadMapOfRomania();

        // Definir el nodo de inicio y el nodo objetivo
        String start = SimplifiedRoadMapOfRomania.ARAD;
        String goal = SimplifiedRoadMapOfRomania.BUCHAREST;

        // Medir el tiempo de inicio
        long tiempoDeIncio = System.nanoTime();

        //Encontrar el camino más corto desde Arad hasta Bucarest utilizando BFS
        List<String> ruta = buscarRutaCortaBFS(map, start, goal);

        //medir el tiempo de finalización
        long tiempoDeFinal = System.nanoTime();

        //Calcular el tiempo tomado
        long duracion = (tiempoDeFinal - tiempoDeIncio) / 1000000;

        System.out.println("Ruta más corta de " + start + " a " + goal + ": " + ruta);
        System.out.println("Tiempo : " + duracion + "ms");

        // Calcular el uso de memoria
        Runtime runtime = Runtime.getRuntime();
        runtime.gc(); // Sugerir al recolector de basura que limpie
        long memoriaUsada = runtime.totalMemory() - runtime.freeMemory();
        System.out.println("Memoria usada (bytes): " + memoriaUsada);
    }
}
