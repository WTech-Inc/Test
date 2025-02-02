from wplay import App
from wplay.ui import Text,View,Button
from wplay.ui.color import rgb
from wplay.ui.messageBox import Message

app = App()

class ScreenView(View):
    def _render(self, **options):
        return self._render_all(**options)
    def first_page(self):
        label1 = Text(padding=["10px","20px", "5px", "5px"],text="Hello",color=rgb(255,255,255))
        btn = Button(padding=["15px","25px"],text="click me",bgColor=rgb(0,0,0),color=rgb(255,255,255),onClick=self.handleClick)
        return self._render(textView=[label1,btn])
    @staticmethod
    def handleClick(self):
        msg = Message(title="Hi",content="you clicked me",type="alert")
        return msg.active()

app.addView(ScreenView)
app.startLoop()