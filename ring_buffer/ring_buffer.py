class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def delete(self):
        if self.next:
            self.next = None


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.head = None
        # One before the node to die
        self.prekill = None

    def append(self, item):
        # When we aren't at capciity
        if self.length < self.capacity:
            self.length += 1
            # If it doesn't exist make it and point to itself
            if self.head == None:
                self.head = Node(item)
                self.head.next = self.head
            # If there is a node navigate to the node before the end
            # add a new node and make it the prekill
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = Node(item)
                current = current.next
                current.next = self.head
                self.prekill = current
        # All spots are filled
        else:
            # The next one to be killed after this addition
            deathRow = self.prekill.next.next
            # The one about to die
            kill = self.prekill.next
            self.prekill.next = Node(item)
            if self.head == kill:
                self.head = self.prekill.next
            kill.delete()
            # Shift Node before the node to die one over
            self.prekill = self.prekill.next
            # Connect that to the new victum
            self.prekill.next = deathRow

    def get(self):
        package = []
        current = self.head
        while current.next != self.head:
            package.append(current.value)
            current = current.next
        package.append(current.value)
        return package
