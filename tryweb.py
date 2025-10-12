from tryweb import Controller
from tryweb.apps import basicServer
from tryweb.views import Views
from tryweb.pages import FontManager
from tryweb.pages.colors import rgb
from tryweb.complier import tryCode
from trydb import DataBase

server = basicServer()
con = Controller(server=server)
views = Views(con)
db = con.use("trydb", DataBase("sqlite:///users.db"))

class index_page_view(views):
    __viewname__ = "index page"
    @head
    def _head(title, meta):
        title = "主頁"
        meta.set_charset("UTF-8")
    @body
    def _body(writer):
        writer(FontManager(type="h2", text="Hello", color=rgb(0,0,0)))
        writer(tryCode=tryCode("using web.front -> nextLine", con))
        writer(tryCode=tryCode("using web.front -> new-font='passage-text',color='RED' -> value='你好，這是html p tag的文字'", con))
        writer(tryCode=tryCode("using web.front -> nextLine", con))

@con.on_route("/")
def index(req, res):
    return res.reply(view=views.find(name="index page"))

server.run()