from wnet import App
from wnet.https import Controller, Response

app = App(apiKey="key", httpsSSL=True)
con = Controller(app, host="127.0.0.1", port=5000)

@con.route("/")
def index(req):
    return Response("Hello", code=200)

app.add_threads([con])
app.run()