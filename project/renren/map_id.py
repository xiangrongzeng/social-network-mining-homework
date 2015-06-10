#! encoding=utf-8

import re
import os

folder = 'mapped_data//'
class Map():
    def __init__(self):        
        if os.path.exists(folder):
            pass
        else:
            os.makedirs(folder)
        self.folder = folder
        edges = get_edges()  
        id_map = {}
        num = 0  
        for edge in edges:
            for uid in edge:
                if id_map.has_key(uid):
                    pass
                else:
                    id_map[uid] = num
                    num += 1
        #print len(id_map),num
        write_mapping_table(id_map)
        self.id_map = id_map
        self.edges = edges
    
    def map_edges(self):
        new_edges = []
        for edge in self.edges:
            node1 = self.id_map[edge[0]]
            node2 = self.id_map[edge[1]]
            if node1 < node2:
                new_edge = [node1, node2]
            else:
                new_edge = [node2, node1]
            new_edges.append(new_edge)
        write_edges(new_edges)
    
    def map_communities(self):
        communities = get_communities()
        new_communities = []
        for community in communities:
            new_community = []
            for old_id in community:
                old_id = re.sub('\n', '', old_id)
                new_id = self.id_map[old_id]
                new_community.append(new_id)
            new_communities.append(new_community)
            print  'bb',len(community),len(new_community)
        write_communities(new_communities)
        print len(new_communities)
        
    def map_center_node(self):
        central_node = get_central_node()
        new_central_node = self.id_map[central_node]
        write_center_node(new_central_node)
    
    def map_index(self):
        uids, name_index, label_index = get_index()
        new_uids = []
        new_name_index = {}
        new_label_index = {}
        for uid in uids:
            if self.id_map.has_key(uid):
                new_uid = self.id_map[uid]
                new_uids.append(new_uid)
                new_name_index[new_uid] = name_index[uid]
                new_label_index[new_uid] = label_index[uid]
        write_index(new_uids, new_name_index, new_label_index)

def get_edges():
    filename = 'original_data//edges.txt'
    #print 'read in'
    f = open(filename,'r')
    edges = []
    for line in f:
        line = re.sub('\n', '', line)
        node_pair = line.split(' ')
        if len(node_pair) == 2:
            edges.append(node_pair)
    f.close()
    return edges

def get_central_node():
    f = open('original_data//center_node.txt','r')
    for line in f:
        node = line.strip()
        if node != '':
            return node
        else:
            print 'NO center node'

def get_communities():
    filename = 'original_data//communities.txt'
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
    uids = []
    f = open('original_data//index.txt','r')
    for line in f:
        line = line.strip().decode('utf-8','ignore')
        info = line.split(':')
        if len(info) == 3:
            uids.append(info[0])
            name_index[info[0]] = info[1]
            label_index[info[0]] = info[2]
    f.close()
    return uids, name_index, label_index

def write_communities(communities):
    f = open(folder + 'communities.txt','w')
    
    for community in communities:
        line = ''
        for node in community:
            line += str(node) + ','
        line = re.sub('\r|\n', ',', line)
        line = re.sub(',$','\n',line)
        f.write( line)
    f.close()

def write_edges(edges):
    f = open(folder + 'edges.txt','w')
    for edge in edges:
        f.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')
    f.close()

def write_center_node(central_node):
    f = open(folder + 'center_node.txt','w')
    f.write(str(central_node))
    f.close()

def write_index(uids, name_index, label_index):
    f = open(folder + 'index.txt','w')
    for uid in uids:
        line = str(uid) + ':' + name_index[uid].encode('utf-8','ignore') + ':' + label_index[uid].encode('utf-8','ignore') + '\n'
        f.write(line)
    f.close()

def write_mapping_table(id_map):
    f = open(folder + 'mapping_table.txt', 'w')
    for old_id, new_id in id_map.items():
        line = str(new_id) + ' ' + str(old_id) + '\n'
        f.write(line)
    f.close()

if __name__ == '__main__':
    print 'mapping'
    m = Map()
    m.map_center_node()
    m.map_index()
    m.map_edges()
    m.map_communities()



