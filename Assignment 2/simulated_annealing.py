import math
import random
def dist(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def path_cost(route):
    total=0
    for i in range(len(route)-1):
        total+=dist(locations[route[i]], locations[route[i+1]])
    return total
def path(route):
    return " -> ".join(str(x+1) for x in route)

def simulated_annealing():
    route=[0]+random.sample(range(1,N),N-1)+[0]
    best=route[:]
    best_len=path_cost(route)
    T=1000.0
    T_min=float('inf')
    alpha=0.995
    iters=1000
    while T>T_min and iters>0:
        i,j=random.sample(range(1,N),2)
        new_route=route[:]
        new_route[i],new_route[j]=new_route[j], new_route[i]
        d_old=path_cost(route)
        d_new=path_cost(new_route)
        delta=d_new-d_old
        if delta<0 or random.random()<math.exp(-delta/T):
            route=new_route
            if d_new<best_len:
                best=new_route[:]
                best_len=d_new
        T*=alpha
        iters-=1
    return best,best_len

print("Enter N:")
N = int(input())
locations=[]
for i in range(N):
    line=input()
    xy=line.strip().split(" ")
    locations.append((float(xy[0]),float(xy[1])))
print(locations)

print("Simulated annealing")
p,d=simulated_annealing()
print("route:",path(p))
print(f"Total distance:{d}")