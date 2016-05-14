
from kivy.network.urlrequest import UrlRequest
from kivy.logger import Logger

# web scrapping inspiration from https://github.com/1995eaton/xkcd_downloader/blob/master/xkcd_downloader.py
import time
import sys


from kivy.clock import Clock

from ComicStrip import ComicStrip

class ComicDownloader(object):
    def __init__(self, carousel):
        self.comic_name = 'xkcd'
        self.carousel = carousel
        # pass

    def process_request(self, req, results):

        print('je')

        if results is not None:
            Logger.info('Results of url request:')
            [Logger.info(key) for key in results.keys()]
        else:
            Logger.info('No id result for request!')

        # key = 'img'
        # Logger.info(key + ' : ' + results[key])

        # [print(key) for key in results.keys()]
        # what = 'year'
        # if what in results.keys():
        #     print(results.get(what))

        # title = 'Nightmares'
        # alt = 'you dont sleep'
        # num = 666
        # image_url = 'http://imgs.xkcd.com/comics/keeping_time.png'

        # self.title = results['title']
        # self., results['alt'], results['num'], results['image_url'])
        self.results = results

        # print(title, alt, num, image_url)
        # return title, alt, num, image_url
        # req.is_finished = True
        return True

    def create_strip_widget(self, number):
        # if self.get_strip_widget()

        # widget = self.get_strip_widget(number)
        widget = ComicStrip(self.get_strip_data(number))
        self.carousel.add_widget(widget)
        return widget

    # def update_strip(self, number, strip_widget):
    #     strip_widget.update_data(self.get_strip_data(number))


    # def get_strip_widget(self, number):
    #     get_strip_data
    #     return ComicStrip(results)

    def get_strip_data(self, number):

        if number < 0:
            url = None
            Logger.info('Cannot load negative comic number!')
            return None
        elif number == 0:
            url = "http://xkcd.com/info.0.json"
        else:
            url = "http://xkcd.com/{0}/info.0.json".format(number)

        print('Trying to get the [{}] comic number [{}]'.format(self.comic_name, number))
        req = UrlRequest(url, self.process_request)

        while not req.is_finished:
            # time.sleep(1)
            Clock.tick()
            pass

        print(req._result)

        return self.results



            # print('Could not get the [{}] comic number [{}]!'.format
            #       (self.comic_name, number))
            #
            # time.sleep(5)
            # return self.get_strip(number+1)