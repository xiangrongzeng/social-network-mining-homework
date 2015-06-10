#! encoding=utf-8
import re

folder = 'mapped_data//'

def run():
    center_node = get_center_node()
    edges = get_edges()
    communities = get_communities()
    name_index,label_index = get_index()
    recommend_node, recommend_name, recommend_reason = recommend(center_node, edges, communities, name_index, label_index)
    write_recommend_node_and_reason(recommend_node, recommend_name, recommend_reason)

def get_edges():
    filename = folder + 'edges.txt'
    f = open(filename,'r')
    edges = {}
    for line in f:
        line = re.sub('\n', '', line)
        node_pair = line.split(' ')
        if edges.has_key(node_pair[0] ):
            edges[node_pair[0]].append(node_pair[1])
        else:
            edges[node_pair[0]] = [node_pair[1]]
        if edges.has_key(node_pair[1] ):
            edges[node_pair[1]].append(node_pair[0])
        else:
            edges[node_pair[1]] = [node_pair[0]]
    f.close()
    return edges

def get_center_node():
    filename = folder + 'center_node.txt'
    f = open(filename,'r')
    for line in f:
        node = line.strip()
        return node

def get_communities():
    filename = folder + 'communities.txt'
#    filename = 'wjjCommunity.txt'
    f = open(filename,'r')
    communities = []
    for line in f:
        community = line.strip().split(',')
        communities.append(community)
    f.close()
    return communities

def get_index():
    name_index = {}
    label_index = {}
    filename = folder + 'index.txt'
    f = open(filename,'r')
    for line in f:
        line = line.strip().decode('utf-8','ignore')
        info = line.split(':')
        name_index[info[0]] = info[1]
        label_index[info[0]] = info[2]
    f.close()
    return name_index, label_index


def get_myfriends(central_node, edges):
    return edges[central_node]

# 返回共同好友中最多的label
def find_reason(our_same_friends, label_index):
    labels = {}
    for friend in our_same_friends:
        label = label_index[friend]
        if labels.has_key(friend):
            labels[label] += 1
        else:
            labels[label] = 1

    max_times = 0
    reason = ''
    for label,times in labels.items():
        if times > max_times:
            reason = label
    return reason



def recommend(central_node, edges, communities, name_index, label_index):
    recommend_node = []
    recommend_name = []
    recommend_reason = []
    myfriends = get_myfriends(central_node, edges)
#    for a in myfriends:
#        print a,name_index[a].encode('gbk','ignore')

    for community in communities:
        # 中心点在这个社区中的好友
        my_community_friends = list(set(myfriends).intersection(set(community)))
        print len(myfriends),len(community),len(my_community_friends)
#        for a in my_community_friends:
#            print a,name_index[a].encode('gbk','ignore')
        for node in community:
            if node in myfriends or node == central_node:
                pass
            else: # 处理好友的好友
                nodefriends = edges[node]
                # 取交集
                our_same_friends = list(set(myfriends).intersection(set(nodefriends)))
                # 如果这个社区中共同好友超过一半，则推荐
                if len(our_same_friends) >= len(my_community_friends) *0.5:
                    reason = find_reason(our_same_friends, label_index)
                    recommend_node.append(node)
                    recommend_name.append(name_index[node])
                    recommend_reason.append(reason)
                    print 'recommend:%s:%s:%s\t%s' % (node,name_index[node].encode('gbk','ignore'),label_index[node].encode('gbk','ignore'), reason.encode('gbk','ignore'))
        print '**************'
    return recommend_node,recommend_name, recommend_reason

def write_recommend_node_and_reason(recommend_node, recommend_name, recommend_reason):
    filename = folder + 'recommend_node.txt'
    f = open(filename,'w')
    for i in range(0, len(recommend_node)):
        node = recommend_node[i]
        name = recommend_name[i]
        reason = recommend_reason[i]
        line = str(node) + ':' + name.encode('utf-8','ignore') + ',' + reason.encode('utf-8','ignore') + '\n'
        f.write(line)
    f.close()
    print ' write to file succeed'

if __name__ == '__main__':
    run()



