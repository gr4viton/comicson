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
# from kivy.uix.behaviors import Sc
from kivy.uix.scatter import Scatter

from kivy.config import Config

from kivy.uix.popup import Popup

from kivy.uix.image import AsyncImage
from kivy.logger import Logger

class AltTextPopup(Popup):
    text = StringProperty()
    def __init__(self, text, **kwargs):
        super(Popup, self).__init__(**kwargs)
        self.text = text

class ImageButton(ButtonBehavior, Image):
    pass

class SetNumberPopup(Popup):
    # value = NumericProperty()
    # min = NumericProperty()
    # max = NumericProperty()
    slider = ObjectProperty()
    def __init__(self, value, max, on_set_number_function, **kwargs):
        super(Popup, self).__init__(**kwargs)
        # self.value = value
        # self.max = max
        self.slider.value = value
        self.slider.max = max
        self.on_set_number_function = on_set_number_function
    #
    # def on_valu
    def on_set_number(self, value, random=False):
        # if self.on_dismiss_function is not None:
        # value = self.slider.value
        print('Selected value from SetNumberPopup = [{}]'.format(value))
        self.on_set_number_function(int(value), random)
        # self.on_set_number
        self.dismiss()
        # super(Popup, self).on_dismiss(**kwargs)

class CenteredAsyncImage(AsyncImage):
    pass

# class ComicStripImage(CenteredAsyncImage, Button):
# class ComicStripImage( ButtonBehavior, Scatter, AsyncImage):
class ComicStripImage( ButtonBehavior, AsyncImage):
    # def __init__(self, **kwargs):
    #     super(AsyncImage, self).__init__(**kwargs)

    # def popup(self):
    #     pass
    pass

class ComicStrip(GridLayout):
    # num = -1
    # alt = ''
    # title = ''
    # image_url = ''
    # im_widget_layout = ObjectProperty()
    im_widget = ObjectProperty()

    title = StringProperty('...loading...')
    alt = StringProperty('...loading...')
    image_url = StringProperty('')
    num = NumericProperty('-')

    def popup_alt(self, whatever=None):
        titlenum = self.titlenum()
        p = AltTextPopup(title=titlenum, text=self.alt)
        p.open()

    def titlenum(self):
        return '[{}] {}'.format(self.num, self.title)

    def __init__(self, results, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        self.update_data_from_result(results)


    def update_data_from_result_async(self, req, results):
        if results is not None:
            Logger.info('Async update from results of url request:')
            # [Logger.info(key) for key in results.keys()]
            self.update_data_from_result(results)
            return self.results
        else:
            Logger.info('Async update from results not possible- results is None!')
            return None

    def update_data_from_result(self, results):
        if results is  None:
            self.results = None
            print('Empty ComicStrip created')
            return
        self.results = results
        self.title = self.results['safe_title']
        self.alt = self.results['alt']
        self.num = int(self.results['num'])
        self.image_url = self.results['img']

        print(self.im_widget, 'reloading with', self.image_url)



    def __str__(self):
        txt = '['
        txt += 'num={0:>5},'.format(self.num)
        txt += 'title={0:>14},'.format(self.title)
        # txt += 'alt={0:>5},'.format(self.alt)
        txt += 'image_url={0:>20},'.format(self.image_url)
        txt += ']'
        return txt
    # pass