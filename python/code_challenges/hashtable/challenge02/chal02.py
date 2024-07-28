class Node:
    """
    A class representing a node in a linked list.
    """

    def __init__(self, key):
        """
        Initializes a Node with a given key.
        """
        self.key = key
        self.next = None


class LinkedList:
    """
    A class representing a linked list to handle collisions in the hashtable.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def insert(self, key):
        """
        Inserts a new key into the linked list.
        """
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        """
        Searches for a key in the linked list. Returns True if found, otherwise False.
        """
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False


class HashTable:
    """
    A class representing a simple hashtable using chaining for collision resolution.
    """

    def __init__(self, size):
        """
        Initializes the hashtable with a given size and empty linked lists.
        """
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def _hash_function(self, key):
        """
        A simple hash function to compute the index for a given key.
        """
        # Convert the key to a lower case to handle case insensitivity
        key = key.lower()

        # Calculate the hash value using the sum of ASCII values of characters
        hash_value = sum(ord(c) for c in key)

        # Return the index by taking modulo with the size of the table
        return hash_value % self.size

    def insert(self, key):
        """
        Inserts a key into the hashtable.
        """
        index = self._hash_function(key)
        self.table[index].insert(key)

    def search(self, key):
        """
        Searches for a key in the hashtable. Returns True if found, otherwise False.
        """
        index = self._hash_function(key)
        return self.table[index].search(key)


def first_repeated_word(input_string):
    """
    Finds the first repeated word in a given string using a hashtable.
    """
    # Remove punctuation and split the string into words
    words = input_string.split()

    # Initialize the hashtable with a reasonable size
    hashtable = HashTable(size=100)

    # Iterate through each word in the list
    for word in words:
        # Check if the word is already in the hashtable
        if hashtable.search(word):
            # Return the first repeated word
            return word
        else:
            # Insert the word into the hashtable
            hashtable.insert(word)

    # If no repetition is found, return "No Repetition"
    return "No Repetition"


# Test cases
input1 = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
input2 = "I am learning programming at ASAC."

print(first_repeated_word(input1))  # Output: ASAC
print(first_repeated_word(input2))  # Output: No Repetition
