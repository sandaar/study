#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

def  addNumbers(l1, l2):
    head = None
    rem = 0 
    tenth = 0
    
    while l1 or l2:
        if l1 and l2:
            total = l1.val + l2.val + tenth
        elif l1:
            total = l1.val + tenth
        else:
            total = l2.val + tenth
        tenth = total // 10
        rem = total % 10
        
        #print("Total {}".format(total))
        #print("rem {}".format(rem))
        #print("tenth {}".format(tenth))
        
        if not head:
            #print("At head adding {}".format(rem))
            node = LinkedListNode(0)
            head = tail = node
            node.val = rem
            #print(node.val)
        else:
            #print("New node adding {}".format(rem))
            node = LinkedListNode(rem)
            #print(node.val)
            tail.next = node
            tail = tail.next
            
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    if tenth:
        node = LinkedListNode(tenth)
        tail.next = node
        tail = tail.next
    
    #print("Result")
    myres = head
    while myres:
        #print(myres.val)
        myres = myres.next
        
    return head
