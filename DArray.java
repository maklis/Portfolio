/**
 * =====================================
 * Please complete the remaining operations:
  0. add a default constructor with initial size of 10 - make this default size
     into a constant
  1. add/insert: an element to a given index (reset as necessary), and a method
     to add an element to the back of the array
  2. resize: reset the size of the array as the user insert data pass the 
     maxSize/capacity or they explicitly invoke the operation 
  3. add getFirst/getLast methods to retrieve the corresponding element
  4. Modify the class so it can handle any kind of data type (generic data type
     class)
  5. Make sure the code is fully documented and the file is fully described 
     with appropriate information and algorithms
 * ==================================
 * @author Ken Nguyen
 * @purpose: simple illustration of a dynamic array/vector 
 */
public class DArray {
	private final double GROW_FACTOR = 0.5;// array size growing rate
	
	//attributes
	private int size;
	private int buffer[]; //the actual array
	
   //constructors
   public DArray(int size) throws Exception{
	   if(size < 0){
		   throw new Exception("Not a valid range");
	   }
	   this.size = size;//the actual array size
	   int bufferSize = (int) Math.ceil(this.size + this.size * GROW_FACTOR);
	   this.buffer = new int[bufferSize]; //create the buffer
   }
   
   //methods

   
   /**
    * 
    * @return the actual size of the array
    */
   public int length(){
	   return this.size;
   }
   
   /**
    * 
    * @return the max length of the dynamic array
    */
   public int maxLength(){
	   return this.buffer.length;
   }
   
   /**
    * 
    * @param index - the location of the element in the array
    * @return the element at the given location/index
    */
   public int elementAt(int index) throws Exception{
	   if(index < 0 || index >= this.size)
		   throw new Exception("Index out of bound");
     return this.buffer[index];
   }
   
   
   //////////////////////////////////////////////////////////
   //driver to test the code
   public static void main(String[] args) throws Exception{
	  DArray a = new DArray(-5);
	  System.out.println(a.length());
	  System.out.println(a.maxLength());
	  
	  a.set(0, 10); //set value 10 into index 0
	  a.set(100, 50);//set value 50 to index 100
	  a.resize(2);
	   
   }//end of main

}//end of DArray class
