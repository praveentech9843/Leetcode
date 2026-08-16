class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        temp = self.head
        count = 0

        while temp is not None:
            if count == index:
                return temp.val

            count += 1
            temp = temp.next

        return -1


    def addAtHead(self, val):
        newnode = Node(val)

        newnode.next = self.head
        self.head = newnode


    def addAtTail(self, val):
        newnode = Node(val)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = newnode


    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        newnode = Node(val)
        temp = self.head

        count = 0

        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            return

        newnode.next = temp.next
        temp.next = newnode


    def deleteAtIndex(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp.next is not None and count < index - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            return

        temp.next = temp.next.next