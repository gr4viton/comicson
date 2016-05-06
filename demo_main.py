# you need this two lines:
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'

#kivy program
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

class TestApp(App):
    def build(self):
        Config.set('graphics', 'multisamples', 0) # to correct bug from kivy 1.9.1 - https://github.com/kivy/kivy/issues/3576
        return Button(text='Hello World')

TestApp().run()





