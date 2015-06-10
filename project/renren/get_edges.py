#!/usr/bin/env 
#!encoding=utf-8

import os
import logging

from Page import Page
from FriendlistPageParser import PageParser

def get_edges(original_url):
    node_friends = {} # 保存所有点及对应好友的数组

    # 处理中心点
    try:
        original_page = Page(original_url)
        original_parser = PageParser(original_page.fetch())
        center_node_id = original_parser.get_center_node_id() # 中心点的id
        total_page_number = original_parser.get_list_page_num() # 共有多少页好友
        # 获取中心点的所有好友
        logging.info( u'获取 %s 中心点 的所有好友，共有%d页' % (center_node_id, total_page_number))
        central_node_friends = get_all_friends(total_page_number, original_url)
        node_friends[center_node_id] = central_node_friends
    except:
        logging.info( u'获取失败')
        return False

    # 逐个处理好友的好友
    num = 1
    for central_node_friend in central_node_friends:
        url = 'http://3g.renren.com/getfriendlist.do?f=all&id=' + central_node_friend['uid']        
        try:
            page = Page(url)
            parser = PageParser(page.fetch())
            total_page_number = parser.get_list_page_num()
            logging.info( u'(%d/%d)\t获取 %s 的所有好友，共有%d页\t' % (
                num, 
                len(central_node_friends),
                central_node_friend['uid'], 
                total_page_number),)
            try:
                logging.info( central_node_friend['uname'].encode('gbk','ignore'))
            except UnicodeDecodeError:
                logging.info( '\n')
            num += 1
            # 获取该好友的所有好友
            friend_all_friends = get_all_friends(total_page_number, url)
            node_friends[central_node_friend['uid']] = friend_all_friends
        except:
            logging.info( u'%s获取失败' % central_node_friend['uid'])
    
    # 生成好友之间的边的关系
    edges = [] # 保存所有的边
    index = {} # 保存每个人的信息
    judge = {} # 判断某条边是否已经保存了
    for node_id, friends in node_friends.items():
        for friend in friends:
            friend_id = friend['uid']
            index[friend_id] = friend['uname'] + ':' + friend['uclass']
            if int(node_id) < int(friend_id):
                key = node_id + ',' + friend_id
                if judge.has_key(key):
                    pass
                else:
                    judge[key] = True
                    edges.append([node_id, friend_id])
            else:
                key = friend_id + ',' + node_id
                if judge.has_key(key):
                    pass
                else:
                    judge[key] = True
                    edges.append([friend_id, node_id])
    for central_node_friend in central_node_friends:
        index[central_node_friend['uid']] = central_node_friend['uname'] + ':' + central_node_friend['uclass']

    # 写入文件
    folder = 'original_data//'
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)
    f = open(folder + 'center_node.txt','w')
    f.write(center_node_id + '\n')
    f.close()

    f = open(folder + 'edges_unselect.txt', 'w')    
    for edge in edges:
        line = edge[0] + ' ' + edge[1] + '\n'
        f.write(line)
    f.close()
    
    f = open(folder + 'index.txt','w')
    for k,v in index.items():
        line = k + ':' + v + '\n'
        f.write(line.encode('utf-8','ignore'))
    f.close()
    logging.info( u'写入文件成功')
    
    return True


# 获取某点所有的好友
def get_all_friends(total_page_number, original_url):
    all_friends = []
    for page_num in range(0, total_page_number):
        url=original_url + '&curpage=' + str(page_num)
        page = Page(url)
        parser = PageParser(page.fetch())
        all_friends.extend(parser.get_friends())
    return all_friends


if __name__ == '__main__':    
    original_url = 'http://3g.renren.com/friendlist.do?'
    get_edges(original_url)
    


