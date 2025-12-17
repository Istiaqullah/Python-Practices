import heapq
def dijkstra(maze,start,end):
    r,c=len(maze),len(maze[0])
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    pq=[(0,start)]
    distances={start:0}
    parent={start:None}

    while pq:
        curr,(x,y)=heapq.heappop(pq)
        if (x,y)==end:
            path=[]
            current=end
            while current is not None:
                path.append(current)
                current=parent[current]
            path.reverse()
            return path

        for dx,dy in directions:
            nx,ny=x+dx, y+dy
            if 0<=nx<r and 0<=ny<c and maze[nx][ny]==0:
                new_dist=curr+1
                if new_dist< distances.get((nx,ny),float('inf')):
                    distances[(nx,ny)]=new_dist
                    parent[(nx,ny)]=(x,y)
                    heapq.heappush(pq,(new_dist,(nx,ny)))
    return None


print("Enter grid size:")
rows, cols = map(int, input().split())

print("enter the rows one by one:")
maze = [list(map(int, input(f"Row {i + 1}: ").split())) for i in range(rows)]

print("start:")
start = tuple(map(int, input().split()))

print("end:")
end = tuple(map(int, input().split()))
path = dijkstra(maze, start, end)

if path:
    print("Path found:")
    print(path)
else:
    print("not found.")