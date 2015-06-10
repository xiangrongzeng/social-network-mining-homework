#!/usr/bin/env 
#!encoding=utf-8

import re

from Page import Page

class PageParser():

    def __init__(self, page):
        self.page = page

    # 获取好友的页数
    def get_list_page_num(self):
        try:
            total_number = re.search(ur'第\d+/(\d+)页', self.page, re.DOTALL).group(1)
            total_number = int(total_number)
#            print total_number
            return total_number
        except Exception as e:
            print u'无法获取好友页数'
            raise

    # 获取中心点id
    def get_center_node_id(self):
        try:
            central_node_id = re.search(ur'首页.*?id=(\d+).*?个人主页', 
                self.page, 
                re.DOTALL).group(1)
            return central_node_id
        except:
            print u'无法获中心点'
            raise

    # 获取一页里面的好友信息
    def get_friends(self):
        try:
            friends = []
            # 每个table是包含了每个好友信息的那块网页
            tables = re.findall(r'<table><tr valign="top">(.*?)</table>',self.page, re.DOTALL)
            # 每位好友的信息
            table_number = 0
            for table in tables:
                # 保存一位好友的信息
                friend = {}
                info = re.search(r'<a href=".*?id=(\d+)&amp;sid.*?">([^<].*?)</a>', table, re.DOTALL)
                friend_id = info.group(1)
                friend_name = info.group(2)
                friend_class = ''
                try:
                    friend_class = re.search(r'<span class="gray">(.*?)</span>', table, re.DOTALL).group(1)
                except:
                    friend_class = u'未分类'
                friend['uid'] = friend_id
                friend['uname'] = friend_name
                friend['uclass'] = friend_class
                friends.append(friend)
#                print u'第 %d 页的第 %d 个好友' % (page_number,table_number)
#                print u'\tid:',friend_id.encode('gbk','ignore'),
#                print friend_name.encode('gbk','ignore'),'\t',
#                print u'\tclass:',friend_class.encode('gbk','ignore')
                table_number += 1
            return friends
        except:
            raise


if __name__ == '__main__':
    url = 'http://3g.renren.com/friendlist.do?'
    page = Page(url)
    parser = PageParser(page.fetch())
    total_num = parser.get_list_page_num()
    print parser.get_center_node_id()