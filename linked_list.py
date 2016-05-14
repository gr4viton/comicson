import sys
from main import ComicDownloader

class Node(object):
    count = 0
    id = None
    data = None
    next = None
    prev = None
    downloader = ComicDownloader()

    def __init__(self, id, next=None, prev=None):
        Node.count += 1
        self.update_data(id)
        self.next = next
        self.prev = prev

    def add_next_on_tail(self):
        new_id = self.id + 1
        if self.next is None:
            tail = self.next = Node(new_id, prev=self)
        else:
            tail = self.next.add_next_on_tail()
        return tail

    def add_prev_on_tail(self):
        new_id = self.id - 1
        if self.prev is None:
            tail = self.prev = Node(new_id, next=self)
        else:
            tail = self.prev.add_prev_on_tail()
        return tail

    def update_data(self, id):
        self.id = id
        # self.data = 'name'+str(id)
        self.data = self.downloader.get_strip(self.id)

    def __str__(self):
        txt = '['
        txt += 'id={0:>5},'.format(self.id)
        txt += 'data={}'.format(self.data)
        txt += ']'
        return txt
        # return "id=\t{}, data=\t[{0:<16}]".format(self.id, self.data)

class StripBuffer(object):
    side_count = 0 # number of nodes on each side of active
    count = 0

    active = None
    tail_back = None
    tail_front = None

    # default_data = 'node_data'

    def __init__(self, current_id=340, size=5):
        self.set_buffer_size(current_id, size)


    def set_buffer_size(self, current_id=340, size=5):

        if divmod(size, 2) == 0:
            print('Only odd size allowed!')
            return False

        self.side_count = int((size-1)/2)
        if self.active is not None:
            self.delete_buffer()

        id = current_id
        self.active = Node(id)
        node = self.active

        tail_front = node.add_next_on_tail()
        tail_back = node.add_prev_on_tail()
        for q in range(self.side_count-1):
            tail_front = tail_front.add_next_on_tail()
            tail_back = tail_back.add_prev_on_tail()


        # circular list
        tail_front.next = tail_back
        tail_back.prev = tail_front
        self.tail_back = tail_back
        self.tail_front = tail_front

        self.count = Node.count
        print('Buffer count: [%d]' % (self.count,))

    def delete_buffer(self):
        pass

    def next_strip(self):
        new_front_id = self.active.id + 1 + self.side_count

        self.active = self.active.next
        self.tail_front = self.tail_front.next
        self.tail_back = self.tail_back.next

        # the new tail_front strip - to reload
        self.tail_front.update_data(new_front_id )

    def prev_strip(self):
        new_back_id = self.active.id - 1 - self.side_count

        self.active = self.active.prev
        self.tail_front = self.tail_front.prev
        self.tail_back = self.tail_back.prev

        # the new tail_back strip - to reload
        self.tail_back.update_data(new_back_id)


    def __str__(self):
        txt = ''
        node = self.active
        txt += '{} = tail_front\n'.format(str(self.tail_front))
        txt += '{} = active\n'.format(str(self.active))
        txt += '{} = tail_back\n'.format(str(self.tail_back))

        txt += 'Printing forward from active!\n'
        node = node.next
        for q in range(self.count-1):
            txt += '{} = previous->next\n'.format(str(node))
            node = node.next
            # if node == self.active:
        if node == self.active:
            txt += 'Got to the begining = circular linked list!\n'

        return txt

if __name__ == '__main__':
    sb = StripBuffer(current_id=100, size=5)
    # sb.set_buffer_size(current_id=0, size=5)
    # sb.print_ids()
    print(sb)
    x = 50
    for q in range(x):
        print('Called next strip')
        sb.next_strip()
        print(sb)
    for q in range(x):
        print('Called prev strip')
        sb.prev_strip()
        print(sb)
    # for q in range(10):
    #     cll.add('list{}'.format(q))


    # cll.add('list0')




    # def __contains__(self, id):    # example algorithm, implements the "in" operator
    #     current = self.active.next
    #     while current != self.active:
    #         if current.id == id:
    #             return True
    #     return False