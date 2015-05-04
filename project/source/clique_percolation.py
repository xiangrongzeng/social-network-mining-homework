# encoding=utf8
import itertools
import re
import networkx as nx
import random
import matplotlib.pyplot as plt
from operator import itemgetter

def clique_percolation(filepath):
    k = 3
    print 'create graph'
    my_graph = get_graph(filepath)
    sorted(my_graph.iteritems(), key=itemgetter(0), reverse=False)
    cliques = []
    print 'find cliques'
    find_k_clique(k, my_graph, cliques)
    print 'clique number = ' + str(len(cliques))
#    print cliques
    print 'merge cliques'
    times = 0
    bigger_clusters = []
    smaller_clusters = cliques
    flag = True
    while flag:
        times += 1
        print '\tmerge round' + str(times) + ': cluster number=' + str(len(smaller_clusters))
        bigger_clusters = merge_clusters(smaller_clusters)
        if len(bigger_clusters) == len(smaller_clusters):
            flag = False
        else:
            smaller_clusters = bigger_clusters
    clusters = bigger_clusters
#    clusters_tmp0 = merge_clique(cliques)
#    clusters_tmp = merge_clique(clusters_tmp0)
#    print clusters_tmp
#    clusters = merge_clique(clusters_tmp)
#    print clusters
    new_clusters = []
    for cluster in clusters:
        if len(cluster) > 70:
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

def merge_clusters(clusters):
    show_range = len(clusters)/50
    if show_range == 0:
        show_range = len(clusters)
    bigger_clusters = [clusters[0]]
    for i in range(1, len(clusters)):
        if i%show_range == 0:
            print i,1.0*i/len(clusters)
        cluster = clusters[i]
        for j in range(0,len(bigger_clusters)):
            bigger_cluster = bigger_clusters[j]
            if is_nearby(cluster, bigger_cluster) == True:
                bigger_cluster += cluster
                bigger_clusters[j] = list(set(bigger_cluster))
                break
            if j == len(bigger_clusters)-1:
                bigger_clusters.append(cluster)
    return bigger_clusters

def is_nearby(clique1, clique2):
    clique = clique1 + clique2
    clique = list(set(clique))
    if len(clique) <= len(clique2) + 1:
        return True
    else:
        return False

def find_k_clique(k, graph, cliques):
    count = 0
    for central_node,adjacent_nodes in graph.items():
        if len(adjacent_nodes) >= k-1:
            for nodes in (itertools.combinations(adjacent_nodes,k-1)):
##                print central_node,nodes
                count += 1
                if is_complete(nodes,graph) == True:
                    count
                    new = [central_node]
                    for node in nodes:
                        new.append(node)
##                    print new
                    cliques.append(new)
#    print count


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
        nx.draw_networkx_nodes(cluster_graph,pos,clusters[i],node_color=(random.random(),random.random(),random.random()))


    nx.draw_networkx_edges(cluster_graph,pos, with_labels=True,alpha=0.5)
#    nx.draw(original_graph)
    plt.savefig('2.png')


if __name__ == '__main__':
#    graph = get_graph(r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined_min.txt')
#    print graph
#    find_k_clique(22, graph, [])
    clique_percolation(r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined_min.txt')
