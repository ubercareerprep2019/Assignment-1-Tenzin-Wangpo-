class Node:
    def __init__(self, item, nextNode = None):
        self.item = item
        self.nextNode = nextNode

    def get_nextNode(self):
        return self.nextNode

    def set_nextNode(self, nodeObject):
        self.nextNode = nodeObject

    def get_item(self):
        return self.item


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    def pushBack(self, data):
        dataToPush = Node(data)
        #if it is first element
        if self.root == None:
            self.root = dataToPush
        else:
            temp = self.root
            foo = self.root.get_nextNode()
            while(foo != None):
                temp = foo
                foo = foo.get_nextNode()
            temp.set_nextNode(dataToPush)
        self.length += 1

    def popBack(self):
        if self.root is None:
            return None

        elif self.root.get_nextNode() is None:
            self.root = None
            self.length -= 1
        else:
            next = self.root.get_nextNode()
            while next is not None:
                temp = next
                next = next.get_nextNode()
            temp.set_nextNode(None)
            self.length -= 1

    def insert(self, index, data):
        dataNode = Node(data)
        if self.length < index:
            return None

        elif self.root == None and index == 0:
            self.pushBack(data)

        elif index == 0:
            dataNode.set_nextNode(self.root)
            self.root = dataNode
            self.length += 1

        else:
            next = self.root
            for i in range(index):
                temp = next
                next = next.get_nextNode()
            temp.set_nextNode(dataNode)
            dataNode.set_nextNode(next)
            self.length += 1


    def erase(self, index):
        if index > self.length or self.root is None:
            return

        elif self.length == 1 and index == 0:
            self.root = None
            self.length -= 1

        else:
            next = self.root
            for i in range(index):
                temp = next
                next = next.get_nextNode()
            temp.set_nextNode(next.get_nextNode())
            self.length -= 1

    def elementAt(self, index):
        if self.length < index:
            return
        elif self.length == 0:
            return
        else:
            next = self.root
            for i in range(index):
                next = next.get_nextNode()
            return next.get_item()

    def size(self):
        return self.length

    def hasCycle(self):
        if self.root == None:
            return False

        hashLinkedList = dict()
        currentNode = self.root
        while currentNode.get_nextNode() != None:
            if id(currentNode) in hashLinkedList:
                return True
            hashLinkedList[id(currentNode)] = currentNode.get_item()
            currentNode = currentNode.get_nextNode()
        return False


    def isPalindrome(self):
        #throw half of item in hash table
        linkedListHash = dict()
        currentNode = self.root
        # sizeDifference is to used later in comparing the node to hashTable
        sizeDifference = 0
        for i in range(self.length // 2):
            linkedListHash[i] = currentNode.get_item()
            currentNode = currentNode.get_nextNode()
            sizeDifference += 1

        # LList length is odd then we can ignore the middle node
        if self.length % 2 != 0:
            sizeDifference += 2
            currentNode = currentNode.get_nextNode()
        else:
            sizeDifference += 1

        for j in range(self.length // 2):
            if currentNode.get_item() != linkedListHash[self.length - (j + sizeDifference)]:
                return False
            currentNode = currentNode.get_nextNode()
        return True

    def printAll(self):
        output = []
        next = self.root
        while next != None:
            output.append(next.get_item())
            next = next.get_nextNode()
        return output

if __name__ == "__main__":
    myLList = LinkedList()
    myLList.pushBack(10)
    print(myLList.size())
    myLList.popBack()
    print(myLList.size())
    myLList.insert(0, 8)
    print(myLList.size())
    myLList.insert(1, 9)
    print(myLList.size())
    print(myLList.printAll())
    myLList.insert(2, 11)
    print(myLList.size())
    print(myLList.printAll())
    myLList.insert(1, 14)
    print(myLList.printAll())
    myLList.insert(0, 14)
    print(myLList.printAll())


    myList = LinkedList()
    myList.insert(0,1)
    print("\n\nlinkedList: {} and size is {}".format((myList.printAll()), myList.size()))
    myList.insert(0,4)
    print("linkedList: {} and size is {}".format((myList.printAll()), myList.size()))
    myList.insert(3,6)
    print("linkedList: {} and size is {}".format((myList.printAll()), myList.size()))
    print("element in index 1: {}".format(myList.elementAt(1)))
    myList.erase(1)
    print("linkedList: {} and size is {}".format((myList.printAll()), myList.size()))
    myList.erase(0)
    print("linkedList: {} and size is {}".format((myList.printAll()), myList.size()))
    myList.erase(0)

    LList = LinkedList()
    LList.pushBack(1)
    LList.pushBack(2)
    LList.pushBack(3)
    LList.pushBack(4)

    LList.pushBack(4)
    LList.pushBack(3)
    LList.pushBack(2)
    LList.pushBack(1)
    print("\n\nlinkedList: {} and size is {}".format((LList.printAll()), LList.size()))
    print("Is above linkList is Palindrome? {}".format(LList.isPalindrome()))

    LList2 = LinkedList()
    listP = [1,2,3,4,5,4,3,2,6]
    for i in listP:
        LList2.pushBack(i)
    print("\n\nlinkedList: {} and size is {}".format((LList2.printAll()), LList2.size()))
    print("Is above linkList is Palindrome? {}".format(LList2.isPalindrome()))

    LList3 = LinkedList()
    listNP = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1] # not palindrome
    for i in listNP:
        LList3.pushBack(i)
    print("\n\nlinkedList: {} and size is {}".format((LList3.printAll()), LList3.size()))
    print("Is above linkList is Palindrome? {}".format(LList3.isPalindrome()))

    L = LinkedList()
    L.pushBack(1)
    print("\n\nlinkedList: {} and size is {}".format((L.printAll()), L.size()))
    print("Is above linkList is Palindrome? {}".format(L.isPalindrome()))

    print("\n\n---------------------  Cycle check  ------------------------")
    cycleCheck = LinkedList()
    print("Empty LinkedList: HasCycle: {}".format(cycleCheck.hasCycle()))
    list_cycle = [3,4,6,7]
    for i in list_cycle:
        cycleCheck.pushBack(i)
    print(cycleCheck.printAll())
    print(cycleCheck.hasCycle())
    cycleCheck.root.get_nextNode().get_nextNode().get_nextNode().set_nextNode(cycleCheck.root)
    print("Last node's next node is root(Head), HasCycle: {}".format(cycleCheck.hasCycle()))







# ---------------------------------------- OUTPUT ---------------------------------------
"""
1
0
1
2
[8, 9]
3
[8, 9, 11]
[8, 14, 9, 11]
[14, 8, 14, 9, 11]


linkedList: [1] and size is 1
linkedList: [4, 1] and size is 2
linkedList: [4, 1] and size is 2
element in index 1: 1
linkedList: [4] and size is 1
linkedList: [] and size is 0


linkedList: [1, 2, 3, 4, 4, 3, 2, 1] and size is 8
Is above linkList is Palindrome? True


linkedList: [1, 2, 3, 4, 5, 4, 3, 2, 6] and size is 9
Is above linkList is Palindrome? False


linkedList: [1, 2, 3, 4, 5, 6, 4, 3, 2, 1] and size is 10
Is above linkList is Palindrome? False


linkedList: [1] and size is 1
Is above linkList is Palindrome? True


---------------------  Cycle check  ------------------------
Empty LinkedList: HasCycle: False
[3, 4, 6, 7]
False
Last node's next node is root(Head), HasCycle: True

"""



