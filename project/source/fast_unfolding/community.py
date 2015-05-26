#! encoding=utf-8

import re

class Community:
    name = 0; # community 名称
    nodes = [] # 包含的顶点
    neighbors = [] # 相连的community

    def __init__(self,community_name):
        self.name = community_name
        self.nodes = [] # 包含的顶点
        self.neighbors = [] # 相连的community

    def get_name(self):
        return self.name

    def add_node(self,node_name):
        self.nodes.append(node_name)

    def get_nodes(self):
        return self.nodes

    def add_neighbor(self,neighbor_name):
        self.neighbors.append(neighbor_name)

    def get_neighbors(self):
        return self.neighbors

    def get_neighbor_communities(self,index):
        neighbor_communities = []
        for neighbor in self.neighbors:
            neighbor_communities.append(index[neighbor])
        # 去重
        neighbor_communities = list(set(neighbor_communities))
        return neighbor_communities

class MyGraph:
    filepath = ''

    def __init__(self, filepath):
        self.filepath = filepath

    def get_graph(self):
        f = open(self.filepath, 'r')
        my_graph = {}
        for line in f:
            line = re.sub('\n', '', line)
            node_pair = line.split(' ')
            try:
                my_graph[node_pair[0]].append(node_pair[1])
            except:
                my_graph[node_pair[0]] = [node_pair[1]]
            try:
                my_graph[node_pair[1]].append(node_pair[0])
            except:
                my_graph[node_pair[1]] = [node_pair[0]]

        return my_graph


if __name__ == '__main__':
    filepath = r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined_min.txt'
    graph = MyGraph(filepath)
    my_graph = graph.get_graph()
    print my_graph
    community_name = 0
    communities = {}
    index = {} # node为key，node所在的community为value
    for node,neighbors in my_graph.items():
        index[node] = community_name
        c = Community(community_name)
        c.add_node(node)
        for neighbor in neighbors:
            c.add_neighbor(neighbor)
        communities[community_name] = c
        community_name += 1
    i = 9
    print communities[i].get_nodes(),communities[i].get_neighbors()[0],communities[i].get_neighbor_communities(index)
    node = communities[i].get_neighbors()[0]
    print communities[index[node]].get_nodes()

