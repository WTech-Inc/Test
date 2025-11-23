import tryweb

web = tryweb.Connection()
route = tryweb.Router(web)
web.webs.use("@+tryweb/front")

@route.getMapping("/")
def index(req, res):
    return res.reply_with_html("pages/index.html", text="hello")

web.start_listen(port=5000)