# AIM: Implement A* Search Algorithm

import queue
from RMP import dict_gn, dict_hn

start = 'Arad'
goal = 'Bucharest'


def get_fn(path):
    cities = path.split(" , ")
    cost = sum(
        dict_gn[cities[i]][cities[i + 1]]
        for i in range(len(cities) - 1)
    )
    return cost + dict_hn[cities[-1]]


def main():
    q = queue.PriorityQueue()
    q.put((get_fn(start), start, start))

    while not q.empty():
        total, path, city = q.get()

        if city == goal:
            print("The A* path with total cost is:")
            print(path, "::", total)
            return

        for neighbor in dict_gn[city]:
            new_path = path + " , " + neighbor
            q.put((get_fn(new_path), new_path, neighbor))


main()
