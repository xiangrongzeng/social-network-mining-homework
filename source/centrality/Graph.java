package centrality;

import org.jgrapht.*;
import org.jgrapht.graph.*;

class Graph {
    private static String[] vertexes = {
        "v1", "v2", "v3", "v4", "v5",
        "v6", "v7", "v8", "v9", "v10"};
//    private static String[] vertexes = {
//        "v1", "v2", "v3", "v4", "v5"};

    public static UndirectedGraph<String, DefaultEdge> get(){
        UndirectedGraph<String, DefaultEdge> graph =
            new SimpleGraph<String, DefaultEdge>(DefaultEdge.class);

        for (int i = 0; i < vertexes.length; i++)
            graph.addVertex(vertexes[i]);

 //       graph.addEdge(vertexes[0],vertexes[1]);
 //       graph.addEdge(vertexes[1],vertexes[2]);
 //       graph.addEdge(vertexes[1],vertexes[3]);
 //       graph.addEdge(vertexes[2],vertexes[4]);
 //       graph.addEdge(vertexes[3],vertexes[4]);
        graph.addEdge(vertexes[1-1], vertexes[2-1]);
        graph.addEdge(vertexes[2-1], vertexes[3-1]);
        graph.addEdge(vertexes[3-1], vertexes[4-1]);
        graph.addEdge(vertexes[3-1], vertexes[5-1]);
        graph.addEdge(vertexes[3-1], vertexes[6-1]);
        graph.addEdge(vertexes[4-1], vertexes[5-1]);
        graph.addEdge(vertexes[4-1], vertexes[6-1]);
        graph.addEdge(vertexes[5-1], vertexes[6-1]);
        graph.addEdge(vertexes[6-1], vertexes[7-1]);
        graph.addEdge(vertexes[7-1], vertexes[8-1]);
        graph.addEdge(vertexes[7-1], vertexes[9-1]);
        graph.addEdge(vertexes[8-1], vertexes[9-1]);
        graph.addEdge(vertexes[8-1], vertexes[10-1]);
        graph.addEdge(vertexes[9-1], vertexes[10-1]);

        return graph;
    }

    public static int getNumberOfVertexes(){
        return vertexes.length;
    }

    public static String getVertex(int node){
        return vertexes[node];
    }
}
