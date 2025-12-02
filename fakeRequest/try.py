import tryweb

web = tryweb.Connection()
route = tryweb.Router(web)
web.webs.use("@+tryweb/front")
web.webs.use("@+tryweb/db")

db = tryweb.DataBase(url="sqlite:///test.db")

@route.getMapping("/")
def index(req, res):
    return res.reply_with_html("pages/index.html", text="hello")

@route.GetMapping("/get/products")
def get_products(req, res):
  results, err = db.sql.execute("select * from product")
  if err or err != None: return res.reply_with_text(err.toMessage())
  for result in results:
    name = result["name"]
    price = result["price"]
    return res.reply_with_xml(f"""
    <?xml version='1.0' encoding='UTF-8'>
      <products>
        <product name="{name}" price="{price}" />
      </products>
    </?xml>
  """)

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