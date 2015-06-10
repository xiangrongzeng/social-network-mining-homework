#!/usr/bin/env 
#!encoding=utf-8
import logging

from get_edges import get_edges
from map_id import Map
from select_nodes import select

def run():
    logging.basicConfig(filename='spider.log', level=logging.DEBUG)
    logging.info('Started')
    # 爬取并解析信息，生成边文件
    print u'开始爬取好友关系'
    original_url = 'http://3g.renren.com/friendlist.do?'
    if get_edges(original_url):
        print  u'爬取好友关系成功'
        # 过滤
        print  u'剔除连接数较少的点'
        select(4)
        print  u'将原始id映射到新的id'
        # 映射原始id到新id
        m = Map()
        m.map_center_node()
        m.map_index()
        m.map_edges()
    logging.info('Finished')
    print u'结束'

if __name__ == '__main__':
    run()