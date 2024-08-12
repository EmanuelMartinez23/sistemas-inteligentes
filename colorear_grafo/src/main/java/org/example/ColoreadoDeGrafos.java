package org.example;
/*
Author: Emanuel
Date: 20/07/2024
*/
import java.util.*;
public class ColoreadoDeGrafos {
    // matriz de adyacencia del grafo
    static int[][] matrizAdyacencia;
    // los colores disponibles para colorear los nodos
    static String[] conjuntoColores;
    // número total de nodos en el grafo
    static int nNodos;

    public static void main(String[] args) {
        // inicializamos la matriz de adyacencia del grafo
        matrizAdyacencia = new int[][]{
                {0, 1, 0,0},
                {1, 0, 1,0},
                {0, 1, 0,0},
                {1, 1, 0,0}
        };

        // número de nodos del grafo
        nNodos = matrizAdyacencia.length;

        // conjunto de colores disponibles
        conjuntoColores = new String[]{"Sin Color", "Azul", "Rojo", "Verde", "Amarillo"};

        // array que almacenará el color de cada nodo
        String[] coloresNodo = new String[nNodos];
        // inicializamos el array de coloresNodo de nodos en "Sin Color"
        Arrays.fill(coloresNodo, conjuntoColores[0]);

        colorear(matrizAdyacencia, coloresNodo, conjuntoColores);

        // imprime el estado final de los nodos
        System.out.println("Colores de los nodos: " + Arrays.toString(coloresNodo));
    }

    public static void colorear(int[][] grafo, String[] coloresNodo, String[] conjuntoColores) {
        // recorremos el grafo nodo a nodo
        for (int nodo = 0; nodo < grafo.length; nodo++) {
            System.out.println("Nodo: "+ (nodo+1));
            // array para marcar qué colores están disponibles para el nodo actual
            boolean[] disponible = new boolean[conjuntoColores.length];
            // inicializamos todos los colores como disponibles
            Arrays.fill(disponible, true);

            // recorremos los nodos adyacentes al nodo actual
            for (int nodoAdj = 0; nodoAdj < grafo.length; nodoAdj++) {
                // si el nodoAdj es adyacente al nodo actual y ya tiene un color del conjuntoColores
                if (grafo[nodo][nodoAdj] == 1 && !coloresNodo[nodoAdj].equals(conjuntoColores[0])) {
                    // marcamos el color del nodo adyacente como no disponible
                    for (int i = 1; i < conjuntoColores.length; i++) {
                        if (coloresNodo[nodoAdj].equals(conjuntoColores[i])) {
                            disponible[i] = false;
                        }
                    }
                }
            }
            // variable que almacena un color disponible para el nodo actual
            int colorIndex;
            // buscamos el primer color disponible
            for (colorIndex = 1; colorIndex < conjuntoColores.length; colorIndex++) {
                if (disponible[colorIndex]) {
                    break;
                }
            }
            // asignamos el color disponible al nodo actual
            System.out.println("Color a asignar "+ conjuntoColores[colorIndex]);
            coloresNodo[nodo] = conjuntoColores[colorIndex];
        }
    }
}
