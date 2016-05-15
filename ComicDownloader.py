
from kivy.network.urlrequest import UrlRequest
from kivy.logger import Logger

# web scrapping inspiration from https://github.com/1995eaton/xkcd_downloader/blob/master/xkcd_downloader.py
import time
import sys


from kivy.clock import Clock

from ComicStrip import ComicStrip
from random import random as rnd

class ComicInfo(object):
    def __init__(self, name, url_last, url_number, url_orig):
        self.name = name
        self.url_last = url_last
        self.url_number = url_number
        self.url_orig = url_orig
        self.max_number = 1

        q = 0
        max_q = 10
        sleep = 0.1
        while(self.max_number is 1):
            time.sleep(sleep)
            q += 1
            if q > max_q:
                # load from storage!
                self.max_number = 1680

    def get_random_number(self):

        random_number = int(rnd() * self.max_number)
        return random_number

class ComicDownloader(object):
    results = None

    def __init__(self, carousel, comic_name):
        self.carousel = carousel
        # pass

        self.comics = {}

        comic_info = ComicInfo('xkcd',
                               'http://xkcd.com/info.0.json',
                               'http://xkcd.com/{0}/info.0.json',
                               'http://xkcd.com')

        self.comics[comic_info.name] = comic_info

        self.comic = self.comics[comic_name]


    def process_request(self, req, results):

        if results is not None:
            Logger.info('Results of url request:')
            [Logger.info(key) for key in results.keys()]
        else:
            Logger.info('No id result for request!')

        self.results = results

        return self.results

    def get_max_id(self, comic_name=None):
        if comic_name is not None:
            self.comic = self.comics[comic_name]
        #     # comic_name = self.comic_name
        #     url = self.comic.url_last
        # else:
        #     url = None
        self.get_strip_data(0,
                            process_request=self.set_max_id_async,
                            wait=False)

    def set_max_id_async(self, req, result):
        max_num = int(result['num'])
        self.comic.max_number = max_num
        print('Comic [{}] has [{}] comic strips!'.format(
            self.comic.name, self.comic.max_number))


    def create_strip_widget(self, number):
        # if self.get_strip_widget()

        # widget = self.get_strip_widget(number)

        # functional - waiting
        widget = ComicStrip(None)
        self.get_strip_data(number,
                            process_request=widget.update_data_from_result_async,
                            wait=False)
        self.carousel.add_widget(widget)


        return widget

    # def update_strip(self, number, strip_widget):
    #     strip_widget.update_data(self.get_strip_data(number))


    # def get_strip_widget(self, number):
    #     get_strip_data
    #     return ComicStrip(results)

    def get_strip_data(self, number, process_request=None, wait=True):
        if process_request is not None:
            this_process_request = process_request
        else:
            this_process_request = self.process_request

        if number < 0:
            # url = self.comic.url_number.format(self.comic.max_number-number)
            Logger.info('Cannot load negative comic number!')
            return None
        elif number == 0:
            url = self.comic.url_last
        else:
            url = self.comic.url_number.format(number)

        print('Trying to get the [{}] comic number [{}]'.format(self.comic.name, number))
        req = UrlRequest(url, this_process_request)

        if wait==True:
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