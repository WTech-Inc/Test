const wnet = require("wnet");

const app = wnet.https.Controller();
app.use("@+/trydb", { url: "tb://test-tb.wtech.com" });

app.mapping("GET", "/", (req,res) => {
  return res.reply("./index.html", code=200, type="text/html");
});

app.listen((host, port) => {
  host = "localhost";
  port = 5000;
  console.log("伺服器正在聆聽第5000號port");
})

wnet.startListen(app, protocol="http");