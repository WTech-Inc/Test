from wplay import App
from wplay.ui import Text,View,Button
from wplay.ui.color import rgb

app = App()

class ScreenView(View):
    def _render(self, **options):
        return self._render_all(**options)
    def first_page(self):
        label1 = Text(padding=["10px 20px 5px 5px"],text="Hello",color=rgb(255,255,255))
        return self._render(textView=[label1])

app.addView(ScreenView)
app.startLoop()