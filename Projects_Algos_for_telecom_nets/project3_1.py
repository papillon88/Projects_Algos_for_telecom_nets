def reliabilityonlinks():
    from itertools import combinations
    import networkx as nx
    import random
    G=nx.dense_gnm_random_graph(5,10)
    total_Edges=G.edges()
    probability=0.8
    for i in xrange(1,11):
        reliability=0
        for subset in combinations(total_Edges,i):
            count=0
            for j in subset:
                if len(subset)!=0:
                    count=count+1
                G.remove_edge(j[0],j[1])
                if (len(list(nx.all_simple_paths(G,0,2))) > 0):
                    reliability+=(pow(1-probability,count))*(pow(probability,(10-count)))
            for k in subset:
                G.add_edge(k[0],k[1])
        print reliability/float(i),i

if __name__=='__main__':
   reliabilityonlinks()

