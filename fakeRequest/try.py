import tryweb

web = tryweb.Connection()
route = tryweb.Router(web)
web.webs.use("@+tryweb/front")

@route.getMapping("/")
def index(req, res):
    return res.reply_with_html("pages/index.html", text="hello")

web.start_listen(port=5000)

# index.html
"""
<!DOCTYPE HTML>
<html>
  <head>
    <title>測試頁面 -- index.html</title>
    <meta charset="UTF-8" />
  </head>
  <body>
     {% using tryweb.front -> pageCenter %}
     {% using tryweb.front -> nextLine %}
     {% using tryweb.front -> nextLine %}
     The text is : {% call tryweb.page_var("text") %}
  </body>
</html>
"""