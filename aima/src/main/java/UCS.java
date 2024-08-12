/*
Author: Emanuel
Date: 05/08/2024
*/
import java.util.*;

public class UCS {

    private static class Node {
        String name;
        double cost;

        Node(String name, double cost) {
            this.name = name;
            this.cost = cost;
        }
    }
    public static List<String> buscarRutaUCS(ExtendableMap map, String start, String goal) {
        // Utiliza una cola de prioridad para explorar los nodos ordenados por el costo del camino
        PriorityQueue<Node> frontera = new PriorityQueue<>(Comparator.comparingDouble(node -> node.cost));

        //mapa para mantener el costo más bajo conocido para llegar a cada nodo
        Map<String, Double> costoAct = new HashMap<>();

        //mapa para reconstruir el camino desde el nodo de inicio hasta el nodo objetivo
        Map<String, String> mapSucesor = new HashMap<>();

        //agregar el nodo inicial a la cola de prioridad con costo 0
        frontera.add(new Node(start, 0.0));
        // Establecer el costo de llegar al nodo de inicio como 0
        costoAct.put(start, 0.0);
        // Marcar el nodo de inicio como el nodo inicial en el mapa mapSucesor
        mapSucesor.put(start, null);

        //  mientras haya nodos en la cola de prioridad
        while (!frontera.isEmpty()) {
            //Extrae el nodo con el costo más bajo de la cola de prioridad
            Node nodoActual = frontera.poll();
            // Obtiene el nombre del nodo actual
            String actualN = nodoActual.name;
            // Si el nodo actual es el objetivo, sale del bucle
            if (actualN.equals(goal)) {
                break;
            }

            // Recorre todos los vecinos del nodo actual
            for (String vecino : map.getPossibleNextLocations(actualN)) {
                //Calcula el costo total para llegar al vecino desde el nodo actual
                double nuevoCosto = costoAct.get(actualN) + map.getDistance(actualN, vecino);
                // Si el costo encontrado es menor al costo registrado, actualiza el costo y el camino
                if (!costoAct.containsKey(vecino) || nuevoCosto < costoAct.get(vecino)) {
                    // Actualiza el costo para llegar al vecino
                    costoAct.put(vecino, nuevoCosto);
                    // Agrega el vecino a la cola de prioridad con el costo actualizado
                    frontera.add(new Node(vecino, nuevoCosto));
                    // Actualiza el camino para llegar al vecino
                    mapSucesor.put(vecino, actualN);
                }
            }
        }
        //reconstruye el camino desde el nodo objetivo hasta el nodo de inicio
        List<String> ruta = new ArrayList<>();
        for (String at = goal; at != null; at = mapSucesor.get(at)) {
            // Agrega cada nodo al camino
            ruta.add(at);
        }
        // Invierte el camino para que sea del inicio al objetivo
        Collections.reverse(ruta);
        // Devuelve el camino del inicio al objetivo
        return ruta;
    }


    public static void main(String[] args) {
        ExtendableMap map = new SimplifiedRoadMapOfRomania();

        // Tiempo de incio
        long tiempoDeIncio = System.nanoTime();

        // Buscar la ruta de Arad a Bucharest usando UCS
        List<String> ruta = buscarRutaUCS(map, SimplifiedRoadMapOfRomania.ARAD, SimplifiedRoadMapOfRomania.BUCHAREST);

        // Tiempo final
        long tiempoFinal = System.nanoTime();

        // Calcular el tiempo tomado
        long duracion = (tiempoFinal - tiempoDeIncio) / 1000000;

        //Calcular memoria usada
        Runtime runtime = Runtime.getRuntime();
        runtime.gc();
        long memoriaUsada = runtime.totalMemory() - runtime.freeMemory();


        System.out.println("Ruta de Arad a Bucharest usando UCS: " + ruta);
        System.out.println("Tiempo tomado: " + duracion + " ms");
        System.out.println("Memoria usada: " + memoriaUsada + " bytes");
    }
}
