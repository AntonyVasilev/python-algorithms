"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n = int(input('Введите количество друзей: '))
is_shacked = [[False for _ in range(n)] for _ in range(n)]
graph = [[1 for _ in range(n)] for _ in range(n)]
for k in range(n):
    graph[k][k] = 0

print(*graph, sep='\n')
shacks_count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not is_shacked[i][j]:
            shacks_count += 1
            is_shacked[j][i] = True

print(f'Количество рукопожатий: {shacks_count}')

# Следующая формула применяется в статистике для определения количества взаимных проверок.
# Здесь использую ее для проверки результата.
print(f'Количество рукопожатий: {n * (n-1) // 2}')
