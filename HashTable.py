import math

class HashTable:

    table = []
    hashFunction = -1
    def __init__(self , size , hashFunction):
        if size < 1:
            size = 1
        self.table = [None] * size
        self.hashFunction = hashFunction

    def insert(self , word , embedding):#inserts an element into the hash table
        position = self.hash(self.hashFunction,word)
        self.table[position] = Node(word , embedding, self.table[position])

    def retrieve(self , word ):# returns the node where the word had been stored
        position = self.hash(self.hashFunction,word)
        temp = self.table[position]
        while temp != None and temp.word != word:
            temp = temp.next
        return temp

    def averageRetrieveComparisons(self):#returns the average number of comparisons done to retrieve an item
        sum = 0
        elements = 0
        for i in range(len(self.table)):
                temp = self.table[i]
                while temp != None:
                    sum += self.retrieveCounter(temp.word)
                    elements += 1
                    temp = temp.next
        return sum / elements

    def retrieveCounter(self , word): # returns the number of comparisons done to retrieve an item
        position = self.hash(self.hashFunction,word)
        counter = 1
        temp = self.table[position]
        while temp != None and temp.word != word:
            temp = temp.next
            counter += 1
        return counter

    def loadFactor(self): #returns the load factor of the table
        elements = 0
        for i in range(len(self.table)):
            if self.table[i] != None:
                cur = self.table[i]
                while cur != None:
                    elements += 1
                    cur = cur.next
        return elements/len(self.table)

    def hash(self, hashFunction, word):#used to find the index to store the word at
        if hashFunction == 1:
            return self.hashFunction1(word)
        if hashFunction == 2:
            return self.hashFunction2(word)
        if hashFunction == 3:
            return self.hashFunction3(word)

    def hashFunction1(self ,word):#modulo hash
        return self.wordToBase26(word) % len(self.table)

    def hashFunction2(self,word):#mid-square hash
        result = self.wordToBase26(word)
        result = result ** 2
        r = int(math.log(len(self.table)))
        if len(self.table) > 10000:
            r = r//2
        result = str(result)
        if len(result) % 2 == 1:
            r -= 1
        start = len(result)//2 - (r//2)
        end = start + r        
        if end - start == 0:
            end +=1
        result = result[start:end]
        result = int(result) % len(self.table)
        return result

    def hashFunction3(self,word):#multiplicative string hash
        result = 29
        for i in range(len(word)):
            result = (result * 29) + ord(word[i])
        return result % len(self.table)

    def printTable(self): #prints the table
        for i in range(len(self.table)):
                temp = self.table[i]
                print('-' , end = '')
                while temp != None:
                    print(temp.word , end = ' ')
                    temp = temp.next
                print()
                
    def wordToBase26(self ,word):#returns the decimal value of the word as base-26 number
        result = 0
        i = 0
        while i < len(word):
            if word[i].isalpha():
                result += (ord(word[i]) - 96) * (26**i)
            i += 1
        return result

class Node(object):
    word = ''
    embedding = []
    next = None

    def __init__(self, word , embedding, next):
        self.word = word
        self.embedding = embedding
        self.next = next
