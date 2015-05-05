from itertools import combinations
import networkx as nx
import random
G=nx.dense_gnm_random_graph(5,10)
t=G.edges()
p=0.9
a=0
r=0
s='nothing'

def main():
    num=[]
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

    for i1 in range(1,99):
        r1=0
        r2=0
        for freq in range(1,600):

            index=random.sample(range(1024), i1)

            for a1 in range(0,len(index)):
                if num[index[a1]][1]=='up':
                   num[index[a1]][1]='down'
                else:
                    num[index[a1]][1]='up'

            r1=r1+reliability(num)

            for a2 in range(0,len(index)):
                if num[index[a2]][1]=='up':
                    num[index[a2]][1]='down'
                else:
                    num[index[a2]][1]='up'

            r2=r2+reliability(num)
        print r1/float(600),r2/float(600)


def reliability(num=[[]]):
    r=0     
    for i in range(0,len(num)):
        if num[i][1]=='up':
            r=r+num[i][0]
    return r

if __name__ == '__main__':
    main()