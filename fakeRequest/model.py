
supportLang = ["py","nodeJS"]
pyWords = {
  "print":"print()",
  "symbols":["=","==",">=","()","!="],
  "dataType":["str","int","float","bool"],
  "condition":["if","elif","else"],
  "loop":["while","for","in","range"],
  "error":["try","except"],
  "class":["class"],
  "functions":["def","@"],
  "import":["from","import"],
  "webModules":["flask"]
}

class Brain:
    def __init__(self,prompt):
        self.input = prompt
        self.coding = False
        self.output = None
        return self.inputLayer()
    def inputLayer(self):
        self.prompt = self.input.strip()
        return self.thinkingLayer()
    def thinkingLayer(self):
        if "Code" in self.prompt:
            self.coding = True
        if self.coding:
            for lang in supportLang:
                if lang in self.prompt:
                    if lang == "py":
                        return self.deepThinkLayer(lang)
                    elif lang == "nodeJS":
                        return self.deepThinkLayer(lang)
                    
    def deepThinkLayer(self, lang):
        if lang == "py":
          if "web" in self.prompt:
            self.output = f'''
            {pyWords["import"][0]} {pyWords["webModules"][0]} {pyWords["import"][1]} *
            app {pyWords["symbols"][0]} Flask("app")
            {pyWords["functions"][1]}app.route("/")
            {pyWords["functions"][0]} index{pyWords["symbols"][3]}:
              return "Hi"
              
            app.run()
            '''
            return self.outputLayer()
        elif lang == "nodeJS":
          pass
    def outputLayer(self):
        print(self.output)