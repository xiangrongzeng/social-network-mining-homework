// define the adjacent matrix of the graph in homework2
package centrality;

class AdjacentMatrix {
    private AdjacentMatrix(){}
    private static double[][] adjacentMatrix = {
        {0,1,0,0,0,0,0,0,0,0},
        {1,0,1,0,0,0,0,0,0,0},
        {0,1,0,1,1,1,0,0,0,0},
        {0,0,1,0,1,1,0,0,0,0},
        {0,0,1,1,0,1,0,0,0,0},
        {0,0,1,1,1,0,1,0,0,0},
        {0,0,0,0,0,1,0,1,1,0},
        {0,0,0,0,0,0,1,0,1,1},
        {0,0,0,0,0,0,1,1,0,1},
        {0,0,0,0,0,0,0,1,1,0}};

    // for @Test
//    private static double[][] adjacentMatrix = {
//        {0,1,0,0,0},
//        {1,0,1,1,0},
//        {0,1,0,0,1},
//        {0,1,0,0,1},
//        {0,0,1,1,0}};

    public static double[][] get() {
        return adjacentMatrix;
    }

    public static double get(int i, int j){
        return adjacentMatrix[i][j];
    }

    public static int getLength(){
        return adjacentMatrix.length;
    }

    public static int getWidth(){
        return adjacentMatrix[0].length;
    }
}
