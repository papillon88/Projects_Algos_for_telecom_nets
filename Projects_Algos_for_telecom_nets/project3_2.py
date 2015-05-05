def probability_reliability():
    from itertools import combinations
    import networkx as nx
    import random
    G=nx.dense_gnm_random_graph(5,10)
    total_Edges=G.edges()
    probability=0
    while probability<1.02:
        reliability=0
        for i in xrange(0,11):
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
        print probability,reliability
        probability+=0.02

if __name__=='__main__':
   probability_reliability()