package centrality;

import centrality.AdjacentMatrix;
import Jama.*;

class EigenvectorCentrality {
    static Matrix adjm = new Matrix(AdjacentMatrix.get());
    static EigenvalueDecomposition evdp = new EigenvalueDecomposition(adjm);
    static int largestValueNumber = 0;

    private static double getLargestEigenvalueNumber(){
        double eigenValues[] = evdp.getRealEigenvalues();
        double largestValue = 0.0;
        for(int i=0; i<AdjacentMatrix.getLength(); i++){
            if (largestValue < eigenValues[i]){
                largestValue = eigenValues[i];
                largestValueNumber = i;
            }
        }
        return largestValue;
    }
    static double[] getRightEigenvector(){
        getLargestEigenvalueNumber();
        Matrix vectors = evdp.getV();
        vectors = vectors.transpose();
        double[][] vector = vectors.getArray();
        return vector[largestValueNumber];
    }

    static double get(int node){
        double[] vector = getRightEigenvector();
        return vector[node];
    }
}
