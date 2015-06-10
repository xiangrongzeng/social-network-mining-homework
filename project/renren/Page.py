#!/usr/bin/env 
#!encoding=utf-8
# author:sunder
# datte:2015/6/6
# 功能：读入人人的cookie，爬取指定的人人网页，返回得到的网页

import requests
import os
import urllib2
import cookielib
import urllib
import logging
class Page():
    def __init__(self, url):
        self.url = url

    def fetch(self):
        headers = {'User-Agent': 'alexkh'}
        cookie = get_cookie()
        try:
            r = requests.get(self.url,headers = headers, cookies = cookie)
            text = r.content.decode('utf-8','ignore')
         #   print text.encode('gbk','ignore')
            logging.debug('fetch succeed')
            return r.text
        except Exception as e:
            logging.debug('fetch failed')
            logging.debug(e)
            raise
    '''
    def fetch(self):
        logging.debug('fetching pages...')
        try:
            f = open('identity.dat', 'r')
            uname = f.readline().strip()
            passwd = f.readline().strip()
            logging.debug('get uname and password succeed')
            domain = 'renren.com'
            try:
                cj = cookielib.LWPCookieJar()
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                urllib2.install_opener(opener)
                params = {'email': uname, 'password': passwd, 'origURL': self.url, 'domain': domain}
                req = urllib2.Request(self.url, urllib.urlencode(params))
                r = opener.open(req)
                html = r.read()
                logging.debug('fetching pages succeed')
                return html.decode('utf-8', 'ignore')
            except Exception as e:
                logging.info(e)
                loging.info(u'无法打开网页')
                raise
        except IOError:
            logging.info(u'无法打开identity.dat')
            raise
        logging.debug('finish fetching')
        '''

def get_cookie():
    cookie = {}
    filename = 'cookie.cookie'
    if os.path.exists(filename):
        f = open(filename)
        for line in f:
            line = line.strip()
            info = line.split('=')
            cookie[info[0]] = info[1]
        f.close()
    else:
        print u'找不到cookie.cookie文件'
    return cookie

if __name__ == '__main__':
    page = Page('http://3g.renren.com/friendlist.do?')
    page.fetch()
