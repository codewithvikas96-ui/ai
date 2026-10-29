# AIM: Implement IDDFS Algorithm

from RMP import dict_gn

start = 'Arad'
goal = 'Bucharest'


def DLS(city, visited, depth, limit):
    print(city, end=' ')

    if city == goal:
        return True

    if depth == limit:
        return False

    visited.append(city)

    for neighbor in dict_gn[city]:
        if neighbor not in visited:
            if DLS(neighbor, visited, depth + 1, limit):
                return True

    return False


def IDDFS():
    for limit in range(9):
        print("\nSearching at Limit:", limit)

        if DLS(start, [], 0, limit):
            print("\nGoal Found!")
            return

        print("\nNot Found!")


IDDFS()
