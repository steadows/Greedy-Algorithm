def check_color(color_list):
    color = 1
    while True:
        if color not in color_list:
            return color
        color += 1


def get_neighbors(graph, vertex):
    i = vertex
    neighbors_list = graph[i]
    return neighbors_list


def get_colors(colors, neighbors):
    neighbor_colors = []
    for n in neighbors:
        if colors.__contains__(n):
            neighbor_colors.append(colors[n])
    return neighbor_colors


def greedy(graph, vertices):
    colors = {}
    for vertex in vertices:
        v = get_neighbors(graph, vertex)
        if any(key in colors for key in v):
            neighbor_colors = get_colors(colors, v)
            colors[vertex] = check_color(neighbor_colors)
        else:
            colors[vertex] = 1
    print(colors)
    return(colors)

# greedy({'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C']}, ['A', 'D', 'B', 'C'])
greedy({'A':['B','C','D','E'], 'B':['A','C','E'], 'C':['A','B','D'], 'D':['A','C'], 'E':['A','B']}, ['E', 'D', 'B', 'C', 'A'])