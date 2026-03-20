# ---------------------------------------------------------
# A* Search Algorithm - Assignment (1)
# Deema Mohammed AL-Maqadma
# ---------------------------------------------------------

import heapq

# ---------------------------------------------------------
# 1. Define the grid (map)
# ---------------------------------------------------------
# S = Start
# G = Goal
# . = Free cell
# # = Obstacle

grid = [
    ['S', '.', '.', '.'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', 'G']
]

rows = len(grid)
cols = len(grid[0])

# Allowed movements: up, down, left, right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# ---------------------------------------------------------
# 2. Find Start (S) and Goal (G)
# ---------------------------------------------------------
start = None
goal = None

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'G':
            goal = (r, c)

# ---------------------------------------------------------
# 3. Heuristic Function (Manhattan Distance)
# ---------------------------------------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# ---------------------------------------------------------
# 4. A* Algorithm
# ---------------------------------------------------------
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    print("\n--->>>  Starting A* Search <<<---\n")

    while open_list:
        f, current = heapq.heappop(open_list)
        print(f"---> Expanding node {current} with f = {f}")

        if current == goal:
            print("\n---> Goal reached! Reconstructing path...\n")
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for d in directions:
            nr, nc = current[0] + d[0], current[1] + d[1]

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                neighbor = (nr, nc)
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    h = heuristic(neighbor, goal)
                    f = tentative_g + h

                    print(f"  Neighbor {neighbor}: g={tentative_g}, h={h}, f={f}")

                    heapq.heappush(open_list, (f, neighbor))
                    came_from[neighbor] = current

    return None

# ---------------------------------------------------------
# 5. Run A* and print final path
# ---------------------------------------------------------
path = a_star(start, goal)

print("--->>> Final Path Found by A*:")
print(path)
print()