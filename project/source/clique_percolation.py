# encoding=utf8
import itertools
import re
import networkx as nx
import random
import matplotlib.pyplot as plt
from operator import itemgetter

def clique_percolation(k, filepath):
    print 'create graph'
    my_graph = get_graph(filepath)
    sorted(my_graph.iteritems(), key=itemgetter(0), reverse=False)
    cliques = []
    relative = {}
    print 'find cliques'
    find_k_clique(k, my_graph, cliques, relative)
#    print cliques
#    print relative
    print 'merge cliques',len(cliques)
    clusters = merge_clique(cliques, relative, k)
    print clusters
    new_clusters = []
    for cluster in clusters:
        if len(cluster) > 20:
            new_clusters.append(cluster)
    write_clusters(new_clusters)
    print 'draw graph'
    draw_cluster_network(my_graph,new_clusters)


def write_clusters(clusters):
    f = open('clusters.txt','a')
    for cluster in clusters:
        line = ''
        for node in cluster:
            line += node + ','
        line = re.sub(',$','\n',line)
        f.write(line)
    f.close()

def merge_clique(cliques, relative, k):
    clusters = []
    is_visited = [0]*len(cliques)
    for clique_number in range(0, len(cliques)):
        all_together = []
        deep_search(cliques, clique_number, relative, is_visited, all_together, k)
        if all_together != []:
            cluster = []
            for i in all_together:
                cluster += cliques[i]
            clusters.append({}.fromkeys(cluster).keys())
    return clusters

def deep_search(cliques, clique_number, relative, is_visited, all_together, k):
    if is_visited[clique_number] == 0:
        clique = cliques[clique_number]
        is_visited[clique_number] = 1
        # 计算访问了多少点，了解进度
        visited = sum(is_visited)
#        if visited%20000 == 0:
#            print visited/len(is_visited),visited
        print clique_number, visited,len(all_together)

        for nodes in (itertools.combinations(clique,k-1)):
            together = relative[nodes[0]]
            for i in range(1, len(nodes)):
                together = list(set(together).intersection(set(relative[nodes[i]])))
            all_together += together
        all_together = {}.fromkeys(all_together).keys()
        while all_together:
            clique_number = all_together.pop()
            deep_search(cliques, clique_number, relative, is_visited, all_together, k)



def find_k_clique(k, graph, cliques, relative):
    count = 0
    number = 0
    for central_node,adjacent_nodes in graph.items():
        if len(adjacent_nodes) >= k-1:
            for nodes in (itertools.combinations(adjacent_nodes,k-1)):
##                print central_node,nodes
                count += 1
                if is_complete(nodes,graph) == True:
                    count
                    new = [central_node]
                    try:
                        relative[central_node].append(number)
                    except:
                        relative[central_node] = [number]
                    for node in nodes:
                        new.append(node)
                        try:
                            relative[node].append(number)
                        except:
                            relative[node] = [number]
##                    print new
                    cliques.append(new)
                    number += 1
    print count


def is_complete(nodes, graph):
    for i in range(0, len(nodes)):
        for j in range(i+1, len(nodes)):
            try:
                if not (nodes[j] in graph[nodes[i]] or nodes[i] in graph[nodes[j]]):
                    return False
            except:
                return False
    return True

def get_graph(filepath):
    f = open(filepath, 'r')
    my_graph = {}
    for line in f:
        line = re.sub('\n', '', line)
        node_pair = line.split(' ')
        try:
            my_graph[node_pair[0]].append(node_pair[1])
        except:
            my_graph[node_pair[0]] = [node_pair[1]]
    return my_graph

def draw_cluster_network(graph,clusters):
    original_graph = nx.Graph()
    cluster_graph = nx.Graph()
    for node,nodes in graph.items():
        for v in nodes:
            cluster_graph.add_edge(node, v)
            original_graph.add_edge(node, v)
    pos = nx.spring_layout(cluster_graph)
    for i in range(0, len(clusters)):
        color = (random.random(),random.random(),random.random())
        print color,clusters[i]
        nx.draw_networkx_nodes(cluster_graph,pos,clusters[i],node_color=color)


    nx.draw_networkx_edges(cluster_graph,pos, with_labels=True,alpha=0.5)
    plt.show()
#    nx.draw(original_graph)
#    plt.show()


if __name__ == '__main__':
#    graph = get_graph(r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined_min.txt')
#    print graph
#    find_k_clique(22, graph, [])
    clique_percolation(3, r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined.txt')
