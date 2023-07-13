public class HW2{
   public static void main(String[] args){
      
      double[][] queryP = {{1.0,1.0,0.4,0.0},
                           {0.0,0.4,0.7,1.0},
                           {0.0,1.0,1.0,0.0}};
                                    
      double[][] UpdateP = {{0.6,0.4,0.0,0.0},
                            {0.0,0.0,0.4,0.6},
                            {0.0,0.5,0.5,0.0}};
      double[] queryCost = {1.0,1.0,1.3};
      int Fragments = 3;
      double[] updateCost = {1.2,1.5,2.0};
      int Sites = 4;
      
      for(int i=0; i < Fragments; i++){
         System.out.println("Optimal allocation for fragment " +i);
         
         
         int[] optimalReplication = new int[Sites];
         for (int j=0; j < Sites; j++){
            optimalReplication[j] = 0;
         }
         
         double expectedCost = 0;
         for (int j = 0; j < Sites; j++){
            expectedCost += queryCost[i] * queryP[i][j] +
                            updateCost[i] * UpdateP[i][j];
         }
         
         double minCost = Double.MAX_VALUE;
         for (int j=0; j < Sites; j++){
            double tempCost = 0;
            for (int k = 0; k < Sites; k++){
               tempCost += queryCost[i] * queryP[i][k] +
                           updateCost[i] * UpdateP[i][k];
            }

               optimalReplication[j] = 1;

        }
        System.out.println("Expected Cost = " + expectedCost);
        System.out.println("Optimal Replication is = " + minCost);

      } 
      System.out.println("Number of sites: " + Sites);
      System.out.println("Number of fragments: " + Fragments);
   }
}