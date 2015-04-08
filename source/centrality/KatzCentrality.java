package centrality;

import centrality.AdjacentMatrix;
import Jama.*;

class KatzCentrality {
    static final double alpha = 0.25;
    static final double beta = 0.2;

    static Matrix adjm = new Matrix(AdjacentMatrix.get());
    static Matrix identityMatrix
        = Matrix.identity(
                AdjacentMatrix.getLength(),
                AdjacentMatrix.getLength());

    static double[][] getKatz(){
        Matrix tmp = identityMatrix.minus(adjm.transpose().times(alpha));
        tmp = tmp.inverse().times(beta);
        return tmp.getArray();
    }

    static double get(int node){
        double[][] katz = getKatz();
        double centrality = 0;
        for(int i = 0; i < AdjacentMatrix.getLength(); i++){
            centrality += katz[node][i];
        }
        return centrality;
    }
}
