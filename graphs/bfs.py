import queue


class Vertex(object):
    def __init__(self, label):
        self.neighbours = list()
        self.label = label
        
def generate_graph():
    vertices = list()
    for i in range(1, 14):
        vertices.append(Vertex(i))
    vertices[0].neighbours.append(vertices[4])
    vertices[0].neighbours.append(vertices[1])
    vertices[4].neighbours.append(vertices[3])
    vertices[1].neighbours.append(vertices[3])
    vertices[3].neighbours.append(vertices[6])
    vertices[3].neighbours.append(vertices[7])
    vertices[2].neighbours.append(vertices[5])
    vertices[5].neighbours.append(vertices[8])
    vertices[5].neighbours.append(vertices[9])
    vertices[8].neighbours.append(vertices[10])
    vertices[8].neighbours.append(vertices[11])
    return vertices

def print_component(component):
    print('Printing component')
    for vertex in component:
        print(vertex.label)
    print('Finished printing component\n')

def bfs(v_start, v_target):
    print('Building path from {} to {}'.format(v_start.label, v_target.label))
    distances = dict()
    prev = dict()
    q = queue.Queue()

    distances[v_start.label] = 0
    q.put(v_start)

    while not q.empty():
        v = q.get()
        if v.label == v_target.label:
            return build_path(prev, v_target)
        for i in v.neighbours:
            if not distances.get(i.label):
                distances[i.label] = distances[v.label] + 1
                prev[i.label] = v
                q.put(i)

    return []

def build_path(prev, target):
    path = list()
    cur = target
    while prev.get(cur.label):
        path.append(cur)
        cur = prev[cur.label]

    path.append(cur)
    path.reverse()
    return path


if __name__ == '__main__':
    vertices = generate_graph()
    path = [v.label for v in bfs(vertices[0], vertices[6])]
    print(path)
