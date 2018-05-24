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

def  BSTtoLL(node):
    st, end = transform(node)
    st.left = end
    end.right = st
    return node

