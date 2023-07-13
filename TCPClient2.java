import java.io.*; 
import java.net.*; 

class TCPClient2{ 

    public static void main(String argv[]) throws Exception{ 
      try{
        //BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in)); 

        //Socket clientSocket = new Socket("10.35.4.143", 6789); 
        Socket clientSocket = new Socket("127.0.0.1", 6789); 
        DataInputStream inFromUser = new DataInputStream(clientSocket.getInputSteam());
        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream()); 
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
	     BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream())); 
        String clientSentence;
        String capitalizedSentence;
        String serverSentence;
        while(!clientSentence.equals("END")){
        System.out.println("Please enter sentence to send to server: ");
        clientSentence = inFromUser.readLine(); 
        outToServer.writeBytes(clientSentence + '\n'); 
        capitalizedSentence = inFromServer.readLine();
        serverSentence = capitalizedSentence;
        System.out.println("FROM SERVER: " + serverSentence); 
        clientSocket.close();
        }
        inFromUser.close();
        outToServer.close();
        clientSocket.close();
       }catch (Exception e){
       System.out.println(e);
       }           
   } 
} 

