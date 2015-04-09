package centrality;

import org.jgrapht.*;
import org.jgrapht.alg.*;
import centrality.Graph;

class ClosenessCentrality{
    static UndirectedGraph graph = Graph.get();

    public static double get(int node){
        double sumOfLength = 0;
        for( int i = 0; i < Graph.getNumberOfVertexes(); i++ ){
            if(i != node){
                DijkstraShortestPath dijstra
                    = new DijkstraShortestPath(graph,
                            Graph.getVertex(node),
                            Graph.getVertex(i));
                sumOfLength += dijstra.getPathLength();
            }
        }
        double closeness = (Graph.getNumberOfVertexes()-1)/sumOfLength;
        return closeness;
    }

}
