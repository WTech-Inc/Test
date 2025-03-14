// apt install wnet

// wnet install -s https://game.dev.wtech.net/source/gameDev.zip
// wnet open -f zip -s gameDev.zip
// cd gameDev

import com.wtech.gamedev.*;

public class Game {
  public static void main(String[] args) {
     GameManager gm = new GameManager("ccc.5677");
     SceneManager scene = new SceneManager(gm);
     gm._install();
     start_screen();
     int status_code = gm.wait_for_screen();
     if (status_code == 200) {
        start_game();
     }
  }
  public static void start_screen() {
     gm.action(gm.screen.open());
  }
  public static void start_game() {
     if (scene.find("sceneOne")) {
     gm.screen.set("window-width",500);
     gm.screen.set("window-height",300);
     gm.screen.set("background-color",gm.colors.rgb(0,0,0));
     //gm.screen.add(type,postions,color)
     gm.screen.add("object",gm.positions.vector3(5,5,5),gm.colors.rgb(255,255,255));
     gm.screen.add_all();
     gm.start_loop();
    }
    scene.create("sceneOne");
    start_game();
  }
}