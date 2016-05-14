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

from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen, ScreenManager

# from kivy.uix.popup import Popup

# is not working with - python2 in android only
# from requests import get
# from json import loads
# import json
# from re import search
#____________________________________________________

from kivy.storage.dictstore import DictStore
from kivy.storage.jsonstore import JsonStore
from os.path import join

# from kivy.network.urlrequest import UrlRequest

# web scrapping inspiration from https://github.com/1995eaton/xkcd_downloader/blob/master/xkcd_downloader.py
import time
import sys

# class CustomPopup(Popup):
#     pass

class ComicDownloader:
    def __init__(self):
        self.comic_name = 'xkcd'
        pass

    def get_strip(self, number):

        title = 'Nightmares'
        alt = 'you dont sleep'
        num = 666
        image_url = 'http://imgs.xkcd.com/comics/keeping_time.png'

        return ComicStrip(title, alt, int(num), image_url)


        print('Trying to get the [{}] comic number [{}]'.format(self.comic_name, number))
        info = self.download_json(number)
        print(info)



        # return
        if info is None:
            print("Error: URL could not be retrieved")
            return self.get_strip(number+1)
        try:
            # print('here')
            title, alt, num = (info['safe_title'], info['alt'], str(info['num']))
            # image = num+search("\.([a-z])+$", info['img']).group()
            image_url = info['img']
            print(title, '|', alt, '|', num ,'|', image_url)
            # print(info)
            # print('here')
            a = ComicStrip(title, alt, int(num), image_url)
            return a
            # print('here2')
        # except AssertionError as ex:
        #     # print("AssertionError ({0}): {1}".format(ex.errno, ex.strerror))
        #     return self.get_strip(number+1)
        except Exception as ex:
            # print("Error({0}): {1}".format(ex.errno, ex.strerror))
            print('Exception:', sys.exc_info()[0])
            print('Could not get the [{}] comic number [{}]!'.format
                  (self.comic_name, number))

            time.sleep(5)
            return self.get_strip(number+1)

    def download_json(self, comic_number):
        return 'nan'
        # return get("http://xkcd.com/info.0.json")

    def download_json_python3(self, comic_number):
        return
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
        except Exception:
            print(Exception.args)
            return self.download_json(comic_number+1)




class Page(GridLayout):

    def __init__(self, index, name='', **kwargs):
        super(Page, self).__init__(**kwargs)
        self.index = index
        if not name:
            self.name = 'page['+str(index)+']'


class Menu(Carousel):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

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
        self.downloader = ComicDownloader()
        # if not self.buffer_count:
        self.buffer_count = 3
        self.buffer_half_count = int(self.buffer_count/2)

        self.buffer = []

        buffer_count_range = range(self.buffer_count)

        self.strip_number = 403
        self.strip_number = 390

        index_range = [self.strip_number + index - self.buffer_half_count
                       for index in buffer_count_range]

        def shift(l, n):
            return l[n:] + l[:n]

        strip_number_range = shift(index_range, self.buffer_half_count)


        # time.sleep(2)
        # for q in buffer_count_range:
        #     item = GridLayout(cols=1)
        #     self.buffer.append(item)
        #     self.add_widget(item)

        for (buffer_index, strip_number) in zip(buffer_count_range, strip_number_range):

            comic_strip = self.downloader.get_strip(strip_number)
            grid_layout = GridLayout(cols=1)
            grid_layout.add_widget(comic_strip)

            self.buffer.append(grid_layout)
            self.add_widget(grid_layout)


        # print(self.buffer)
        self.comic_strip_index = 0
        # self.last_comic_strip_index = 0

    def load_next(self, mode='next', **kwargs):
        super(ComicStripSlideViewer, self).load_next(**kwargs)
        # self.next_strip()
        print('loading next')
        self.reload_buffer()

    def next_strip(self):
        self.load_next()

    def reload_buffer(self):
        self.comic_strip_index = self.index
        if(self.comic_strip_index+1 == self.buffer_count):
            actualize_index = 0
        else:
            actualize_index = self.comic_strip_index + 1

        grid_layout = self.buffer[actualize_index]
        strip_number = self.strip_number = self.strip_number+1
        # strip_number = grid_layout.children[0].num + 1
        grid_layout.clear_widgets()


        comic_strip = self.downloader.get_strip(strip_number)
        grid_layout.add_widget(comic_strip)



    # def get_slide_container(self, slide):

class ComicStrip(GridLayout):
    def __init__(self, title, alt, num, image_url, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        self.title = title
        self.alt = alt
        self.num = num
        self.image_url = image_url
        # print('hereeres')

        im = CenteredAsyncImage(source = self.image_url)
        # im = CenteredAsyncImage(source = 'http://kivy.org/funny-pictures-cat-is-expecting-you.jpg')
        self.add_widget(im)

    # pass

class CenteredAsyncImage(AsyncImage):
    pass


class RedDwarfQiz(GridLayout):
    # gl_left = ObjectProperty()
    # label_mean_exec_time = StringProperty('??')
    layout_bottom = ObjectProperty()

    def process_it(self, req, results):
        # for key, value in results['weather'][0].items():
        #     print(key, ': ', value)
        print('here')
        [print(key) for key in results.keys()]
        what = 'year'
        if what in results.keys():
            print(results.get(what))


        p = CustomPopup(title = results['safe_title'])
        p.open()

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RedDwarfQiz, self).__init__(**kwargs)

        # data_dir = getattr(self, 'user_data_dir') #get a writable path to save the file
        # store = JsonStore(join(data_dir, 'kivy_user.json'))
        store = JsonStore('kivy_user.json')

        store.put('score', best=50)

        #
        # dn = ComicDownloader()
        # dn.get_strip(1100)
        
        exp = CenteredAsyncImage(
            source='http://kivy.org/funny-pictures-cat-is-expecting-you.jpg')


        # req = UrlRequest(url, on_success, on_redirect, on_failure, on_error,
        #                  on_progress, req_body, req_headers, chunk_size,
        #                  timeout, method, decode, debug, file_path, ca_file,
        #                  verify)


        # store = JsonStore('http://dynamic.xkcd.com/api-0/jsonp/comic/123')
        return

        id = 123
        url = "http://xkcd.com/{0}/info.0.json".format(id)
        print(url)
        p = CustomPopup(title = url)
        p.open()

        return
        req = UrlRequest(
            # 'http://api.openweathermap.org/data/2.5/weather?q=Paris,fr',
            url,
            self.process_it)


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

        self.layout_bottom.add_widget(exp)



        car = Carousel()
        for x in range(0,10):
            car.add_widget(Page(index=x+1))


        self.layout_bottom.add_widget(car)
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