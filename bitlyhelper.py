#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'


import urllib.request
import json


TOKEN ='7b4687b6df5cdd677c732492b8d4bfb796ed1328'
ROOT_URL = 'https://api-ssl.bitly.com'
SHORTEN = '/v3/shorten?access_token={}&longUrl={}'


class BitlyHelper(object):
    def shorten_url(self,longurl):
        try:
            url = ROOT_URL+SHORTEN.format(TOKEN,longurl)
            response = urllib.request.urlopen(url).read()
            jr = json.loads(response)
            return jr['data']['url']
        except Exception as e:
            print(e)


if __name__ == '__main__':
    BH = BitlyHelper()
    jr = BH.shorten_url("http://127.0.0.1:5000")
    print(jr)