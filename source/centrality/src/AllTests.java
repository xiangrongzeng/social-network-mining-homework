package centrality;

import centrality.*;

class AllTests {
    static final String NEWLINE = "\r\n";
    public static void main(String[] args) {
//        testMatrix();
        testDegreeCentrality();
        testEigenvectorCentrality();
        testKatzCentrality();
        testPagerankCentrality();
//        testGraph();
        testClosenessCentrality();
        testBetweennessCentrality();
    }

    static void testMatrix(){
        System.out.println(AdjacentMatrix.getLength());
        System.out.println(AdjacentMatrix.getWidth());
        for (int i=0; i<AdjacentMatrix.getLength(); i++) {
            for (int j=0; j<AdjacentMatrix.getWidth(); j++) {
                System.out.println(AdjacentMatrix.get(i,j));
            }
            System.out.println(NEWLINE);
        }
    }

    static void testDegreeCentrality(){
        System.out.println("-------------------------------------");
        System.out.println("DegreeCentrality");
        for (int node = 0; node <AdjacentMatrix.getLength(); node++){
            System.out.println(DegreeCentrality.get(node));
        }
    }

    static void testEigenvectorCentrality(){
        System.out.println("-------------------------------------");
        System.out.println("EigenvectorCentrality");
        for (int node = 0; node <AdjacentMatrix.getLength(); node++){
            System.out.println(EigenvectorCentrality.get(node));
        }
    }

    static void testKatzCentrality(){
        System.out.println("-------------------------------------");
        System.out.println("KatzCentrality");
        for (int node = 0; node <AdjacentMatrix.getLength(); node++){
            System.out.println(KatzCentrality.get(node));
        }
    }

    static void testPagerankCentrality(){
        System.out.println("-------------------------------------");
        System.out.println("PagerankCentrality");
        for(int node = 0; node < AdjacentMatrix.getLength(); node++){
            System.out.println(PagerankCentrality.get(node));
        }
    }

    static void testGraph(){
        System.out.println(Graph.getNumberOfVertexes());
            System.out.println(Graph.get().toString());
    }

    static void testClosenessCentrality(){
        System.out.println("-------------------------------------");
        System.out.println("ClosenessCentrality");
        for (int node = 0; node < Graph.getNumberOfVertexes(); node++){
            System.out.println(ClosenessCentrality.get(node));
        }
    }

    static void testBetweennessCentrality(){
        System.out.println("-------------------------------------");
        System.out.println("BetweennessCentrality");
        for(int node = 0; node < AdjacentMatrix.getLength(); node++){
            System.out.println(BetweennessCentrality.get(node));
        }
    }
}
