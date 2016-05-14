#
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
import kivy
kivy.require('1.0.6')
__version__ = '0.0.1'

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

from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.popup import Popup

from kivy.logger import Logger
from kivy.animation import AnimationTransition

# is not working with - python2 in android only
# from requests import get
# from json import loads
# import json
# from re import search
#____________________________________________________

from kivy.storage.dictstore import DictStore
from kivy.storage.jsonstore import JsonStore
from os.path import join

from ComicStrip import CenteredAsyncImage

import ComicDownloader as cd
from linked_list import StripBuffer

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




class Page(GridLayout):

    def __init__(self, index, name='', **kwargs):
        super(Page, self).__init__(**kwargs)
        self.index = index
        if not name:
            self.name = 'page['+str(index)+']'


class Menu(Carousel):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        # Menu.next_slide()

        self.load_next()

class ComicScreen(Screen):
    def __init__(self, **kwargs):
        super(ComicScreen, self).__init__(**kwargs)

        #
        # self.downloader = ComicDownloader()

class ComicStripSlideViewer(Carousel):

    def __init__(self, **kwargs):
        super(ComicStripSlideViewer, self).__init__(**kwargs)
        # self.downloader = self.parent.downloader
        # self.downloader = downloader
        # return
        # self.downloader = ComicDownloader()

        strip_number = 390
        size = 3
        self.downloader = cd.ComicDownloader(self)

        self.sb = StripBuffer(current_id=strip_number, size=size,
                              downloader=self.downloader)
        print(self.sb)

        # print(dir(AnimationTransition))
        a= ['in_back', 'in_bounce', 'in_circ', 'in_cubic', 'in_elastic', 'in_expo',
            'in_out_back', 'in_out_bounce', 'in_out_circ', 'in_out_cubic', 'in_out_elastic',
            'in_out_expo', 'in_out_quad', 'in_out_quart', 'in_out_quint', 'in_out_sine',
            'in_quad', 'in_quart', 'in_quint', 'in_sine', 'linear', 'out_back', 'out_bounce',
            'out_circ', 'out_cubic', 'out_elastic', 'out_expo', 'out_quad', 'out_quart',
            'out_quint', 'out_sine']

        self.anim_type = 'in_expo'
        self.anim_type = 'in_out_quart'

        # x = 50
        # for q in range(x):
        #     print('Called next strip')
        #     sb.next_strip()
        #     print(sb)
        # for q in range(x):
        #     print('Called prev strip')
        #     sb.prev_strip()
        #     print(sb)


    def load_next(self, mode='next', **kwargs):
        super(ComicStripSlideViewer, self).load_next(mode=mode,**kwargs)
        # print('Loading next strip')
        # self.sb.next_strip()
        if mode == 'next':
            print('Loading next strip')
            self.sb.next_strip()
        else:
            print('Loading previous strip')
            self.sb.prev_strip()

    # def load_previous(self, **kwargs):
    #     super(ComicStripSlideViewer, self).load_previous(**kwargs)
    #     print('Loading previous strip')
    #     self.sb.prev_strip()

    def on_sliding_end(self):
        '''
        happens at a time the user slides to a new slide
        = next or previous
        (or after a time interval)
        '''

        # cur = buffer[cur_id]
        self.update_strip_buffer()

        pass
    #
    # def update_strip_buffer(self):
    #     # for strip in self.buffer:
    #     #     if
    #     pass

    def next_strip(self):
        self.load_next()

    def prev_strip(self):
        # self.load_previous()
        self.load_next(mode='prev')

    # def reload_buffer(self):
    #     self.comic_strip_index = self.index
    #     if(self.comic_strip_index+1 == self.buffer_count):
    #         actualize_index = 0
    #     else:
    #         actualize_index = self.comic_strip_index + 1
    #
    #     grid_layout = self.buffer[actualize_index]
    #     strip_number = self.strip_number = self.strip_number+1
    #     # strip_number = grid_layout.children[0].num + 1
    #     grid_layout.clear_widgets()
    #
    #
    #     comic_strip = self.downloader.update_strip(strip_number)
    #     grid_layout.add_widget(comic_strip)



    # def get_slide_container(self, slide):




class RedDwarfQiz(GridLayout):
    # gl_left = ObjectProperty()
    # label_mean_exec_time = StringProperty('??')
    layout_bottom = ObjectProperty()

    def process_it(self, req, results):
        # for key, value in results['weather'][0].items():
        #     print(key, ': ', value)
        Logger.info('%'*42+'here')
        if results is not None:
            Logger.info('%'*42 + 'yes')
            [Logger.info(key) for key in results.keys()]
        else:
            Logger.info('%'*42 +'no')
        key = 'img'
        Logger.info(key + ' : ' + results[key])

        # [print(key) for key in results.keys()]
        # what = 'year'
        # if what in results.keys():
        #     print(results.get(what))
        pass
    #
    #
    #     p = CustomPopup(title = results['safe_title'])
    #     p.open()

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RedDwarfQiz, self).__init__(**kwargs)

        # data_dir = getattr(self, 'user_data_dir') #get a writable path to save the file
        # store = JsonStore(join(data_dir, 'kivy_user.json'))


        # store = JsonStore('kivy_user.json')
        # store.put('score', best=50)

        #
        # dn = ComicDownloader()
        # dn.get_strip(1100)
        
        exp = CenteredAsyncImage(
            source='http://kivy.org/funny-pictures-cat-is-expecting-you.jpg')


        self.layout_bottom.add_widget(exp)



        car = Carousel()
        for x in range(0,10):
            car.add_widget(Page(index=x+1))


        self.layout_bottom.add_widget(car)
        # req = UrlRequest(url, on_success, on_redirect, on_failure, on_error,
        #                  on_progress, req_body, req_headers, chunk_size,
        #                  timeout, method, decode, debug, file_path, ca_file,
        #                  verify)


        # store = JsonStore('http://dynamic.xkcd.com/api-0/jsonp/comic/123')
        # return

        # id = 123
        # url = "http://xkcd.com/{0}/info.0.json".format(id)
        # print(url)
        # p = CustomPopup(title = url)
        #
        # req = UrlRequest(
        #     # 'http://api.openweathermap.org/id/2.5/weather?q=Paris,fr',
        #     url,
        #     self.process_it)
        #
        # p.open()
        # ____________________________________________________
        # store = JsonStore(url)
        # # a = store.get('title')
        # print('here')
        # [print(key) for key in store.keys()]
        # what = 'year'
        # if store.exists(what):
        #     print(store.get(what))

        # a = store.get('num')
        # print(id)

        # return
        # self.init_keyboard()



    #
    # def init_keyboard(self):
    # #     Widget
    # #     self._keyboard = self.request_keyboard(
    # #         self._keyboard_closed, self, 'text')
    # #     if self._keyboard.widget:
    # #         # If it exists, this widget is a VKeyboard object which you can use
    # #         # to change the keyboard layout.
    # #         pass
    # #     self._keyboard.bind(on_key_down=self._on_keyboard_down)
    #     pass
    #
    # def _keyboard_closed(self):
    #     print('My keyboard have been closed!')
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard = None
    #
    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     print('The key', keycode, 'have been pressed')
    #     try:
    #         print('- text :', text)
    #     except:
    #         print('cannot print text')
    #     try:
    #         print('- modif:', modifiers)
    #     except:
    #         print('cannot print modifiers')
    #     # print(' - text is %r' % text)
    #     # print(' - modifiers are %r' % modifiers)
    #
    #     # Keycode is composed of an integer + a string
    #     # If we hit escape, release the keyboard
    #     if keycode[1] == 'escape':
    #         keyboard.release()
    #
    #     # Return True to accept the key. Otherwise, it will be used by
    #     # the system.
    #     return True
    #
    # def on_touch(self, *args, **kwargs):
    #     self.uniforms['touch'] = [float(i) for i in self.touch]


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

# todo: link to explanatory site
# todo: xkcd what if
# todo: stderr > file