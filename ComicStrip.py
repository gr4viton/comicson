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

class CustomPopup(Popup):
    pass

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

    def popup_alt(self):
        p = CustomPopup(title=self.alt)
        p.open()

    def __init__(self, results, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        self.update_data_from_result(results)
        # print('hereeres')
        # self.im_widget_layout(self.add_widget())

    # def __init__(self, title, alt, num, image_url, **kwargs):
    #     super(GridLayout, self).__init__(**kwargs)
    #     self.title = title
    #     self.alt = alt
    #     self.num = num
    #     self.image_url = image_url
    #     # print('hereeres')
    #
    #     self.im_widget_layout = CenteredAsyncImage(source = self.image_url,
    #                             on_double_tap=CustomPopup(title=self.alt).open)
    def update_data_from_result_async(self, req, results):
        if results is not None:
            Logger.info('Async update from results of url request:')
            [Logger.info(key) for key in results.keys()]
            self.update_data_from_result(results)
            return self.results
        else:
            Logger.info('Async update from results not possible- results is None!')
            return None




    def update_data_from_result(self, results):
        self.results = results

        self.title = self.results['safe_title']
        self.alt = self.results['alt']
        self.num = int(self.results['num'])
        self.image_url = self.results['img']

        # self.title_text = self.title
        # self.remove_widget(self.im_widget_layout)
        # self.im_widget_layout.()
        # self.clear_widgets()
        # self.im_widget_layout.add_widget(
        #     CenteredAsyncImage(source = self.image_url,
        #                         on_double_tap=CustomPopup(title=self.alt).open)
        # )
        # self.im_widget = CenteredAsyncImage(source = self.image_url,
        #                         )
        # self.im_widget.source = self.image_url
        # self.im_widget.on_double_tap=CustomPopup(title=self.alt).open
        # self.im_widget.reload()
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