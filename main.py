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
from kivy.uix.screenmanager import Screen, ScreenManager

from requests import get
from json import loads
from re import search



class ComicStrip(GridLayout):
    def __init__(self, title, alt, num, image_url,**kwargs):
        super(ComicStrip, self).__init__(**kwargs)
        self.title = title
        self.alt = alt
        self.num = num
        self.image_url = image_url

        # self.CenteredAsyncImage.source = self.image_url



class ComicDownloader:
    def __init__(self):
        pass

    def get_strip(self, number):
        info = self.download_json(number)
        if not info:
            print("Error: URL could not be retrieved")
            return
        title, alt, num = info['safe_title'], info['alt'], str(info['num'])
        # image = num+search("\.([a-z])+$", info['img']).group()
        image_url = info['img']
        print(title, '|', alt, '|',num ,'|', image_url)
        return ComicStrip(title, alt, num, image_url)

    def download_json(self, comic_number):
        if comic_number < 0:
            return None
        try:
            if comic_number == 0:
                return get("http://xkcd.com/info.0.json").json()
            else:
                return get("http://xkcd.com/{0}/info.0.json".
                           format(comic_number)).json()
        # except (requests.exceptions.ConnectionError, ValueError):
        #     return None
        except:
            return None




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

class ComicScreen(Screen):
    # def __init__(self, **kwargs):
    #     super(ComicScreen, self).__init__(**kwargs)
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


        dn = ComicDownloader()
        dn.get_strip(1100)

        exp = CenteredAsyncImage(
            source='http://kivy.org/funny-pictures-cat-is-expecting-you.jpg')
        self.layout_bottom.add_widget(exp)

        car = Carousel()
        for x in range(0,10):
            car.add_widget(Page(index=x+1))
        self.layout_bottom.add_widget(car)
        self.init_keyboard()




    def init_keyboard(self):
    #     Widget
    #     self._keyboard = self.request_keyboard(
    #         self._keyboard_closed, self, 'text')
    #     if self._keyboard.widget:
    #         # If it exists, this widget is a VKeyboard object which you can use
    #         # to change the keyboard layout.
    #         pass
    #     self._keyboard.bind(on_key_down=self._on_keyboard_down)
        pass

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        try:
            print('- text :', text)
        except:
            print('cannot print text')
        try:
            print('- modif:', modifiers)
        except:
            print('cannot print modifiers')
        # print(' - text is %r' % text)
        # print(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

    def on_touch(self, *args, **kwargs):
        self.uniforms['touch'] = [float(i) for i in self.touch]

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

