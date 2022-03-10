'''
Implement a singly Linkedlist
Operations:
1. Insertion: First , last, at a given position the linked list
2. Traversal
3. Deletion : First, last, at a given position in the linked list
4. Delete the entire linked list
5. Searching in the linked list
'''

# create a node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # initialize the head and tail of the linked list
        self.head = None
        self.tail = None

    # based on location
    def insert(self, value, position=0):
        # create the node
        new_node = Node(value)

        # insertion of 1st element
        if self.head is None and self.tail is None:
            print(f"Inserting in newly created linked list, value:{value}")
            self.head = new_node
            self.tail = new_node
        else:
            # insertion at 1st position
            if position == 0:
                print(f"Inserting at location 0,value:{value}")
                new_node.next = self.head
                self.head = new_node
            elif position == "last":
                print(f"Inserting at last position,value:{value}")
                # insertion at last position
                self.tail.next = new_node
                self.tail = new_node
            else:
                # insertion at a given position
                print(f"Inserting at location:{position},value:{value}")
                temp = self.head
                count = 1
                while count != position:
                    temp = temp.next
                    count += 1

                new_node.next = temp.next
                temp.next = new_node


    # based on location
    def delete(self, position=1):
        isdeleted = False

        # deletion in an empty list
        if self.head is None and self.tail is None:
            print("Deletion tried on an empty linked list")

        # deletion of last node
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            isdeleted = True

        # deletion at beginning
        elif position == 0:
            self.head = self.head.next
            isdeleted = True

        # deletion at end
        elif position == "last":
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
            isdeleted = True

        # deletion in between
        else:
            temp = self.head
            pos = 1
            while pos != position-1:
                temp = temp.next
                pos += 1
            temp.next = temp.next.next
            isdeleted = True
        return isdeleted

    def traverse(self):
        if self.head is None:
            print("Linked list is empty, nothing to traverse")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end='')
                temp = temp.next
            print()

    def search(self, ele):
        isfound = False
        if self.head is None:
            print("Linked list is empty")
            return isfound, 0
        else:
            temp = self.head
            pos = 1
            while temp is not None:
                if temp.data == ele:
                    isfound = True
                    break
                pos += 1
                temp = temp.next

            return isfound, pos

    def deleteLinkedList(self):
        if self.head is None:
            print("Linked list is empty, nothing to delete")
        else:
            self.head = None
            self.tail = None
            print("Linked list is empty")

sllist = SinglyLinkedList()
sllist.insert(3)            # insertion of 1st element
sllist.insert(1,0)          # insertion at position 1st
sllist.insert(4,'last')     # insertion at last position
sllist.insert(2,1)          # insertion at a given position

sllist.traverse()           # traverse the linked list


# search the element
to_search = [1,3,4,5]
for ele in to_search:
    res, pos = sllist.search(ele)
    if res:
        print(f"Element is found at location:{pos}")
    else:
        print("Linked list is empty or element not found")


sllist.delete(0)          # deletion at 1st position
sllist.traverse()
sllist.delete(2)          # deletion at 2nd position
sllist.traverse()
sllist.delete("last")     # deletion at last position
sllist.traverse()
sllist.delete(0)          # deletion of last element
sllist.traverse()
sllist.delete(0)
sllist.traverse()

sllist.deleteLinkedList()

sllist.insert(2,0)
sllist.traverse()
sllist.deleteLinkedList()





