from heapq import heappush, heappop

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(n, grid, start, target):

    pq = []
    heappush(pq, (manhattan_distance(start, target), 0, start, [start]))

    visited = set()
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while pq:
        est_total_cost, cost_so_far, current, path = heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == target:
            return path

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc #-------------
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    new_cost = cost_so_far + 1
                    new_est_cost = new_cost + manhattan_distance((nr, nc), target)
                    heappush(pq, (new_est_cost, new_cost, (nr, nc), path + [(nr, nc)]))

    return None

# ---------------- MAIN PROGRAM ----------------
n = int(input("Maze grid: "))
grid = [tuple(map(int, input().split())) for _ in range(n)]
start_x, start_y = map(int, input("Starting position: ").split())
end_x, end_y = map(int, input("Destination position: ").split())

path = a_star_search(n, grid, (start_x, start_y), (end_x, end_y))

result = (' '.join(f'({c}, {r})' for r, c in path)) or ('No path found!')
print(result)

# Dawoodur Rahman Owns this snippet of codes