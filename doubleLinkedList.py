from random import randint
import types


class Node():
    def __init__(self,value) -> None:
        self.prev = None
        self.next = None
        self.value = value

class DoubleLinkedList():
    def __init__(self) -> None:
        self.firstNode = None
        self.lastNode = None
    
    def append(self,value):
        newNode = Node(value)
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            self.lastNode.next = newNode
            newNode.prev = self.lastNode
            self.lastNode = newNode

    def insert(self,value,index):
        _index = 0
        newNode = Node(value)
        currentNode = self.firstNode
        while _index < index-1:
            currentNode = currentNode.next
            _index += 1
        newNode.next = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode

    def pop(self,index):
        _index = 0
        currentNode = self.firstNode
        while _index < index - 1:
            currentNode = currentNode.next
            _index += 1
        currentNode.next = currentNode.next.next

    def remove(self,value):
        if value == self.firstNode.value:
            self.firstNode = self.firstNode.next
            return
        currentNode = self.firstNode
        while currentNode.next.value != value:
            currentNode = currentNode.next
        currentNode.next = currentNode.next.next

    def reverse(self):
        currentNode = self.firstNode
        currentNode2 = self.lastNode
        for i in range(self.__len__()//2):
            currentNode.value, currentNode2.value = currentNode2.value, currentNode.value
            currentNode = currentNode.next
            currentNode2 = currentNode2.prev

    def sort(self):
        count = self.__len__()
        for i in range(count):
            currentNode = self.firstNode
            for j in range(count-i-1):
                if currentNode.next == None:
                    break
                else:
                    if currentNode.value > currentNode.next.value:
                        currentNode.value, currentNode.next.value = currentNode.next.value, currentNode.value
                    currentNode = currentNode.next
    
    def extend(self,*value):
        if isinstance(value[0], types.GeneratorType):
            self.extend(list(value[0]))
        else:
            for el in value:
                if type(el) is list:
                    self.extend(*el)
                else:
                    self.append(el)
    
    def count(self,value):
        br = self.__len__()
        count = 0
        current1 = self.firstNode
        current2 = self.lastNode
        for i in range(br//2):
            if current1.value == value:
                count += 1
            if current2.value == value:
                count += 1
            current1 = current1.next
            current2 = current2.prev
        if br % 2 != 0:
            if current1.value == value:
                count += 1
        return count
    
    def copy(self):
        kopija = DoubleLinkedList()
        currentNode = self.firstNode
        for i in range(self.__len__()):
            kopija.append(currentNode.value)
            currentNode = currentNode.next
        return kopija

    def clear(self):
        return self.__init__()
    
    def index(self,value):
        current = self.firstNode
        index = 0
        for i in range(self.__len__()):
            if current.value == value:
                return index
            current = current.next
            index += 1
        if index == self.__len__():
            return -1
    
    def at(self,index):
        currentNode = self.firstNode
        for i in range(index):
            currentNode = currentNode.next
        return currentNode.value
        
    def __getitem__(self, index):
         return self.at(index)
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.__len__()-1:
            currentNode = self.at(self.n)
            self.n += 1
            return currentNode
        else:
            raise StopIteration

    def __len__(self):
        size = 0
        currentNode = self.firstNode
        while currentNode != None:
            size += 1
            currentNode = currentNode.next
        return size

    def __str__(self) -> str:
        value = '['
        if self.firstNode == None:
            value += ']'
            return value
        currentNode = self.firstNode
        for i in range(self.__len__()):
            if i == self.__len__()-1:
                if type(currentNode.value) is str:
                    value += f"'{currentNode.value}'" + "]"
                else:
                    value += str(currentNode.value) + "]"
            else:
                if type(currentNode.value) is str:
                    value += f"'{currentNode.value}'" + ", "
                else:
                    value += str(currentNode.value) + ", "
                currentNode = currentNode.next
        return value



