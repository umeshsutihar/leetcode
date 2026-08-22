class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        # Traverse from the closer side
        if index < self.size // 2:
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        new_node = Node(val)

        new_node.prev = curr.prev
        new_node.next = curr

        curr.prev.next = new_node
        curr.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.head

        if index < self.size // 2:
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)