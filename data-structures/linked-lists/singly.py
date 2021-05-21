class Node():

    def __init__(self, value, next_node=None):

        """
        Initializes a Node instance, where value represents the data, 
        and next_node represents the next node.
        """
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_value(self, value):
        self.value = value
    
    def set_next_node(self, node):
        self.next_node = node

class SinglyLinkedList():

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.initialized = False

    
    def insert_at_head(self, value):

        elem = Node(value, self.head.get_next_node())

        if(not self.initialized):
            self.tail.set_next_node(elem)
            self.initialized = True

        self.head.set_next_node(elem)

    
    def insert_at_tail(self, value):

        elem = Node(value, None)

        if(not self.initialized):
            self.head.set_next_node(elem)
            self.initialized = True
        else:
            self.tail.get_next_node().set_next_node(elem)

        self.tail.set_next_node(elem)

    def __repr__(self) -> str:
        
        result = ''
        x = self.head.get_next_node()

        while x != None:
            result += str(x.get_value()) + ' -> '
            x = x.get_next_node()
        
        return result[:-4].strip()

if __name__ == "__main__":
    l = SinglyLinkedList()

    l.insert_at_tail(30)
    l.insert_at_head(1)
    l.insert_at_head(2)
    l.insert_at_head(3)

    l.insert_at_tail(4)

    l.insert_at_head(20)

    l.insert_at_tail(30)

    l.insert_at_head(100)

    l.insert_at_tail(500)

    print(l)