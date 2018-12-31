#Custom Containers
"""
-> If element added beyond max size, delete highest priority space
-> Assign priority function during initialization
-> Delete operation should be constant time
-> Add operation constant time, takes up lowest priority empty space
-> Search operation constant time (expected)
-> p : index -> real

* Array Operations
* LinkedList
* UnboundedArray
* PriorityQueue
* HashTable
* BinarySearchTree (Balanced)
* Trie

"""
from LinkedList import *

##
class CustomContainers(object):
    #x='buffalo'    
    #exec("%s = %d" % (x,2))
    def __init__(self, choices):
        #allows simultaneous data structures
        #custom threading b/w different structures allowed
        numChoices = len(choices)
        output = [None]*numChoices
        for i in range(numChoices):
            s = choices[i]
            exec("output[i] = " + s + "()")
            
        self.allDS = output
        
#A = CustomContainers(["LinkedList"])


        
        
        
        
            
        
        
        