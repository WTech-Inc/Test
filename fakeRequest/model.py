
supportLang = ["py","nodeJS"]
pyWords = {
  "print":"print(.)",
  "symbols":["=","==",">=","(.)","!="],
  "dataType":["str","int","float","bool"],
  "condition":["if","elif","else"],
  "loop":["while","for","in","range"],
  "error":["try","except"],
  "class":["class"],
  "functions":["def","@"],
  "import":["from","import"]
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
          if 'print' in self.prompt:
            self.output = f'''
            {pyWords["print"].split(".")[0]}放你想打印的東西{pyWords["print"].split(".")[1]}
            '''
          elif 'for' in self.prompt:
            self.output = f'''
            # range() 函數：
            # return a list for 用戶輸入
            # 參數：
            # 1: start -- 由什麼數值開始
            # 2: end -- 什麼數值停止（一定要end的數值+1。例子：如果我想在10停止，就要end=11。)
            # 3: step (可選參數)-- 步長 （即你想每一個數值中間隔距如何，預設是1)
            {pyWords["loop"][1]} i {pyWords["loop"][2]} {pyWords["loop"][3]}{pyWords["symbols"][3].split(".")[0]}0,11,1{pyWords["symbols"][3].split(".")[1]}:
              {pyWords["print"].split(".")[0]}i{pyWords["print"].split(".")[1]}
            '''
          elif '函數' in self.prompt:
            pass
            return self.outputLayer()
        elif lang == "nodeJS":
          pass
    def outputLayer(self):
        print(self.output)