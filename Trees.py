##Author: Kusha Maharshi
##Email: kmaharsh@andrew.cmu.edu
import string

"""
BST

Custom Features:
Number if children (d)
Implementation ->
- Functional
- Imperative
Additional features:
- Augment with reduced values
- Balanced

Functions:
- Add
- Delete
- Insert at Rank
- Search
- Print (Inorder, Preorder, Postorder)
- Construct from traversals
- Merge
- Split
- Pretty Print
- Remove Duplicates
"""

def intCmp(num1, num2):
    if num1 > num2: return "GREATER"
    elif num2 > num1: return "LESS"
    else: return "EQUAL"
    
    
class Tree(object):
    def __init__(self, x):
        self.data = x
        self.l = None
        self.r = None
        
        
def isLeaf(tree):
    return tree != None and tree.data != None and tree.l == None and tree.r == None


def findMin(tree):
    setMin = 2**32
    if tree == None: return "calling min on empty tree"
    def help(t):
        
        if t.l == None: return t.data
        return help(t.l)
    return help(tree)
        
        
class BST(object):
    
    def __init__(self, cmpFn = intCmp, bal = False, aug = False, augFn = None):
        try:
            if augFn != None: assert(not aug)
        except:
            print("set aug to True to specify augmenting function")
            return
        
        self.root = None #empty tree on initialization
        self.size = 0
        self.cmp = cmpFn
        
    def __repr__(self):
        return "Please use the custom print functions"
        
    def add(self, x):
        
        T = self.root
        
        #help to add x
        def help(tree):
            if tree == None:
                return Tree(x)
            cur = tree.data
            
            if self.cmp(x, cur) == "GREATER":
                tree.r = help(tree.r)
                
            #elif self.cmp(x, cur) == "EQUAL":
                #return tree
            else:
                tree.l = help(tree.l)
                
            
            return tree
        
        self.root = help(T)
        self.size += 1
    
    def printInorder(self):
        
        T = self.root
        
        def help(tree):
            if tree == None:
                return []
            return help(tree.l) + [tree.data] + help(tree.r)
            
        
        ans = help(T)
        print(ans)
        return ans
        
    
    def printPreorder(self):
        
        T = self.root
        
        def help(tree):
            if tree == None:
                return ""
            return str(tree.data) + " " + help(tree.l) +  " " + help(tree.r)
            
        print(help(T))
        
    def printPostorder(self):
        
        T = self.root
        
        def help(tree):
            if tree == None:
                return ""
            return help(tree.l) +  " " + help(tree.r) + " " + str(tree.data)
            
        print(help(T))
        
    @staticmethod
    def isLeaf(tree):
        return tree != None and tree.data != None and tree.l == None and tree.r == None

    @staticmethod
    def findMin(tree):
        setMin = 2**32
        if tree == None: return "calling min on empty tree"
        def help(t):
            if isLeaf(t): return t.data
            return help(t.l)
        return help(tree)
        
    def delete(self, x):
        T = self.root
        
        if T == None: return T
        if isLeaf(T): self.root = None
        self.size -= 1
        def help(tree, y):
            if tree == None:
                
                self.size += 1
                return tree
            cur = tree.data
            
            left = tree.l
            right = tree.r
            
            if self.cmp(y, cur) == "GREATER":
                tree.r = help(tree.r, y)
                if tree.r != None and tree.r.data == None:
                    tree.r = None
                
            elif self.cmp(y, cur) == "LESS":
                tree.l = help(tree.l, y)
                if tree.l != None and tree.l.data == None:
                    tree.l = None
                
            else:
               
                if left == None and right == None:
                    
                    tree.data = None
                    
                elif right == None:
                    v = left.data
                    tree.data = v
                    tree.l = help(left, v)
                    if tree.l != None and tree.l.data == None:
                        tree.l = None
                    
                else:
                    v = findMin(right)
                    tree.data = v
                    tree.r = help(right, v)
                    if tree.r != None and tree.r.data == None:
                        tree.r = None
                    
            
            return tree
            
        return help(T, x)
        
    def prettyPrintBad(self):
        T = self.root
        
        if T == None: return ""
        
        def help(tree):
            if tree == None:
                return ("", 0, 0)
            else:
                (lstring, lsize, lheight) = help(tree.l)
                (rstring, rsize, rheight) = help(tree.r)
                m = max([lheight, rheight])
                padding = (2*m + 3)*"  "
                padding2 = (m + 1)*"  "
                cur = str(tree.data)
                slashstring = "/" + (2*m + 3)*"  " + "\\"
                if m == lheight:
                    chosen = lstring
                    other = rstring
                else:
                    chosen = rstring
                    other = lstring
                C = chosen.splitlines()
                O = other.splitlines()
                c = len(C)
                o = len(O)
                assert(c >= o)
                diff = c - o
                extra = C[c-(diff) : c]
                merged = ""
                if m == lheight:
                    for i in range(o):
                        #other is right
                        merged = merged + C[i] + " " + O[i] + "\n"
                    for j in range(diff):
                        merged = merged + " " + extra[j] + "\n"
                        
                else:
                    for i in range(o):
                        #other is left
                        merged = merged + O[i] + " " + C[i]
                    for j in range(diff):
                        merged = merged + padding + extra[j] + "\n"
                merged.strip("\n")
                s = padding + cur + padding + "\n" + padding2 + slashstring + padding2 + "\n" + merged
                return (s, m+1, lsize+rsize+1)
        return help(T)[0]
        
    def merge1(self, other):
        
        IT1 = self.printInorder()
        IT2 = other.printInorder()
        
        PT1 = self.printPreorder()
        PT2 = other.printPreorder()
        
        M = mergeLists(IT1, IT2)
        
        
        
        
        
        
        
    
        
def testBST():
    
    t1 = BST()
    #t1.printInorder()
    t1.add(2)
    t1.add(3)
    t1.add(1)
    #print(t1.prettyPrint())
    t1.add(24)
    
    t1.add(11)
    t1.add(28)
    t1.add(22)
    t1.add(-1)
    #print(t1.prettyPrint())
    t1.printInorder()
    t1.delete(3)
    #t1.printInorder()
    t1.delete(1)
    #t1.printInorder()
    t1.delete(-1)
    #t1.printInorder()
    t1.delete(2)
    #t1.printInorder()
    assert(t1.size == 4)
    #print(t1.prettyPrint())
    """t2 = BST()
    t2.add(2)
    t2.add(3)
    t2.add(1)
    t2.printInorder()
    t2.delete(1)
    t2.printInorder()
    t2.delete(3)
    t2.printInorder()
  
    t2.delete(2)
   # assert(t1.size == 5)
    t2.printInorder()"""

testBST()
            
            
        
        
            
        
    









