
import junit.framework.TestCase;


public class SilhouetteTest extends TestCase{
    Silhouette silhouette = new Silhouette();
    public void testWithinAverageDistance(){
        assertEquals(25.0, silhouette.getWithinAverageDistance(0,0));
    }

    public void testDistanceWithOtherCluster(){
        assertEquals(312.5, silhouette.getDistanceWithOtherCluster(0,0));

    }

    public void testCalc(){
        assertEquals( 0.88,silhouette.calc() );
    }
}
