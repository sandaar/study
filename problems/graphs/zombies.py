def explore(i, zombies, seen):
    seen[i] = True
    
    for j in range(len(zombies)):
        if j not in seen and zombies[i][j] == '1':
            explore(j, zombies, seen)
            
def zombieCluster(zombies):
    count = 0
    seen = dict()
    for i in range(len(zombies)):
        if i not in seen:
            explore(i, zombies, seen)
            count += 1
    return count

