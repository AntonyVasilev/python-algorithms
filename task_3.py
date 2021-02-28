"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

from random import randint


def dfs(start, visited, prev, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            prev[u] = start
            dfs(u, visited, prev, g)
    return visited, prev


def graph_search(g, start):
    n = len(graph)
    visited = [False] * n
    prev = [None] * n

    visited, prev = dfs(start, visited, prev, g)
    print_result(visited, prev, g)


def print_result(visited, prev, g):
    visited_vertexes = [i for i in range(len(g)) if visited[i]]

    print('Граф:')
    for j in range(len(g)):
        print(f'{j}: {g[j]}')
    print('*' * 50)
    print(f'Посещенные вершины графа: {visited_vertexes}')
    # print(visited)
    # print(prev)


def create_graph(vertex_num):
    new_graph = []
    for i in range(vertex_num):
        k = randint(1, vertex_num - 1)
        temp_list = []
        while len(temp_list) < k:
            new_num = randint(0, vertex_num - 1)
            if new_num != i and new_num not in temp_list:
                temp_list.append(new_num)
        new_graph.append(temp_list)

    return new_graph


if __name__ == '__main__':
    # graph = create_graph(10)
    graph = [
        [1, 4, 5],
        [2, 3],
        [8],
        [1, 7],
        [1],
        [0, 4, 6],
        [3, 4],
        [6],
        [2, 3, 6],
        [7, 8]
    ]

    graph_search(graph, 9)
    # print(prev)
    # print(visited)


