from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, ListProperty

#from gradient4kivy import GLGradient  # ← your class from earlier
from gradient4kivy.gradient import GLGradient

KV = '''
<GradientLabel>:
    canvas.before:
        Rectangle:
            size: self.size
            pos: self.pos
            texture: self.texture_bg

<MyGrid>:
    cols: 2
    spacing: dp(10)
    padding: dp(10)
    canvas.before:
        Color:
            rgba:[1,1,1,1]
        Rectangle:
            pos:self.pos
            size:self.size

    GradientLabel:
        text: 'Vertical'

    GradientLabel:
        text: 'Horizontal'

    GradientLabel:
        text: 'Diagonal'

    GradientLabel:
        text: 'Reverse Diagonal'

    GradientLabel:
        text: 'Radial'

    GradientLabel:
        text: 'Diamond'

    GradientLabel:
        text: '4-Corner'

    GradientLabel:
        text: 'Sweep'
'''

class GradientLabel(Label):
    texture_bg = ObjectProperty(None)

class MyGrid(GridLayout):
    textures = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, *args):
        size = (256, 256)  # Adjust as needed
        self.textures = [
            GLGradient.vertical(top_color=(1, 0, 0, 1), bottom_color=(0, 0, 1, 1), size=size),
            GLGradient.horizontal(left_color=(0, 1, 0, 1), right_color=(0, 0, 1, 1), size=size),
            GLGradient.diagonal(start_color=(0, 1, 0, 1), end_color=(1, 0, 1, 1), size=size),
            GLGradient.reverse_diagonal(start_color=(1, 0.5, 0, 1), end_color=(0, 0.5, 1, 0.1), size=size),
            GLGradient.radial(center_color=(1, 0, 0, 1), border_color=(0, 1, 0, 1), size=size),
            GLGradient.diamond(start_color=(1, 0, 0.5, 1), end_color=(0, 1, 0.5, 1), size=size),
            GLGradient.corner(
                tl=(1.0, 0.0, 0.0, 1.0),
                tr=(0.0, 1.0, 0.0, 1.0),
                bl=(0.0, 0.0, 1.0, 1.0),
                br=(1.0, 1.0, 0.0, 1.0),
                size=size
            ),
            GLGradient.sweep(size=size)
        ]

        for widget, tex in zip(reversed(self.children), self.textures):
            widget.texture_bg = tex

class TestApp(App):
    def build(self):
        Builder.load_string(KV)
        return MyGrid()

if __name__ == '__main__':
    TestApp().run()

