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
        
    def topView(self):
        raise Exception("NYI")
        #left spine trav + cur + right spine trav
        
        
    @staticmethod
    def levelOrder(root):
        #Write your code here
        d = dict()
        
        def help(tree, depth):
            
            if tree == None:
                return
            cur = tree.info
            help(tree.left, depth+1)
            if depth in d: d[depth].append(cur)
            else: d[depth] = [cur]
            help(tree.right, depth+1)
        
        help(root, 0)
    
        l = len(d)
        ans = []
        for i in range(l):
            assert(i in d)
            ans.extend(d[i])
    
        for i in range(len(ans)):
            print(ans[i], end = " ")

     
    @staticmethod
    def lcad(ptr1, ptr2):
        #assert(isinstance(ptr1, Tree) and isinstance(ptr2, Tree))
        raise Exception("NYI")
        
    @staticmethod  
    def lca(root, v1, v2):
        
        def help(tree):
            
            if tree == None:
                return None
            else:
                cur = tree.info
                if v1 > cur and v2 > cur:
                    return help(tree.right)
                elif v1 < cur and v2 < cur:
                    return help(tree.left)
                else:
                    return tree
                    
        return help(root)
                    
        
        
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
        
    @staticmethod
    def mergeLists(L1, L2):
        
        i = 0
        j = 0
        k = 0
        a = len(L1)
        b = len(L2)
        L = [None]*(len(L1) + len(L2))
        
        while(i < a and j < b):
            l1cur = L1[i]
            l2cur = L2[j]
            if l1cur < l2cur:
                L[k] = l1cur
                i+=1
                k+=1
            else:
                L[k] = l2cur
                j+=1
                k+=1
        
        while(i < a):
            cur = L1[i]
            L[k] = cur
            k+=1
            i+=1
            
        while(j < b):
            cur = L2[j]
            L[k] = cur
            k+=1
            j+=1
            
        assert(L.count(0) == 0)
        return L
        
        
    @staticmethod
    def treeFromInorder(L):
        
        l = len(L)
        
        if l == 0:
            return None
        
        left = L[:l//2]
        cur = L[l//2]
        right = L[l//2+1 : ]
        
        make = Node(cur)
        make.l = treeFromInorder(left)
        make.r = treeFromInorder(right)
        
        return make
        
        
    
        
        
    def merge1(self, other):
        # non-destructive
        #limited space implementation
        T1 = self.printInorder()
        T2 = self.printInorder()
        
        T = mergeLists(T1, T2)
        
        merged = treeFromInorder(T)
        
        return merged
        
        
    
        
    
        
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
            
            
##Hackerrank Huffman Tree        
import string
def decodeHuff(root, s):
    l = len(s)
    i = 0
    curnode = root
    if root == None:
        print("")
        return

    while(i < l):
        cur = s[i]
        if curnode == None:
            break
        if cur == "1":
                curnode = curnode.right
               
        else:
                curnode = curnode.left
               
        i+=1

        if curnode.data.isalnum() or curnode.data in string.punctuation: 
            print(curnode.data, end = "")
            curnode = root
    return

##hackerrank isBST

def check_binary_search_tree_(root):
    
    if root == None: return True
    def cmp(x, y):
        if x == "ni": return "Low"
        if y == "ni": return "High"
        if x == "pi": return "High"
        if y == "pi": return "Low"
        if x < y: return "Low"
        elif x > y: return "High"
        else: return "Eq"
        
    def help(tree, lower, upper):
        #lower and upper bounds of current tree node
        if tree == None:
            return True
        cur = tree.data
        if cmp(cur, upper) == "Low" and cmp(cur, lower) == "High":
            rlo = cur
            rup = upper
            llo = lower
            lup = cur
            return help(tree.left, llo, lup) and help(tree.right, rlo, rup)
        else: return False
        
    return help(root, "ni", "pi")
        

##







