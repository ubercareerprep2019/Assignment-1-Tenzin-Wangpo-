"""
    Tenzin Wangpo

    I am using double linked list to keep track of the minimum

    mini Time: O(1) and space O(1)
"""

class Node:
    def __init__(self, item, next_min = None, prev_min = None):
        self.__item = item
        self.nextMin = next_min
        self.prevMin = prev_min

    def get_item(self):
        return self.__item

    def get_nextMin(self):
        return self.nextMin

    def get_prevMin(self):
        return self.prevMin

    def set_nextMin(self, object_node):
        self.nextMin = object_node

    def set_prevMin(self, object_node):
        self.prevMin = object_node

class Stack:
    def __init__(self):
        self.__store = list()
        self.min = None

    def push(self, data):
        newObject = Node(data)

        # adding the first data
        if self.min is None:
            self.min = newObject

        elif self.min.get_item() >= newObject.get_item():
            newObject.set_nextMin(self.min)
            self.min.set_prevMin(newObject)
            self.min = newObject

        else:
            temp = None
            temp_node = self.min
            notLast = True
            while temp_node.get_item() < newObject.get_item():
                # if we reach the last element then we do all the changes in that loop and exit from while loop
                if temp_node.get_nextMin() is None:
                    temp_node.set_nextMin(newObject)
                    newObject.set_prevMin(temp_node)
                    notLast = False
                    break
                else:

                    temp = temp_node
                    temp_node = temp_node.get_nextMin()

            # new position is in between some two nodes then
            if notLast:
                temp.set_nextMin(newObject)
                newObject.set_prevMin(temp)
                newObject.set_nextMin(temp_node)
                temp_node.set_prevMin(newObject)
        self.__store.append(newObject)

    # parts of linked list for minimum step is same but position of pop in stack and queue is different
    def pop(self, value=None, typeDS = "Stack"):
        if value == None:
            try:
                if typeDS == "Stack":
                    dataOut = self.__store[-1]
                else:
                    # for Queue
                    dataOut = self.__store[0]

                # self min is the node that need to be pop
                if dataOut == self.min:
                    if len(self.__store) == 1:
                        self.min = None
                    else:
                        self.min = dataOut.get_nextMin()
                        self.min.set_prevMin(None)

                # pop node is not the last node of linked list
                elif dataOut.get_nextMin() is not None:
                    prev = dataOut.get_prevMin()
                    next = dataOut.get_nextMin()
                    prev.set_nextMin(next)
                    next.set_prevMin(prev)

                # if pop Node is the last node in linked list
                else:
                    prev = dataOut.get_prevMin()
                    prev.set_nextMin(None)

                if typeDS == "Stack":
                    return self.__store.pop().get_item()
                else:
                    # if it's Queue
                    del (self.__store[0])
                    return dataOut.get_item()

            # if the stack is empty, it will return None
            except IndexError:
                return None
        # it's only used in Stack (it only happen when user pop specific value)
        else:
            if len(self.__store) == 1 and self.__store[0].get_item() == value:
                self.min = None
                return self.__store.pop().get_item()

            # in case duplicate value in stack, then I am deleting the first value and break the loop
            for i in range(len(self.__store)):
                if self.__store[i].get_item() == value:
                    prev = self.__store[i].get_prevMin()
                    prev.set_nextMin(self.__store[i].get_nextMin())
                    del (self.__store[i])
                    return value

        # value not in stack
        return None

    def top(self):
        try:
            return self.__store[-1].get_item()

        #if the stack is empty, it will return None
        except AttributeError:
            return None
        except IndexError:
            return None

    def isEmpty(self):
        return len(self.__store) == 0

    def printAll(self):
        output = []
        for i in self.__store:
            output.append(i.get_item())
        return output

    def mini(self):
        try:
            return self.min.get_item()
        except AttributeError:
            return None


if __name__ == "__main__":
    stack = Stack()
    print("stack: {} and minimum: {}".format(stack.printAll(), stack.mini()))
    print("is stack empty: {}".format(stack.isEmpty()))
    stack.push(4)
    stack.push(1)
    print("stack: {} and minimum: {}".format(stack.printAll(), stack.mini()))
    stack.push(9)
    print("stack: {} and minimum: {}".format(stack.printAll(), stack.mini()))
    print("stack top: {}".format(stack.top()))
    print("stack pop: {}".format(stack.pop()))
    print("stack: {} and is stack empty: {}".format(stack.printAll(), stack.isEmpty()))
    print("stack pop: {}".format(stack.pop()))
    print("stack: {} and minimum: {}".format(stack.printAll(), stack.mini()))
    print("stack pop: {}".format(stack.pop()))
    print("stack: {} and is stack empty: {}".format(stack.printAll(), stack.isEmpty()))
    print("stack: {} and minimum: {}".format(stack.printAll(), stack.mini()))
    print("stack top: {}".format(stack.top()))
    print("stack pop: {}".format(stack.pop()))
    print("stack: {} and stack top: {}".format(stack.printAll(), stack.top()))
    stack.push(0)
    print("stack: {} and minimum: {}".format(stack.printAll(), stack.mini()))
    print("stack top: {}".format(stack.top()))

# ------------------------------------- OUTPUT -----------------------------------------
"""
stack: [] and minimum: None
is stack empty: True
stack: [4, 1] and minimum: 1
stack: [4, 1, 9] and minimum: 1
stack top: 9
stack pop: 9
stack: [4, 1] and is stack empty: False
stack pop: 1
stack: [4] and minimum: 4
stack pop: 4
stack: [] and is stack empty: True
stack: [] and minimum: None
stack top: None
stack pop: None
stack: [] and stack top: None
stack: [0] and minimum: 0
stack top: 0
"""