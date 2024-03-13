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

class HashTable:

    def __init__(self,size):
        self.size = size # so we know that when the hashtable object will be created we will need to pass on a size and whereever we use it we need to use the variable name self.size
        self.hash_table = self.create_buckets() # also a variable self.hash_table will be initialized will will hold the value of the value returned from the create_buckets function inside the class

    def create_buckets(self):
        return [[] for i in range(self.size)] # so this basically creates an empty hash table of size that we provide and the empty table is stored in the self.hash_table   

    def set_val(self,key, val):# this will insert a keyvalue pair to the table
        #Get the index from the key using hash function

        hashed_key = hash(key)% self.size # it calculates the hashed key using the built-in 'hash' function and takes the the modulus of it with the size of the has table to get the index
        # we know that modulus gives the remainder
        bucket = self.hash_table[hashed_key] # this stores the bucket which is the small array corresponding to the index

        found_key = False # initializes a variable 'found_key' to 'False'
        for index, record in enumerate(bucket): # it iterates through the records in the bucket using the 'enumerate'function to keep track of the index and the record itself
            record_key, record_val = record

            
            if record_key ==key: # if the key of the current record matches the key we are trying to insert, it sets found_key to True and breaks out of the loop
                found_key = True
                break

        if found_key:# if found _key is True
            bucket[index]=(key, val) # updates the key-value pair
        else:
            bucket.append((key,val)) # otherwise adds new that is appends


    def get_val(self,key):
        hashed_key = hash(key)%self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record


            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No record found"
        

    def delete_val(self,key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]

        found_key= False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    

    def __str__(self):# this method provides a string representation of the hash table
        return "".join(str(item) for item in self.hash_table) # it concatenates the string representations of all the items in the hash table and returns the result
            
hash_table = HashTable(50)

hash_table.set_val("amans@gmail.com", "some value")
print(hash_table)
print()

hash_table.set_val('piyush@gmail.com', 'some other value')
print(hash_table)
print()

print(hash_table.get_val('piyush@gmail.com'))
print()

hash_table.delete_val('piyush@gmail.com')
print(hash_table)


