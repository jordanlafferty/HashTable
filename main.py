# {"key": number, "index" : [], "word":string}

class HashTable1:
    M = 31

    def __init__(self):
        self.array = [[]] * self.M

    def Hash(self, key):
        return key % self.M

    def insert(self, key, value):
        hashcode = self.Hash(key)

        found = len(self.array[hashcode]) > 0
        print(self.array[hashcode])
        if found is True:
            for i in range(len(self.array[hashcode])):
                if self.array[hashcode][i] == key:
                    self.array[hashcode][i]["index"].append(value["index"][0])
                    return hashcode
                self.array[hashcode].append(value)
            return hashcode
        else:
            self.array[hashcode].append(value)

    def search(self, key):
        hashcode = self.Hash(key)
        if len(self.array[hashcode]) > 0:
            for i in range(len(self.array[hashcode])):
                if self.array[hashcode][i]["key"] == key:
                    return self.array[hashcode][i]["index"]
            return None
        else:
            return None


class HashTable:
    M = 53

    def __init__(self):
        self.theHash = [[] for _ in range(self.M)]

    def Hash(self, key):
        return key % self.M

    def insert(self, key, value):
        hashcode = self.Hash(key)
        self.theHash[hashcode].append(value)

    def delete(self, value):
        for i in range(len(self.theHash)):
            x = []
            if self.theHash[i] != x:
                if self.theHash[i][0] == value:
                    self.theHash[i].clear()
                    break

    def search(self, key):
        hashcode = self.Hash(key)
        x = []
        if self.theHash[hashcode] != x:
            return self.theHash[hashcode][0]
        return None

    def thePrint(self):
        for i in range(len(self.theHash)):
            print("{key-", i, end=" value- [")
            for j in self.theHash[i]:
                print(j, end=" ")

            print("]}")


def getKey(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            letter = letter.lower()
            break
    allChars = "abcdefghijklmnopqrstuvwxyz1234567890!,.?''+=()&;: "
    for i in range(len(allChars)):
        if letter == allChars[i]:
            return i


def newPoem(text, hashTable):
    thePoem = []

    for i in range(len(text)):
        letter = hashTable.search(text[i])
        if letter is not None:
            thePoem.append(letter)

    spaceCount = 0
    for j in range(len(thePoem)):
        if thePoem[j] != " ":
            print(thePoem[j].lower(), end=" ")
        else:
            spaceCount += 1
            print(thePoem[j], end=" ")
            if spaceCount == 5:
                spaceCount = 0
                print("\n")


def readTheText(text):
    theHash = HashTable()
    poemInKeys = []
    for i in range(len(text)):
        index = getKey(text[i])
        letter = text[i]
        theHash.Hash(index)
        theHash.insert(index, letter)
        poemInKeys.append(index)
    return theHash, poemInKeys


def deletePuncuation(hashTable):
    punc = "!,.?''+=()&;:"
    for i in range(len(punc)):
        hashTable.delete(punc[i])
    hashTable.thePrint()
    return hashTable


def displayPoem(line):
    spaceCount = 0
    for j in range(len(line)):
        if line[j] != " ":
            print(line[j].lower(), end=" ")
        else:
            spaceCount += 1
            print(line[j], end=" ")
            if spaceCount == 5:
                spaceCount = 0
                print("\n")
    print("\n")


with open('poem.txt') as f:
    y = f.read()

displayPoem(y)
myHash, poem = readTheText(y)
myHash.thePrint()
myHash = deletePuncuation(myHash)
newPoem(poem, myHash)
