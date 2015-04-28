
class Silhouette{
    double[][] clusters = {{-10,-5},{5,10}};
    double[] clustersCenter={-7.5,7.5};

    public double calc(){
        double silouetteSum = 0;
        int totalNumber = 0;
        for(int clusterNumber = 0; clusterNumber<clusters.length; clusterNumber++){
            for( int instanceNumber = 0; instanceNumber < clusters[clusterNumber].length; instanceNumber++){
                double withinDistance = getWithinAverageDistance(instanceNumber, clusterNumber);
                double distanceWithOtherCluster = getDistanceWithOtherCluster(instanceNumber, clusterNumber);
                double s = (distanceWithOtherCluster-withinDistance)/max(distanceWithOtherCluster, withinDistance);
                silouetteSum += s;
                totalNumber++;
            }
        }
        double coefficient = silouetteSum/totalNumber;
        return coefficient;
    }
    double max(double a, double b){
        if (a > b)
            return a;
        return b;
    }
    double getWithinAverageDistance(int instanceNumber, int clusterNumber){
        double[] cluster = clusters[clusterNumber];
        double sum = 0;
        for(int i = 0; i < cluster.length; i++){
            sum += (cluster[i]-cluster[instanceNumber])*(cluster[i]-cluster[instanceNumber]);
        }
        return sum/(cluster.length - 1);
    }

    double getDistanceWithOtherCluster(int instanceNumber, int clusterNumber){

        double minDistance = Double.MAX_VALUE;
        for (int i=0; i<clusters.length; i++){
            if ( i != clusterNumber){
                double[] cluster = clusters[i];
                double sum = 0;
                for (int j=0; j<cluster.length; j++){
                    sum += (cluster[j] - clusters[clusterNumber][instanceNumber])*(cluster[j] - clusters[clusterNumber][instanceNumber]);
                }
                double distance = sum/cluster.length;
                if(distance < minDistance){
                    minDistance = distance;
                }
            }
        }
        return minDistance;
    }
}

