import random

D = [[0,2,2,5],[2,0,3,4],[2,3,0,1],[5,4,1,0]]
N = len(D)
pher = [[1]*N for _ in range(N)]
a,b=1,2; evap=0.5; pc=1
best_path, best_dist = None, float('inf')

def probs(c, v):
    p=[(pher[c][i]**a)*((1/D[c][i])**b) if i not in v and D[c][i]>0 else 0 for i in range(N)]
    s=sum(p)
    if s==0: p=[1 if i not in v else 0 for i in range(N)]; s=sum(p)
    return [x/s for x in p]

def wchoice(choices, weights):
    r=random.random()*sum(weights)
    for c,w in zip(choices,weights):
        r-=w
        if r<=0: return c
    return choices[-1]

for _ in range(100):
    paths,dists = [],[]
    for _ in range(4):
        v=[random.randint(0,N-1)]
        while len(v)<N:
            v.append(wchoice(range(N), probs(v[-1], v)))
        v.append(v[0])
        dist=sum(D[v[i]][v[i+1]] for i in range(N))
        paths.append(v); dists.append(dist)
        if dist<best_dist: best_dist,best_path=dist,v
    for i in range(N):
        for j in range(N): pher[i][j]*=1-evap
    for p,d in zip(paths,dists):
        for i in range(len(p)-1): pher[p[i]][p[i+1]]+=pc/d

print("Best Path:", best_path)
print("Best Distance:", best_dist)
