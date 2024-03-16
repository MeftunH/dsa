class SinglyLinkedList:


    def __init__(self):


    self.head = None


def append(self, data):


    if not self.head:
    self.head = Node(data)
else:
current = self.head
while current.next:
    current = current.next

current.next = Node(data)


def print_list(self):


    current = self.head

while current:
