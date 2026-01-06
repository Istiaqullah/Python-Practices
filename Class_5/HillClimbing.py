def heuristic(node,goal):
    distance=abs(node[0]-goal[0])+abs(node[1]-goal[1])
    return distance

def get_neighbor(node, graph):
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    valid_neighbor = []

    for move in moves:
        tentative_neighbor = (node[0] + move[0], node[1] + move[1])
        if (0 <= tentative_neighbor[0] <= 4 and
            0 <= tentative_neighbor[1] <= 4 and
            graph[tentative_neighbor[0]][tentative_neighbor[1]] == 0):
            valid_neighbor.append(tentative_neighbor)

    return valid_neighbor

def hill_climbing(graph,start,goal):
    curr=start
    while True:
      neighbors=get_neighbor(curr,graph)
      current_min= float('inf')
      current_best=None

      for neighbor in neighbors:
          temp=heuristic(neighbor,goal)
          if temp<current_min:
              current_min=temp
              current_best=neighbor

      if current_min<heuristic(curr,goal):
          curr=current_best
      else:
          break

    return curr

graph=[[0,1,0,0,0],
       [0,1,0,1,0],
       [0,0,0,1,0],
       [1,1,0,1,0],
       [0,1,0,1,0],
       ]
start,goal=(0,0),(4,4)

answer=hill_climbing(graph,start,goal)
print(answer)