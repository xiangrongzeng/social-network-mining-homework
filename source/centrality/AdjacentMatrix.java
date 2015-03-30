// define the adjacent matrix of the graph in homework2
package centrality;

class AdjacentMatrix {
    private int[][] adjacentMatrix = {
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

    int[][] get() {
        return adjacentMatrix;
    }

    int get(int i, int j){
        return adjacentMatrix[i][j];
    }

    int getLength(){
        return adjacentMatrix.length;
    }

    int getWidth(){
        return adjacentMatrix[0].length;
    }
}
