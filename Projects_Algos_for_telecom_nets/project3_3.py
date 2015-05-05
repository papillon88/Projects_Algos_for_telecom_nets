from itertools import combinations
import networkx as nx
from random import choice
G=nx.dense_gnm_random_graph(5,10)
t=G.edges()
p=0.9
a=0
r=0
s='nothing'
num=[]


def main():
    for i in xrange(0,11):
        for subset in combinations(t,i):
            count=0
            for j in subset:
                if len(subset)!=0:
                    count=count+1
                G.remove_edge(j[0],j[1])
            if (len(list(nx.all_simple_paths(G,0,2))) > 0):
                s='up'
            else:
                s='down'
            r=(pow(1-p,count))*(pow(p,(10-count)))
            for k in subset:
                G.add_edge(k[0],k[1])
            num.append([r,s])
    #print num
    for i in range(2,3):
        r1=0 
        r2=0 
        c=0
        for sub in combinations(num,i):
            m=[]
            for j in sub:
                if j[1]=='up':
                    m.append(j[1])
                    j[1]='down'
                else:
                    m.append(j[1])
                    j[1]='up'
            #calculate R for flipped netork
            r1=r1+reliability(num)
            #revert back the link states
            q=0
            for w in sub:
                w[1]=m[q]
                q=q+1
            #calculate R for original network
            r2=r2+reliability(num)
            c=c+1
        r1=r1/float(c)
        r2=r2/float(c)
        print r1,r2
    return


def reliability(num=[[]]):
    r=0
    for i in range(0,len(num)):
        if num[i][1]=='up':
            r=r+num[i][0]
    return r


if __name__ == '__main__':
    main()