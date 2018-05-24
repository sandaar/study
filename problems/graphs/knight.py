import queue

def possible_moves(m, rows, cols):
    result = list()
    if m[0] - 1 >= 0 and m[1] - 2 >= 0:
        result.append((m[0] - 1, m[1] - 2))
    if m[0] - 1 >= 0 and m[1] + 2 < cols:
        result.append((m[0] - 1, m[1] + 2))
    if m[0] + 1 < rows and m[1] - 2 >= 0:
        result.append((m[0] + 1, m[1] - 2))
    if m[0] + 1 < rows and m[1] + 2 < cols:
        result.append((m[0] + 1, m[1] + 2))
    if m[1] - 1 >= 0 and m[0] - 2 >= 0:
        result.append((m[0] - 2, m[1] - 1))
    if m[1] - 1 >= 0 and m[0] + 2 < rows:
        result.append((m[0] + 2, m[1] - 1))
    if m[1] + 1 < cols and m[0] - 2 >= 0:
        result.append((m[0] - 2, m[1] + 1))
    if m[1] + 1 < cols and m[0] + 2 < rows:
        result.append((m[0] + 2, m[1] + 1))
    return result
    
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    start = (start_row, start_col)
    end = (end_row, end_col)
    q = queue.Queue()
    distances = dict()
    
    distances[start] = 0
    q.put(start)
    
    while not q.empty():
        v = q.get()
        if v == end:
            #print(distances)
            return distances[v]
        for m in possible_moves(v, rows, cols):
            if m not in distances:
                distances[m] = distances[v] + 1
                q.put(m)
        #print(distances)
    return -1
            

