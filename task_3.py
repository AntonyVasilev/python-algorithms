"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

from random import randint


def _dfs_1(start, visited, graph):
    visited[start] = True
    for vertex in graph[start]:
        if not visited[vertex]:
            _dfs_1(vertex, visited, graph)
    return visited


def graph_1_search(graph, start):
    n = len(graph)
    visited = [False] * n

    visited = _dfs_1(start, visited, graph)
    print_result(visited, graph, 1)


def _dfs_2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for vertex in graph[start] - visited:
        _dfs_2(graph, vertex, visited)
    return visited


def graph_2_search(graph, start):
    visited = _dfs_2(graph, start)
    print_result(list(visited), graph, 2)


def print_result(visited, graph, variant):
    visited_vertexes = None

    print('\n\n')
    print('-' * 60)
    print(f'Граф {variant}:')

    if variant == 1:
        visited_vertexes = [i for i in range(len(graph)) if visited[i]]
        for j in range(len(graph)):
            print(f'{j}: {graph[j]}')

    elif variant == 2:
        visited_vertexes = sorted(visited)
        for key in graph.keys():
            print(f'{int(key)}: {graph[key]}')

    print('*' * 60)
    print(f'Посещенные вершины графа: {visited_vertexes}')


def create_graph(vertex_num):
    new_graph_list = []
    new_graph_dict = {}

    for i in range(vertex_num):
        k = randint(1, vertex_num // 3)
        temp_list = []
        temp_set = set()

        while len(temp_list) < k:
            new_num = randint(0, vertex_num - 1)
            if new_num != i and new_num not in temp_list:
                temp_list.append(new_num)
                temp_set.add(str(new_num))

        new_graph_list.append(temp_list)
        new_graph_dict[str(i)] = temp_set

    return new_graph_list, new_graph_dict


if __name__ == '__main__':
    # graph_1 - списки смежности через list, graph_2 - через dict и set
    graph_1, graph_2 = create_graph(10)
    graph_1_search(graph_1, 0)
    graph_2_search(graph_2, '0')
