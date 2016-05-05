#
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'


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

from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel


class Page(GridLayout):

    def __init__(self, index, name='', **kwargs):
        super(Page, self).__init__(**kwargs)
        self.index = index
        if not name:
            self.name = 'page['+str(index)+']'


class CenteredAsyncImage(AsyncImage):
    pass

class Menu(Carousel):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

class ComicOutlineFrame(GridLayout):
    # def __init__(self, **kwargs):
    #     super(ComicOutlineFrame, self).__init__(**kwargs)
    pass

class ComicStripSlideViewer(Carousel):
    # def __init__(self, **kwargs):
    #     super(ComicSlideViewer, self).__init__(**kwargs)
    pass

class RedDwarfQiz(GridLayout):
    gl_left = ObjectProperty()
    label_mean_exec_time = StringProperty('??')
    layout_bottom = ObjectProperty()

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RedDwarfQiz, self).__init__(**kwargs)


        exp = CenteredAsyncImage(
            source='http://kivy.org/funny-pictures-cat-is-expecting-you.jpg')
        self.layout_bottom.add_widget(exp)

        car = Carousel()
        for x in range(0,10):
            car.add_widget(Page(index=x+1))
        self.layout_bottom.add_widget(car)


class RedDwarfQizApp(App):
    def build(self):
        # Config.set('graphics', 'multisamples', 0) # to correct bug from kivy 1.9.1 - https://github.com/kivy/kivy/issues/3576
        # Config.write()
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


        # Config.set('graphics', 'fullscreen', 'fake')
        # Config.set('graphics', 'fullscreen', 1)

        self.root = root = RedDwarfQiz()


        return root
    def on_stop(self):
        pass

if __name__ == '__main__':
    RedDwarfQizApp().run()
    # comment

# todo: slide navigation and screens
# todo: logo
# todo: markup language
# todo: xml loading for language extension
# todo: xml loading for individual questions and answers

