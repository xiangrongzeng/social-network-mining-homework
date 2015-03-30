package centrality;

import centrality.*;

class AllTests {
    static final String NEWLINE = "\n";
    static AdjacentMatrix adjm = new AdjacentMatrix();
    public static void main(String[] args) {
//        testMatrix();
        testDegreeCentrality();
    }
    static void testMatrix(){
        System.out.println(adjm.getLength());
        System.out.println(adjm.getWidth());
        for (int i=0; i<adjm.getLength(); i++) {
            for (int j=0; j<adjm.getWidth(); j++) {
                System.out.println(adjm.get(i,j));
            }
            System.out.println(NEWLINE);
        }
    }

    static void testDegreeCentrality(){
        for (int i = 0; i < DegreeCentrality.calculate().length; i++){
            System.out.println(DegreeCentrality.calculate()[i]);
        }
    }
}
