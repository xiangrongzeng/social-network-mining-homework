package centrality;

import centrality.AdjacentMatrix;

class DegreeCentrality {

    static int[] calculate(){
        AdjacentMatrix adjm = new AdjacentMatrix();
        int[] centralities = {0,0,0,0,0,0,0,0,0,0};
        for (int node=0; node<adjm.getLength(); node++){
            for (int j=0; j<adjm.getWidth(); j++) {
                centralities[node] += adjm.get(node, j);
            }
        }
        return centralities;
    }
}
