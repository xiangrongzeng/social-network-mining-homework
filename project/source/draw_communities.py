
# encoding=utf8
import re
import networkx as nx
import random
import matplotlib.pyplot as plt

def get_graph(graph_data_path):
    f = open(graph_data_path, 'r')
    my_graph = {}
    for line in f:
        line = re.sub('\n', '', line)
        node_pair = line.split(' ')
        try:
            my_graph[node_pair[0]].append(node_pair[1])
        except:
            my_graph[node_pair[0]] = [node_pair[1]]
    return my_graph

def get_clusters(communities_data_path):
    f = open(communities_data_path, 'r')
    clusters = []
    for line in f:
        line = re.sub('\n', '', line)
        cluster = line.split(',')
        clusters.append(cluster)
    return clusters

def draw_cluster_network(graph_data_path, communities_data_path):
    graph = get_graph(graph_data_path)
    clusters = get_clusters(communities_data_path)
    original_graph = nx.Graph()
    cluster_graph = nx.Graph()
    labels = {}
    for node,nodes in graph.items():
        for v in nodes:
            cluster_graph.add_edge(node, v)
            original_graph.add_edge(node, v)
            labels[node] = r'$'+node+'$'
            labels[v] = r'$'+v+'$'
    pos = nx.shell_layout(cluster_graph)
    pos = nx.spectral_layout(cluster_graph)
    pos = nx.spring_layout(cluster_graph)
    for i in range(0, len(clusters)):
        nx.draw_networkx_nodes(cluster_graph,
                               pos,
                               node_size = 500,
                               nodelist = clusters[i],
                               node_color=(random.random(),random.random(),random.random()),
                               alpha = 0.5)
    nx.draw_networkx_edges(cluster_graph,
                           pos,
                           with_labels=True,
                           alpha=0.5,
                           width = 0.5)
    nx.draw_networkx_labels(cluster_graph,
                            pos,
                            labels,
                            fontsize=16)
#    nx.draw(original_graph)
    plt.show()
    plt.savefig('2.png')
    plt.clf()

if __name__ == '__main__':
    draw_cluster_network('network_data', 'mycommunities.txt')
