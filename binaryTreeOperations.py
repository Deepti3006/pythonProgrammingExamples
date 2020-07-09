class binaryTree:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self,data):
        if data <self.data:
            if self.left is None:
                self.left = binaryTree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right =binaryTree(data)
            else:
                self.right.insert(data)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def findTheElement(self,element):

        root = self.data
        if element == root:
            print("Element is root " + str(self.data))
        elif element < root:
            if self.left is None :
                print("Not seen")
            else:
                return self.left.findTheElement(element)
        elif element > root:
            if self.right is None:
                print("Not seen")
            else:
                return self.right.findTheElement(element)
        else:
            print("found")

    def totalheightOfBinaryTree(self, root):

        self.res = 0
        node = root

        def helper(node):
            if node == None:
                return 0
            else:

                l = helper(node.left)
                r = helper(node.right)
                self.res += abs(r - l)
                return self.res+1

        helper(node)

        return self.res












b= binaryTree(20)
b.insert(10)
b.insert(30)
b.insert(5)
b.insert(40)
b.PrintTree()
b.findTheElement(5)
#print(b.preOrderTraversal(b))
#print(b.inOderTraversal(b))
print(b.totalheightOfBinaryTree(b))

