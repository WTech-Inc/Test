from tryweb import Controller
from tryweb.apps import basicServer
from tryweb.views import Views
from tryweb.pages import FontManager
from tryweb.pages.colors import rgb

server = basicServer()
con = Controller(server=server)
views = Views(con)

class index_page_view(views):
    __viewname__ = "index page"
    @head
    def _head(title, meta):
        title = "主頁"
        meta.set_charset("UTF-8")
    @body
    def _body(writer):
        writer(FontManager(type="h2", text="Hello", color=rgb(0,0,0)))
    

@con.on_route("/")
def index(req, res):
    return views.find(name="index page")

server.run()