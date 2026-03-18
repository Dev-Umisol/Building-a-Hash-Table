class HashTable:
    def __init__(self):
        self.collection = dict()
    
    def hash(self, string):
        unicode_sum = 0
        for letters in string: # <-- # loop through each letter and ord() converts letters into unicode values
            unicode_sum += ord(letters)
               
        return unicode_sum
    
    def add(self, key, value):
        hash_key = self.hash(key) # <-- Keeping original key intact
        
        if hash_key in self.collection:
            self.collection[hash_key][key] = value # <-- {hash_key: {'key': 'value}} (appending to existing bucket)
        else:
            self.collection[hash_key] = {key: value} # <-- create new bucket (nested dictionary)
    
    def remove(self, key):
        unicode_sum = self.hash(key) # <-- Compute the hash
        
        # Check to see if hash_key and key is already in the nested dictionary and dictionary
        if unicode_sum in self.collection and key in self.collection[unicode_sum]: 
            del self.collection[unicode_sum][key]
        
    def lookup(self, key):
        hash_key = self.hash(key)
        
        # Checking for key in nested and regular dictionary
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key] # return value inside nested dictionary
        else:
            return None # Not in dictionary

# --> Example Usage <--
print(HashTable().hash('golf')) # 424
print(HashTable().add('golf', 'sport')) # 424
print(HashTable().add('dear', 'friend')) # 412
print(HashTable().add('read', 'book')) # 412

print(HashTable().lookup('golf')) # sport
print(HashTable().lookup('cfc')) # None

print(HashTable().add('rose', 'flower')) # { 441: { 'rose': 'flower' }}
