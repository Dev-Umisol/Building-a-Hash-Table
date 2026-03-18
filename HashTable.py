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
        unicode_sum = self.hash(key)
        
        
        
    
    def lookup(self, key):
        pass