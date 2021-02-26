"""
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""
from collections import deque

gr = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    length = len(graph)
    path = [[] for _ in range(length)]
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    path[i].append(start)
                    # print(parent)
                    # print(min_cost)
                    # input()

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, path


def get_path(path, start):
    length = len(path)
    is_full_path = [False for _ in range(length)]
    # Добавляю номер конечной вершины в список path_list
    path_list = [deque([i]) for i in range(8)]
    stop_sign = False

    while not stop_sign:

        # Добавляю путь до вершины
        for j, is_done in enumerate(is_full_path):
            if not is_done:
                prev_path = path_list[j][0]
                temp_list = reversed(path[prev_path])
                for num in temp_list:
                    path_list[j].appendleft(num)

        # Проверяю достиг ли путь точки старта
        for i, path_i in enumerate(path_list):
            if path_i[0] == start or path_i[0] == i:
                is_full_path[i] = True

        stop_sign = all(is_full_path)

    # Если пути нет или это начальная точка, убираю номер конечной вершины
    for el in path_list:
        if len(el) == 1:
            el.pop()

    return path_list


st = int(input('От какой вершины идти: '))
# st = 0
cost_list, shortest_path = dijkstra(gr, st)
shortest_path = get_path(shortest_path, st)

print('*' * 70)
n = 0
for cost, current_path in zip(cost_list, shortest_path):
    print(f'Кратчайший путь между вершинами {st} и {n}: {list(current_path)}, растояние: {cost}')
    n += 1
