#also called Hash_map
# these are dictionaries for larger datasets,key-value pair
# k is the key
# h(k)=i which is the index, look at it like f(x)=y
# we store the value of the key in the i index
# time constant O(1)


'''Applications of Hash Table
Hash tables are implemented where

constant time lookup and insertion is required
cryptographic applications
indexing data is required'''

#eg. studetn id for students, capital for countries
#hashmap.keys()
#hashmap.values()
#hashmap.items() - gives both keys and values

#hash collision when one or more item have the same index
'''
is resolved using chaining meanina a doubly linked list is stored in that index
open addressing: 
1.linear probing: checks for the next slot
2.quadratic probing: same but space increase between slots, it becomes quadratic
3. double hashing:another hash function is calculated for finding the next slot.


'''

#Python program to demonstrate working of HashTable
hashTable =[[],]*10 #list of lists of size 10 obvious

def checkPrime(n): #checks if the number is a prime number. Prime means not divisible by any number expect 1. 
    if n==1 or n==0:
        return 0 # 1 and 0 are not prime
    
    for i in range(2,n//2):
        if n%i ==0:
            return 0 #returns 0 if no
        
    return 1 #returns 1 if yes

def getPrime(n):# takes a number and returns the next prime number greater than 'n'
    if n%2 ==0:
        n=n+1 # increments n to ensure that the next number checked is odd. since even numbers ta prime hunai sakdaina

    while not checkPrime(n):
        n+=2  # continuous increments 'n' by 2 until it finds a prime number using the function checkPrime

    return n
def hashFunction(key): # calculates the hash value(index) for a given key based on the hash table's capacity
    capacity = getPrime(10) # it calls the getPrime function to get a prime number greate than or equal to 10(size of the hash table)
    return key % capacity # it returns the remainder of the key so that hash value hash table to range bhitra nai paros

def insertData(key,value):
    index = hashFunction(key)# jun value is returned above doing key%capacity is stored as index
    hashTable[index]=[key,value]  # aba tei index ma key value haldiyo


def removeData(key):
    index = hashFunction(key) 
    hashTable[index]=0  #same garxa tara value nai 0 banaidinxa tyo key ko value ko which means delete

insertData(123, "Aman")
insertData(432, "Shrestha")
insertData(213, "Computer Science")
insertData(654, "Technology")
print(hashTable)
removeData(123)
print(hashTable)

