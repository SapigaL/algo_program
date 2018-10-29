import collections
import math

i = 0
max_in_min = math.inf
max_weight = math.inf
servers_len = 0


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight

    # --------
    len_visited = len(visited)
    for index in range(0, servers_len):
        for visit in range(0, len_visited):
            if str(servers[int(index)]) == str(visit) and None != visited.get(str(visit)):
                visited.pop(str(visit))
    len_client = len(client)
    min_weight: int = 0

    for nubmer in range(0, len_client):
        max_weight = visited.get(str(client[nubmer]))
        if min_weight != None and max_weight!=None:
            if int(min_weight) < max_weight:
                min_weight = max_weight

    return min_weight


if __name__ == "__main__":
    G = Graph()
    file = open('discnt_in')
    lines = [line.rstrip('\n') for line in file]
    node_adge = []
    client = []
    servers = []
    rows = []
    min_weight = 0

    for amount in lines[0].split(" "):
        node_adge.append(int(amount))

    for nubmer in lines[1].split(" "):
        client.append(int(nubmer))
    client_len = len(client)
    for node in range(node_adge[0]):
        i = i + 1
        servers.append(int(i))
        for index in range(0, client_len):
            if int(i) == client[int(index)]:
                servers.remove(i)
    servers_len = len(servers)

    for node in range(0, servers_len):
        G.add_node(str(servers[node]))

    for n in range(node_adge[1]):
        for row in lines[n + 2].split(" "):
            rows.append(int(row))
        G.add_edge(str(rows[0]), str(rows[1]), int(rows[2]))
        G.add_edge(str(rows[1]), str(rows[0]), int(rows[2]))
        rows = []

    for node in G.nodes:
        min_weight = dijsktra(G, node)
        if None != min_weight and min_weight < max_in_min:
            max_in_min = min_weight
    my_file = open("discnt_out", "w")
    my_file.write(str(max_in_min))
    my_file.close()
    print(max_in_min)
