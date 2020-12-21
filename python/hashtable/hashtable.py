'''
Required Features:
- [x] create hashtable class
- [x] add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- [x] get: takes in the key and returns the value from the table.
- [x] contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
- [x] hash: takes in an arbitrary key and returns an index in the collection.
'''

from code_challenges.linked_list.linked_list.linked_list import LinkedList

class InvalidOperationError(Exception):
    pass

class Hashtable():
    '''
    This Hashtable class definition can be used to create an instance of a hashtable data structure.  It will be composed of a LinkedList???  Or just list?
    ?It has an attribute of ????.
    '''

    def __init__(self, size=24):
        self._size = size
        self._buckets = size * [None]


    def add(self, key, value):
        ''' takes in both the key and value. This method should hash the key, and add   the key and value pair to the table, handling collisions as needed. '''

        hashed_index = self._hash(key)

        if not self._buckets[hashed_index]:
            self._buckets[hashed_index] = LinkedList()

        self._buckets[hashed_index].insert((key,value))

    def set(self, key, value):
        ''' this method allows for the add method to get called by another common name '''
        self.add(key,value)


    def get(self, key):
        ''' takes in the key and returns the value from the table. '''

        hashed_index = self._hash(key)

        linked_list_in_bucket = self._buckets[hashed_index]

        if linked_list_in_bucket == None:
            return None

        current = linked_list_in_bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next_node


    def contains(self, key):
        ''' takes in the key and returns a boolean, indicating if the key exists in the table already. '''

        hashed_index = self._hash(key)

        linked_list_in_bucket = self._buckets[hashed_index]

        if linked_list_in_bucket == None:
            return False

        current = linked_list_in_bucket.head
        while current:
            if current.value[0] == key:
                return True
            current = current.next_node

        return False


    def _hash(self, key):
        ''' takes in an arbitrary key and returns an index in the collection. '''

        product = 1

        for char in key:
            product *= ord(char)

        productplus = product + len(key)

        primed = productplus * 19

        hashed_index = primed % self._size

        return hashed_index
