import java.net.*;
import java.io.*;
import java.util.Scanner;
public class urlreq{

    public static void main(String args[]) {

       for (int i=0; i<99; i++) {
	   	  try {
			 	String u = "https://moodle2627.vtc.edu.hk";
			 	httpReq(u, i); 
		  } catch (Exception e) { System.out.println("req error"); }
	   }
    }
	public static void httpReq(String u, int i) throws Exception {
		URL url = new URL(u);
		 HttpURLConnection conn = (HttpURLConnection) url.openConnection();
		 conn.setConnectTimeout(5000);
		 conn.setReadTimeout(5000);
		 conn.setRequestMethod("GET");
		 conn.setRequestProperty("User-Agent", "hk-gov/999");
		 conn.setRequestProperty("X-Forwarded-For", "188.90.98.78, 127.0.0.1");
		 //conn.setRequestProperty("Connection", "keep-alive");
		 //Scanner scan = new Scanner(conn.getInputStream());
		 //while (scan.hasNextLine()) {
		 	//System.out.println(scan.nextLine());
		 //}
		 //scan.close();
		 int status;
		 try {
           status = conn.getResponseCode();
           if (status >= 200 && status < 400) {
              System.out.println("Req time: " + i);
              // 消費輸入流，釋放緩衝，避免socket洩漏
              try(var is = conn.getInputStream()){
                is.readAllBytes();
              }
           } else {
                System.out.println("Request fail " + status);
                // 錯誤狀態碼要讀 errorStream
                try(var es = conn.getErrorStream()){
                   if(es != null) es.readAllBytes();
                 }
           }
        } finally {
          conn.disconnect();
        }
	}
}



