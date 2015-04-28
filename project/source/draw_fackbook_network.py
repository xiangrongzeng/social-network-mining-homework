import networkx as nx
import matplotlib.pyplot as plt
import re

filepath = "c:\\Users\\sunder\\Documents\\project\\social-network-mining\\project\\project_document\\facebook\\facebook_combined.txt"
facebook = open(filepath)

G = nx.Graph()
for line in facebook:
    line = re.sub("\r\n","", line)
    node_pair = line.split(" ")
    G.add_edge(int(node_pair[0]), int(node_pair[1]))
nx.draw_spring(G)
plt.show()


