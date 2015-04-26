package centrality;

import centrality.AdjacentMatrix;
import centrality.DegreeCentrality;
import Jama.*;
import java.util.*;

class PagerankCentrality{
    static double alpha = 0.3;
    static double beta = 0.3;
    static Matrix adjm = new Matrix(AdjacentMatrix.get());
    static Matrix identityMatrix
        = Matrix.identity(
                AdjacentMatrix.getLength(),
                AdjacentMatrix.getLength());

    static Matrix getNodeDegree(){
        double[][] degrees = new double[AdjacentMatrix.getLength()][AdjacentMatrix.getLength()];
        for (int i = 0; i<AdjacentMatrix.getLength(); i++){
            for(int j = 0; j<AdjacentMatrix.getLength(); j++){
                if(i==j){
                    degrees[i][j] = DegreeCentrality.get(i);
                }else{
                    degrees[i][j] = 0;
                }
            }
        }
        Matrix nodeDegree = new Matrix(degrees);
        return nodeDegree;
    }

    static double[][] getPagerank(){
        Matrix nodeDegree = getNodeDegree();
        Matrix tmp1 = adjm.transpose()
            .times(nodeDegree.inverse());
        Matrix tmp2 = tmp1.times(alpha);
        Matrix tmp3 = identityMatrix.minus(tmp2);
        Matrix tmp4 = tmp3.inverse();
        Matrix tmp5 = tmp4.times(beta);
        return tmp5.getArray();
    }

    static double get(int node){
        double[][] array = getPagerank();
        double centrality = 0;
        for(int i = 0; i < AdjacentMatrix.getLength(); i++){
            centrality += array[node][i];
        }
        return centrality;
    }
}
