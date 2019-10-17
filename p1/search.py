import sys
txt_file = sys.argv[1]
graph_txt = open(txt_file, "r")
graph = {}
adjacents = {}
def fill_edge(row):
    key_indis = 3
    value_indis = 5
    edge = {}
    adjacent = []
    while value_indis < len(row) :
        if int(row[value_indis]) != 0:
            edge[row[key_indis]]= int(row[value_indis])
        key_indis += 5
        value_indis +=5
    add_edge(row[0], edge)
    for key, value in edge.items():
        if value != 0:
            adjacent.append(key)
    add_adjacent(row[0], adjacent)

def add_edge(i,edge):
    graph[i] = edge

def add_adjacent(i,adjacent):
    adjacents[i] = adjacent
for row in graph_txt:
    fill_edge(list(row))

def bfs(graph, start, end):

    queue = [(start,[start])]
    visited = set()

    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)
        for node in graph[vertex]:
            if node == end:
                return path + [end]
            else:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

def ucs(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        #return distances[start], path[::-1]
        return path[::-1]
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxsize)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return ucs(graph,closestnode,end,visited,distances,predecessors)

start = input("Please enter the start state : ")
goal = input("Please enter the goal state : ")

bfs_list = bfs(adjacents,start,goal)
strBfs = ''.join(str(str1) for str1 in bfs_list)
print("BFS : ", end="")
print(*strBfs, sep=" - ")

dfs_list = dfs(adjacents,start,goal)
strDfs = ''.join(str(str2) for str2 in dfs_list)
print("DFS : ", end="")
print(*strDfs, sep=" - ")

ucs_list = ucs(graph,start,goal)
strUcs = ''.join(str(str3) for str3 in ucs_list)
print("UCS : ", end="")
print(*strUcs, sep=" - ")
