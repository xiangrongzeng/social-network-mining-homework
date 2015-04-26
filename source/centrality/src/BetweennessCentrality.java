package centrality;

import java.util.*;
import org.jgrapht.*;
import org.jgrapht.graph.*;

import centrality.*;

class BetweennessCentrality {

    private static double[] betweenness = new double[AdjacentMatrix.getLength()];
    private static void calculate(){
        for(int i = 0;i < AdjacentMatrix.getLength();i++)
            betweenness[i] = 0.;
        for (int s = 0; s < AdjacentMatrix.getLength(); s++){
            Stack stack = new Stack();
            ArrayList list[] = new ArrayList[AdjacentMatrix.getLength()];
            int[] sigma = new int[AdjacentMatrix.getLength()];
            int[] distance = new int[AdjacentMatrix.getLength()];
            // init
            for (int i = 0; i < AdjacentMatrix.getLength(); i++){
                sigma[i] = 0;
                distance[i] = -1;
                list[i] = new ArrayList();
            }
            sigma[s] = 1;
            distance[s] = 0;

            Queue<Integer> queue = new LinkedList<Integer>();
            queue.offer(s);
            while( !queue.isEmpty()){
                int v = queue.poll();
                stack.push(v);
                // foreach neighbor of node
                for(int w = 0; w < AdjacentMatrix.getLength(); w++){
                    if(AdjacentMatrix.get(v, w) > 0.5) {//the neighbor
                        // w found for the first time?
                        if(distance[w] < 0){
                            queue.offer(w);
                            distance[w] = distance[v] + 1;
                        }
                        // shortest path to w via v?
                        if( distance[w] == distance[v] + 1){
                            sigma[w] = sigma[w] + sigma[v];
                            list[w].add(v);
                        }
                    }
                }
            }

            double[] delta = new double[AdjacentMatrix.getLength()];
            for(int i = 0; i < AdjacentMatrix.getLength(); i++)
                delta[i] = 0;
            // stack returns vertices in order of non-increasing distance form s
            while( !stack.isEmpty()){
                int w = Integer.class.cast(stack.pop());
                for (int i = 0; i < list[w].size(); i++){
                    int v = Integer.class.cast(list[w].get(i));
                    delta[v] = delta[v] + (double)sigma[v]/sigma[w]*(1.+delta[w]);
                }
                if(w != s){
                    betweenness[w] = betweenness[w] + delta[w];
                }
//        System.out.println(betweenness[w]);
//            System.out.println("---------------");
            }
        }
       // return betweenness;
    }

    public static double get(int node){
        calculate();
        return betweenness[node];
    }
}
