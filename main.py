from kivy.app import App
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture

from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
# from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.config import Config

class RedDwarfQiz(GridLayout):
    gl_left = ObjectProperty()
    label_mean_exec_time = StringProperty('??')

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RedDwarfQiz, self).__init__(**kwargs)

class RedDwarfQizApp(App):
    def build(self):
        # root.bind(size=self._update_rect, pos=self._update_rect)
        h = 500
        w = 300
        Config.set('kivy', 'show_fps', 1)
        Config.set('kivy', 'desktop', 1)

        # Config.set('graphics', 'window_state', 'maximized')
        Config.set('graphics', 'position', 'custom')
        Config.set('graphics', 'height', h)
        Config.set('graphics', 'width', w)
        Config.set('graphics', 'top', 15)
        Config.set('graphics', 'left', 4)
        Config.set('graphics', 'multisamples', 0) # to correct bug from kivy 1.9.1 - https://github.com/kivy/kivy/issues/3576

        # Config.set('graphics', 'fullscreen', 'fake')
        # Config.set('graphics', 'fullscreen', 1)

        self.root = root = RedDwarfQiz()
        return root
    def on_stop(self):
        pass

if __name__ == '__main__':
    RedDwarfQizApp().run()
    # comment


