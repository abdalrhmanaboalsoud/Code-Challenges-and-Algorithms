
# First Repeated Word Problem


1. Problem Domain:

   - Find the first repeated word in a given string.
   - If no repeated words are found, return "No Repetition."

   Example:
     Input:  "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
     Output: "ASAC"

2. Algorithms:

   - Use a Hashtable to store encountered words.
   - Use Linked Lists to handle hash collisions.
   - Iterate through words, return the first repeated one.

3. Pseudo Code:

   CLASS Node:
       FUNCTION __init__(key):
           self.key = key
           self.next = None

   CLASS LinkedList:
       FUNCTION __init__():
           self.head = None

       FUNCTION insert(key):
           new_node = Node(key)
           new_node.next = self.head
           self.head = new_node

       FUNCTION search(key):
           current = self.head
           WHILE current:
               IF current.key == key:
                   RETURN True
               current = current.next
           RETURN False

   CLASS HashTable:
       FUNCTION __init__(size):
           self.size = size
           self.table = [LinkedList() for _ in range(size)]

       FUNCTION _hash_function(key):
           key = key.lower()
           hash_value = sum(ord(c) for c in key)
           RETURN hash_value % self.size

       FUNCTION insert(key):
           index = self._hash_function(key)
           self.table[index].insert(key)

       FUNCTION search(key):
           index = self._hash_function(key)
           RETURN self.table[index].search(key)

   FUNCTION first_repeated_word(input_string):
       words = input_string.split()
       hashtable = HashTable(size=100)

       FOR word IN words:
           IF hashtable.search(word):
               RETURN word
           ELSE:
               hashtable.insert(word)

       RETURN "No Repetition"

4. Test Cases:

   - Input: "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
     Output: "ASAC"
   - Input: "I am learning programming at ASAC."
     Output: "No Repetition"
   - Input: "The cat jumped over the dog. The dog barked at the cat."
     Output: "The"
   - Input: "Hello, world! Hello again, world!"
     Output: "Hello"
   - Input: ""
     Output: "No Repetition"

5. Big O Notation:

   - Time Complexity: O(n)
     * Average case constant time operations for hashtable (O(1)).
     * n is the number of words.

   - Space Complexity: O(m)
     * m is the number of unique words stored.
