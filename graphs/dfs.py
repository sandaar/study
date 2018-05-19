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
    vertices[4].neighbours.append(vertices[6])
    vertices[4].neighbours.append(vertices[7])
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

def dfs(vertices):
    seen = set()

    for v in vertices:
        if v.label not in seen:
            component = list()
            explore(v, seen, component)
            print_component(component)

def explore(vertex, seen, component):
    seen.add(vertex.label)
    component.append(vertex)

    for v in vertex.neighbours:
        if v.label not in seen:
            explore(v, seen, component)

if __name__ == '__main__':
    vertices = generate_graph()
    dfs(vertices)

