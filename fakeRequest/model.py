
supportLang = ["py","nodeJS"]
pyWords = {
  "print":"print()",
  "condition":["if","elif",else"]
}

class Brain:
    def __init__(self,prompt):
        self.input = prompt
        self.coding = False
        self.output = ""
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
            pass
        elif lang == "nodeJS":
            pass
    def outputLayer(self):
        pass