#! encoding=utf-8
import re
import os

def select(threshold):
    filename = 'original_data//edges_unselect.txt'
    print 'read in'
    f = open(filename,'r')
    nodes_times = {}
    node_pairs = []
    for line in f:
        line = re.sub('\n', '', line)
        node_pair = line.split(' ')
        node_pairs.append(node_pair)
        for node in node_pair:
            if nodes_times.has_key(node):
                nodes_times[node] += 1
            else:
                nodes_times[node] = 1
    f.close()
    
    print 'selsect',len(node_pairs),
    filename = 'original_data//edges.txt'
    f = open(filename,'w')
    num = 1
    for node_pair in node_pairs:
        t1 = nodes_times[node_pair[0]]
        t2 = nodes_times[node_pair[1]]
        if t1 >= threshold and t2 >= threshold:
            f.write(node_pair[0] + ' ' + node_pair[1] + '\n')
            num += 1
    f.close()
    print 'to %d' % num

if __name__ == '__main__':
    select(4)



