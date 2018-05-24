

def explore(node, path):
    if not node:
        return
    if not (node.left or node.right):
        print_path(node, path)
        return
    path.append(node)
    for kid in (node.left, node.right):
        if kid:
            explore(kid, path)
    path.pop()
 
def print_path(node, path):
    prepath = ' '.join([str(n.val) for n in path])
    if prepath:
        prepath += ' '
    print prepath + str(node.val)
    
def  printAllPaths(root):
    path = list()
    explore(root, path)
