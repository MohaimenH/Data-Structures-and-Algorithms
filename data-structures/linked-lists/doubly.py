from singly import Node, SinglyLinkedList


class DNode(Node):

    def __init__(self, value, prev_node=None, next_node=None):
        super().__init__(value, next_node=next_node)
        self.prev_node = prev_node

    def set_prev_node(self, node):
        self.prev_node = node

    def get_prev_node(self):
        return self.prev_node

class DoublyLinkedList(SinglyLinkedList):

    def __init__(self):
        self.head = DNode(None, None, None)
        self.tail = DNode(None, None, None)

        self.initialized = False


    def insert_at_head(self, value):

        elem = DNode(value, self.head, self.head.get_next_node())

        if(not self.initialized):
            self.tail.set_prev_node(elem)
            elem.set_next_node(self.tail)
            self.initialized = True
        else:
            self.head.get_next_node().set_prev_node(elem)

        self.head.set_next_node(elem)

        # print(elem)

    
    def insert_at_tail(self, value):

        elem = DNode(value, self.tail.get_prev_node(), self.tail)

        if(not self.initialized):
            self.head.set_next_node(elem)
            elem.set_prev_node(self.head)
            self.initialized = True
        else:
            self.tail.get_prev_node().set_next_node(elem)

        self.tail.set_prev_node(elem)

        # print(elem)

    def __repr__(self) -> str:
        
        result = ''
        x = self.head.get_next_node()

        while x != None and x != self.tail and x != self.head:
            result += str(x.get_value()) + ' <-> '
            x = x.get_next_node()
        
        return result[:-4].strip()
    
    def reverseRepr(self) -> str:
        result = ''
        x = self.tail.get_prev_node()

        while x != None and x != self.tail and x != self.head:
            result += str(x.get_value()) + ' <-> '
            x = x.get_prev_node()

        return result[:-4].strip()
    
    def get_head_elem(self):
        return self.head.get_next_node().get_value()
    
    def get_tail_elem(self):
        return self.tail.get_prev_node().get_value()


if __name__ == "__main__":
    l = DoublyLinkedList()

    # l.insert_at_tail(30)
    l.insert_at_head(1)
    l.insert_at_head(2)
    l.insert_at_head(3)

    l.insert_at_tail(4)

    l.insert_at_head(20)

    l.insert_at_tail(30)

    l.insert_at_head(100)

    l.insert_at_tail(500)

    print(l.get_head_elem())
    print(l.get_tail_elem())
    
    print(l.reverseRepr())