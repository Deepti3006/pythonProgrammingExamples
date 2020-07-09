class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.headval = None





    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next








l =LinkedList()
l.headval = Node(30)
e2 = Node(40)
e3 =Node(50)
e4 = Node(30)
l.headval.next = e2
e2.next = e3
e3.next = e4







