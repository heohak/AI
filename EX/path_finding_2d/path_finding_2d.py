
from queue import Queue, PriorityQueue
import time


def h(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def bfs(map_data, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        neighbors = [
            (current[0] - 1, current[1]), (current[0] + 1, current[1]),
            (current[0], current[1] - 1), (current[0], current[1] + 1)
        ]

        for next in neighbors:
            if 0 <= next[0] < len(map_data) and 0 <= next[1] < len(map_data[0]) and map_data[next[0]][
                next[1]] != '*' and next not in came_from:
                frontier.put(next)
                came_from[next] = current

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

def greedy(map_data, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        neighbors = [
            (current[0] - 1, current[1]), (current[0] + 1, current[1]),
            (current[0], current[1] - 1), (current[0], current[1] + 1)
        ]

        for next in neighbors:
            if 0 <= next[0] < len(map_data) and 0 <= next[1] < len(map_data[0]) and map_data[next[0]][
                next[1]] != '*' and next not in came_from:
                priority = h(next, goal)
                frontier.put((priority, next))
                came_from[next] = current

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path


def astar(map_data, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        neighbors = [
            (current[0] - 1, current[1]), (current[0] + 1, current[1]),
            (current[0], current[1] - 1), (current[0], current[1] + 1)
        ]

        for next in neighbors:
            if 0 <= next[0] < len(map_data) and 0 <= next[1] < len(map_data[0]) and map_data[next[0]][next[1]] != '*':
                new_cost = cost_so_far[current] + 1

                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + h(next, goal)
                    frontier.put((priority, next))
                    came_from[next] = current

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

def read_map(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]


if __name__ == '__main__':
        map_sizes = ['small', 'medium', 'large']
        map_files = {
            'small': 'cave300x300',
            'medium': 'cave600x600',
            'large': 'cave900x900'
        }

        positions = {
            'small': ((2, 2), (295, 257)),
            'medium': ((2, 2), (598, 595)),
            'large': ((2, 2), (898, 895))
        }

        for size in map_sizes:
            print(f"Testing on {size.upper()} map...")

            map_data = read_map(map_files[size])

            # Define start and goal positions
            start, goal = positions[size]

            # Test BFS
            print("Running BFS...")
            start_time = time.time()
            path = bfs(map_data, start, goal)
            # print("BFS path:", path)
            print("Time taken:", time.time() - start_time)
            print("Iterations:", len(path))
            print("Path length:", len(path) - 1)
            print("------")

            # Test Greedy Search
            print("Running Greedy Search...")
            start_time = time.time()
            path = greedy(map_data, start, goal)
            # print("Greedy path:", path)
            print("Time taken:", time.time() - start_time)
            print("Iterations:", len(path))
            print("Path length:", len(path) - 1)
            print("------")

            # Test A* Search
            print("Running A* Search...")
            start_time = time.time()
            path = astar(map_data, start, goal)
            # print("A* path:", path)
            print("Time taken:", time.time() - start_time)
            print("Iterations:", len(path))
            print("Path length:", len(path) - 1)
            print("------")
