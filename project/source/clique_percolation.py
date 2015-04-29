# encoding=utf8
import itertools
import re
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

def clique_percolation(k, filepath):
    print 'create graph'
    my_graph = get_graph(filepath)
    sorted(my_graph.iteritems(), key=itemgetter(0), reverse=False)
    cliques = []
    print 'find cliques'
    find_k_clique(k, my_graph, cliques)
#    print cliques
    print 'merge cliques',len(cliques)
    clusters = merge_clique(cliques)
#    print clusters
    print 'draw graph'
    draw_cluster_network(my_graph,clusters)

    write_clusters(clusters)

def write_clusters(clusters):
    f = open('clusters.txt','a')
    for cluster in clusters:
        line = ''
        for node in cluster:
            line += node + ','
        line = re.sub(',$','\n',line)
        f.write(line)
    f.close()

def merge_clique(cliques):
    clusters = [cliques[0]]
    for i in range(1, len(cliques)):
        if i%20000 == 0:
            print i,1.0*i/len(cliques)
        clique = cliques[i]
        for j in range(0,len(clusters)):
            cluster = clusters[j]
            if is_nearby(clique, cluster) == True:
                cluster += clique
                clusters[j] = list(set(cluster))
                break
            if j == len(clusters)-1:
                clusters.append(clique)
    return clusters

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
    colors = ['red','blue','black','white','yellow','green','gray','cyan','magenta']
    for i in range(0, len(clusters)):
        nx.draw_networkx_nodes(cluster_graph,pos,clusters[i],node_color=colors[i])
#        nx.draw_networkx_nodes(cluster_graph,pos,clusters[i],node_color=(1.0*i/len(clusters),1.0*i/len(clusters),1.0*i/len(clusters)))


    nx.draw_networkx_edges(cluster_graph,pos, with_labels=True,alpha=0.5)
#    nx.draw(original_graph)
    plt.show()


if __name__ == '__main__':
#    graph = get_graph(r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined_min.txt')
#    print graph
#    find_k_clique(22, graph, [])
    clique_percolation(3, r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined.txt')

