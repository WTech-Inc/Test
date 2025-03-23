from wnet import App
from wnet.https import Controller, Response, jsonify, render

app = App(apiKey="key", httpsSSL=True)
con = Controller(app, host="127.0.0.1", port=5000, usingDatabase=True)
con.config("dataurl","psql-url")

@con.route("/")
def index(req):
    return Response("Hello", code=200)

@con.route("/login")
def login(req):
    if req.method == "GET":
        return render("index.html")
    username = req.form.get("username")
    pw = req.form.get("pw")
    users = con.db.session.query("select * from users where username=(%s)", (username)).fetchone()
    if users:
        if pw == users["password"]:
            return Response("Login success", code=200)
    return Response(jsonify({"msg":"Users not found"}), code=404)
    

app.add_threads([con])
app.run()