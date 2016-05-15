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


import ComicDownloader as cd
from linked_list import StripBuffer

from ComicStrip import SetNumberPopup, CenteredAsyncImage
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

        # self.load_next()

class ComicScreen(Screen):
    def __init__(self, **kwargs):
        super(ComicScreen, self).__init__(**kwargs)



class ComicStripSlideViewer(Carousel):
    ignore_on_slide_end_count = 0

    def __init__(self, strip_number=None, size=3, **kwargs):
        super(ComicStripSlideViewer, self).__init__(**kwargs)
        # self.downloader = self.parent.downloader
        # self.downloader = downloader
        # return
        # self.downloader = ComicDownloader()


        # strip_number = 390
        # size = 3
        comic_name = 'xkcd'
        self.downloader = cd.ComicDownloader(self, comic_name)
        self.downloader.get_max_id()

        if strip_number == None:
            strip_number = self.downloader.comic.get_random_number()
        self.sb = StripBuffer(current_id=strip_number, size=size,
                              downloader=self.downloader)

        self.last_index = self.index
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

    def load_next_strip(self, mode='next'):

        if mode == 'next':
            print('Loading next strip')
            self.sb.next_strip()
            self.last_strip = self.sb.active
            self.last_index = self.index
        elif mode == 'prev':
            print('Loading previous strip')
            self.sb.prev_strip()
            self.last_strip = self.sb.active
            self.last_index = self.index

    def load_prev_strip(self):
        self.load_next_strip(mode='prev')
    #
    # def load_prev_strip(self):
    #     print('Loading previous strip')
    #     self.sb.prev_strip()
    #     self.last_strip = self.sb.active
    #     self.last_index = self.index

    def load_next(self, mode='next', **kwargs):
        super(ComicStripSlideViewer, self).load_next(mode=mode,**kwargs)
        # self.load_next_strip(mode=mode)



    def on_sliding_end_index(self, current_index):
        '''
        called at a time the user slides to a new slide = next or previous
        (after some time latency interval)
        '''
        # if self.ignore_on_slide_end_count != 0:
        #     self.ignore_on_slide_end_count = 0
        #     return
        tail_index = len(self.slides)-1
        print('yes')
        last_index = self.last_index
        # if last_index < 0:
        #     last_index = self.downloader.comic.max_number - last_index
        print('current_index', current_index)
        print('self.last_index', last_index)
        print('tail_index', tail_index)


        if current_index == 0 and last_index == tail_index:
            # slided front
            self.load_next_strip()
        elif current_index == tail_index and last_index == 0:
            # slided back
            self.load_prev_strip()
        elif last_index < current_index:
            # slided front
            self.load_next_strip()
        elif last_index > current_index:
            # slided back
            self.load_prev_strip()

        if self.slides[current_index].num != self.sb.active.id:
            print('The active strip id {} does not match the current index num {}'.format(
            self.sb.active.id, self.slides[current_index].num
            ))

    def on_sliding_end_current_slide(self, current_slide):
        '''
        called at a time the user slides to a new slide = next or previous
        (after some time latency  interval)
        '''
        print('yes')
        # print('current_slide',current_slide)
        # print('self.last_strip', self.last_strip)
        # print('self.last_strip.next', self.last_strip.next)
        if self.last_strip.next.id == current_slide.num:
            # slided front
            self.load_next_strip()
        elif self.last_strip.prev.id == current_slide.num:
            # slided back
            self.load_prev_strip()

    #
    # def update_strip_buffer(self):
    #     # for strip in self.buffer:
    #     #     if
    #     pass

    def next_strip(self, from_gui=False):
        self.load_next()

    def prev_strip(self, from_gui=False):
        self.load_next(mode='prev')


    def set_number(self, random=False):
        if random==True:
            num = self.downloader.comic.get_random_number()
            self.sb.set_active_id(num)
        else:
            id = self.sb.active.id
            max = self.downloader.comic.max_number
            p = SetNumberPopup(id, max, on_set_number_function=self.set_number_async)
            p.open()

    def set_number_async(self, number):
        self.sb.set_active_id(number)

    def save_image(self):
        print('Image not saved')
        pass

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