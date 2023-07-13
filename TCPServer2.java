import java.io.*; 
import java.net.*; 

class TCPServer2{ 

    public static void main(String argv[]) throws Exception{ 
        String clientSentence; 
        String capitalizedSentence;
        try{ 
        //server is listening on port 6789
        ServerSocket welcomeSocket = new ServerSocket(6789); 
  
        // loop for getting client request
        while(true){ 
  
           Socket connectionSocket = welcomeSocket.accept();
           //create new thread
           clientServerThread t = new clientServerThread(connectionSocket/*, inFromClient, outToClient*/);
           t.start();
           
      } 
     }catch (Exception e){
         cconnectionSocket.close();
         e.printStackTrace();
      }
  } 
} 

class clientServerThread extends Thread {
   Socket connectionSocket;
   clientServerThread(Socket otherSocket){
   connectionSocket = otherSocket;
   }
  public void run(){
  try{
  //BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream())); 
           
           //creating input and output streams
	        DataInputStream inFromClient = new DataInputStream(connectionSocket.getInputStream());
           DataOutputStream  outToClient = new DataOutputStream(connectionSocket.getOutputStream()); 
           String clientSentence; 
           String capitalizedSentence;
           String serverSentence;
           
           while(!clientSentence.equals("END")){
           // capitailize the sentence from Client
           clientSentence = inFromClient.readLine(); 
           capitalizedSentence = clientSentence.toUpperCase() + '\n'+'\n'; 
           outToClient.writeBytes(capitalizedSentence);
           serverSentence = capitalizedSentence.readline(); //MODIFIED SENTENCE
           System.out.println(serverSentence);
           }
            inFromClient.close();
            outToClient.close();
            connectionSocket();
  }catch (Exception e){
  System.out.println(e);
    }
   }  
}
