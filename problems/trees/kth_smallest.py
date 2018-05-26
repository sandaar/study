class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def generate_tree():
    # 1 5 6 10 11 15 20
    #       15
    #   10      20
    # 5   11
    #1 6
    nodes = list()
    nodes.append(TreeNode(1))
    nodes.append(TreeNode(5))
    nodes.append(TreeNode(6))
    nodes.append(TreeNode(10))
    nodes.append(TreeNode(11))
    nodes.append(TreeNode(15))
    nodes.append(TreeNode(20))
    nodes[1].left = nodes[0]
    nodes[1].right = nodes[2]
    nodes[3].left = nodes[1]
    nodes[3].right = nodes[4]
    nodes[5].left = nodes[3]
    nodes[5].right = nodes[6]
    return nodes[5]

def kth_smallest(node, k):
    if not node:
        return
    print(node.data, k)
    if node.left:
        result = kth_smallest(node.left, k)
        if result:
            return result
    if node.right:
        result = kth_smallest(node.right, k)
        if result:
            return result


if __name__ == '__main__':
    root = generate_tree()
    #print(root.data)
    k = 0
    result = kth_smallest(root, k)
    print(result.data)
