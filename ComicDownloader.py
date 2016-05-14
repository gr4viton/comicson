
from kivy.network.urlrequest import UrlRequest
from kivy.logger import Logger

# web scrapping inspiration from https://github.com/1995eaton/xkcd_downloader/blob/master/xkcd_downloader.py
import time
import sys


from kivy.clock import Clock

from ComicStrip import ComicStrip

class ComicDownloader(object):
    results = None
    def __init__(self, carousel):
        self.comic_name = 'xkcd'
        self.carousel = carousel
        # pass

    def process_request(self, req, results):

        if results is not None:
            Logger.info('Results of url request:')
            [Logger.info(key) for key in results.keys()]
        else:
            Logger.info('No id result for request!')

        self.results = results

        return self.results


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
            url = None
            Logger.info('Cannot load negative comic number!')
            return None
        elif number == 0:
            url = "http://xkcd.com/info.0.json"
        else:
            url = "http://xkcd.com/{0}/info.0.json".format(number)

        print('Trying to get the [{}] comic number [{}]'.format(self.comic_name, number))
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