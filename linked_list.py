import sys

class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "Node[Data = %s]" % (self.data,)

class CircularLinkedList(object):
    count = None
    active = None
    rightmost = None
    leftmost = None

    def __init__(self):
        self.active = Node(None, None) # this is the sentinel node!
        self.active.next = self.active   # link it to itself

    def add(self, data):             # no special case code needed for an empty list
        self.active.next = Node(data, self.active.next)

    def __contains__(self, data):    # example algorithm, implements the "in" operator
        current = self.active.next
        while current != self.active:
            if current.data == data:
                return True
        return False

    def __str__(self):
        current = self.active.next
        txt = ''
        while current != self.active:
            if current.data == CircularLinkedList.active.data:
                return txt
            current = current.next
        return False

if __name__ == '__main__':
    cll = CircularLinkedList()
    for q in range(10):
        cll.add('list{}'.format(q))


    # cll.add('list0')