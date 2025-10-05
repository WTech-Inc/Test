import com.wtech.trydb.TryDB;
import com.wtech.trydb.complier.Controller;

public class trydb {
  public static void main(String args[]) {
    try {
      TryDB db = new TryDB("sqlite:///users.db");
      Controller statement = new Controller("create table user -> ('id', 'Integer'), ('name', 'String')", db);
      System.out.println(statement.getResult()["msg"]);
    } catch (Exception err) { System.out.println(err.getMessage()); }
  }
}