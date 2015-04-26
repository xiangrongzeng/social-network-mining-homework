package centrality;

import centrality.AdjacentMatrix;

class DegreeCentrality {

    static int get(int node){
        int centralitie = 0;
        for (int j=0; j<AdjacentMatrix.getLength(); j++) {
            centralitie += AdjacentMatrix.get(node, j);
        }
        return centralitie;
    }
}
