# Complete the function below.

def transform(node):
    if not node:
        return None, None
        
    if not (node.right or node.left):
        return node
    
    if node.left:
        st1, end1 = transform(node.left)
    else:
        st1, end1 = node, node
    if node.right:
        st2, end2 = transform(node.right)
    else:
        st2, end2 = node, node
    
    node.left = end1
    node.right = st2
    
    return st1, end2

def print_ll(node):
    cur = node
    while cur.right != node:
        print(cur.val)
        cur = cur.val
    print(cur.val)
    
def  BSTtoLL(node):
    st, end = transform(node)
    st.left = end
    end.right = st
    print_ll(node)

