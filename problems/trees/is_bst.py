def  isBST(root):
    if root is None:
        return True
    
    if ((root.left is None) or (root.left.val < root.val)) and ((root.right is None) or (root.right.val > root.val)) and isBST(root.left) and isBST(root.right):
        return True
    return False

