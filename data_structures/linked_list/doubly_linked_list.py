class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
 
class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
 
    def get_node(self, index):
        current = self.first
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        if ref_node.next is None:
            self.last = new_node
        else:
            new_node.next = ref_node.next
            new_node.next.prev = new_node
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.first = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        ref_node.prev = new_node
 
    def insert_at_beg(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insert_before(self.first, new_node)
 
    def insert_at_end(self, new_node):
        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            self.insert_after(self.last, new_node)
 
    def remove(self, node):
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next
 
        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev
 
    def display(self):
        current = self.first
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
a_dllist = DoublyLinkedList()
 
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
 
while True:
    print('The list: ', end = '')
    a_dllist.display()
    print()
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
 
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_dllist.insert_at_beg(new_node)
            elif position == 'end':
                a_dllist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_dllist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_dllist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_dllist.insert_before(ref_node, new_node)
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_dllist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_dllist.remove(node)
 
    elif operation == 'quit':
        break
