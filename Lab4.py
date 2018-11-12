#CS2302
#Aaron Brown
#Diego Aguirre
#Anindita Nath
#11/11/18
#Read words and their embeddings from a file then store them in a hash table

from HashTable import HashTable, Node

def main():
    loadFactor = -1
    for i in range(1,4):
        numberOfWords = 400000
        tableSize = 400000
        hashFunction = i
        table = createTable(numberOfWords, tableSize , hashFunction)
        #table.printTable()
        loadFactor = table.loadFactor()

        print('Average number of comparisons done for retrieve using hash function '
        + str(hashFunction) + ':\n' + str(table.averageRetrieveComparisons()))
    print('Load factor for tables: ' + str(loadFactor))

def createTable(numberOfWords, tableSize , hashFunction):
    word_embeddings = open('glove.6B.50d.txt')
    table = HashTable(tableSize , hashFunction)
    for i in range(numberOfWords):
        word = word_embeddings.readline()
        if word[0].isalpha() == True: #ignores words that do not start with an alphabetic character
            table.insert(getWord(word) , getWordEmbedding(word))
    word_embeddings.close()
    return table

def getWord(word): #returns word without embedding
    i = 0
    while word[i].isspace() != True:
        i+=1
    return word[0:i]

def getWordEmbedding(word):#returns word embedding without word
    i = 0
    while word[i].isspace() != True:
        i+=1
    i+=1

    e = []
    while  i < len(word):
        j = i
        if word[i].isnumeric() or word[i] == '-':
            while j < len(word) and word[j].isspace() == False:
                j += 1
            e.append(float(word[i:j]))
        i = j + 1

    return e

main()

