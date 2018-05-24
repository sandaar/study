def find_path(node, target, path):
    if node is None:
        return False
    path.append(node)
    if node.val == target:
        return True
    if (node.left != None and find_path(node.left, target, path)) or (node.right != None and find_path(node.right, target, path)):
        return True
    path.pop()
    return False

def print_path(path):
    print(' '.join((str(p.val) for p in path)))
    
def get_lca(path1, path2):
    i = 0
    #print_path(path1)
    #print_path(path2)
    while i < len(path1) or i < len(path2):
        if i >= len(path1):
            return path2[i - 1]
        if i >= len(path2):
            return path1[i - 1]
        if path1[i] != path2[i]:
            return path1[i - 1]
        i += 1
    
    
    

def  findLCA(root, n1, n2):
    path1 = list()
    path2 = list()
    find_path(root, n1, path1)
    find_path(root, n2, path2)
    lca = get_lca(path1, path2)
    return lca
