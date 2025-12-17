import com.wtech.calEasy.stockModel;
import com.wtech.calEasy.stock.*;

public class stockJava {
  public static void main(String[] args) {
     stockModel model = new stockModel(apiKey="xxxx")
                          .agreeEULA(true)
                          .setIntent("all-true")
                           .setTarget("stock-hk")
                           .build();
      Stock stock = model.find("0005.HK");
      int[][] results = model.anys(intent="stock-suitable-buying", target=stock);
      int[] result = new int[100];
      for (int i = 0; i < results.length; i++) {
          for (int j = 0; i < results[i].length; j++) {
             if (results[i][j] == 1) {
                result[i] = results[i][j];
             }
          }
      }
  }
}