
import junit.framework.*;

public class AllTests{
    public static TestSuite suite(){
        TestSuite suite = new TestSuite();
        suite.addTestSuite(SilhouetteTest.class);
        return suite;
    }
}
