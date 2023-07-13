import java.util.Arrays;
import java.util.Collections; 
import java.util.Random;
public class HW5Normal {    
   
     private static int computeSum(int arr[], int n) {
 
         //base or terminating condition
         if (n <= 0) {
            return 0;
          }
 
          //Calling method recursively
          return computeSum(arr, n-1 ) + arr[n-1];
       }
   
    public static void main(String[] args) {        
        Random rd = new Random();
        //define original array     
        int [] intArray = new int [] {57,340,132,576,102,827,52,983,34,7};     
        int temp = 0;    
 
        //print original array    
       System.out.println("Original array: ");    
       for (int i = 0; i <intArray.length; i++) {     
           System.out.print(intArray[i] + " ");    
        }    
        
        //Print the sum
        int sum = computeSum(intArray, intArray.length);
        System.out.println("\n\nRecursive Sum: ");
        System.out.println(sum);
        
        //Sort the array in ascending order using two for loops    
        for (int i = 0; i <intArray.length; i++) {     
          for (int j = i+1; j <intArray.length; j++) {     
              if(intArray[i] >intArray[j]) {      //swap elements if not in order
                 temp = intArray[i];    
                 intArray[i] = intArray[j];    
                 intArray[j] = temp;    
               }     
            }     
        }    
        //print sorted array    
        System.out.println("\nArray sorted: ");    
        for (int i = 0; i <intArray.length; i++) {     
            System.out.print(intArray[i] + " ");    
        }    
    }    
}   