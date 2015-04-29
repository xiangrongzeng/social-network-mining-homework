# encoding=utf8
import itertools
import re
import networkx as nx
import matplotlib.pyplot as plt

def clique_percolation(k, filepath):
    print 'create graph'
    my_graph = get_graph(filepath)
    cliques = []
    print 'find cliques'
    find_k_clique(k, my_graph, cliques)
    clusters = merge_clique(cliques)
#    print clusters
    print 'draw graph'
    draw_cluster_network(my_graph,clusters)

def merge_clique(cliques):
    cluster_label = []
    for i in range(0, len(cliques)):
        cluster_label.append(i)

    clusters = [[]]*len(cliques)
    for i in range(0, len(cliques)):
        for j in range( i+1, len(cliques)):
#            print i,cliques[i],j,cliques[j]
            if is_nearby(cliques[i], cliques[j]) == True:
                cluster_label[j] = cluster_label[i]
                # 去重
                clique =clusters[cluster_label[i]] + cliques[i] + cliques[j]
                clusters[cluster_label[i]] =  list(set(clique))
#                print cluster_label[i],clusters

    while [] in clusters:
        clusters.remove([])

    return clusters

def is_nearby(clique1, clique2):
    clique = clique1 + clique2
    clique = list(set(clique))
    if len(clique) == len(clique1) + 1:
        return True
    else:
        return False

def find_k_clique(k, graph, cliques):
    for central_node,adjacent_nodes in graph.items():
        if len(adjacent_nodes) >= k-1:
            for nodes in (itertools.combinations(adjacent_nodes,k-1)):
                if is_complete(nodes,graph) == True:
                    new = [central_node]
                    for node in nodes:
                        new.append(node)
#                    print new
                    cliques.append(new)


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
    colors = ['y','b']
    original_graph = nx.Graph()
    cluster_graph = nx.Graph()
    for node,nodes in graph.items():
        for v in nodes:
            cluster_graph.add_edge(node, v)
            original_graph.add_edge(node, v)
    pos = nx.spring_layout(cluster_graph)
    for i in range(0, len(clusters)):
        col = colors[i]
        nx.draw_networkx_nodes(cluster_graph,pos,clusters[i],node_color=col)


    nx.draw_networkx_edges(cluster_graph,pos, with_labels=True,alpha=0.5)
#    nx.draw(original_graph)
    plt.show()


if __name__ == '__main__':
#    graph = get_graph(r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined_min.txt')
#    print graph
#    find_k_clique(22, graph, [])
    clique_percolation(3, r'c:\Users\sunder\Documents\project\social-network-mining\project\project_document\facebook\facebook_combined.txt')

