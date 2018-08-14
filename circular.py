class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    # Insert data into circular list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
        ptr1.next = self.head

        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1  # For the first node
        self.head = ptr1

    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print(temp.data,end=" ")
                temp = temp.next
                if (temp == self.head):
                    break
    def smallestNumber(self):
        temp = self.head

        if self.head is not None:
            min = temp.data
            while (True):
                if temp.data<min:
                    min= temp.data
                temp = temp.next
                if (temp == self.head):
                    break
            print("\n")
            print("Smallest number in the list : ",min)

if __name__ =="__main__":
    cllist = CircularLinkedList()

    n = int(input('Enter no of elements in the list: '))
    a = []
    print("Enter elements")
    for i in range(n):
        t = int(input())
        a.append(t)
        cllist.push(t)
    print("Contents of circular Linked List")
    cllist.printList()
    cllist.smallestNumber()
