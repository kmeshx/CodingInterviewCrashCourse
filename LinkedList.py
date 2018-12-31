##Author: Kusha Maharshi
##Email: kmaharsh@andrew.cmu.edu

#Prelim testing finished. Include more tests and edge cases to ensure correctness. 

"""
Documentation:

LinkedList class:
--> Property (client): kind - "Single" or "Double"
--> Property (interface): size
--> Uses "Node" class for creating linked list; is a wrapper itself

Node class:
--> Property: data
--> Property: next
--> Property: prev

Functions implemented for linked list class:

__init__
__repr__
addToEnd (Single and Double)
addToStart (Single and Double)
insertFromEnd (Double)
insertFormStart (Single and Double)
DLLCheck (Double)
getAtIndexStart (Single and Double)
deleteFirst (Single and Double)
deleteAll (Single and Double)
deleteAllLinear (Single and Double)
cyclePoint (Single)

"""
##LinkedList Implementation Starts

class Node():
    
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self, kind):
        self.start = None
        self.end = None
        try:
            assert(kind == "Single" or kind == "Double")
        except:
            raise Exception("Type of LinkedList must be Single or Double")
        self.kind = kind
        self.size = 0
    def __repr__(self):
        if self.kind == "Single":
            sep = "->"
        else:
            sep = "<->"
        
        p = self.start
        ret = str(p.data)
        while(p.next != None):
            print(p.data)
            p = p.next
            ret = ret + " " + sep + " " + str(p.data)
            
        #ret = ret + str(p.data) + " " + sep + " "
        assert(p.next == None)
        return ret
    
    def addToEnd(self, x):
        if self.start == None:
            self.start = Node(x)
            if self.kind == "Double":
                self.end = self.start
                
        else:
            p = self.start
            while(p.next != None):
                p = p.next
            assert(p.next == None)
            p.next = Node(x)
            if self.kind == "Double":
                p.next.prev = p
                self.end = p.next
        self.size += 1
            
    def addToStart(self, x):
        if self.start == None:
            self.start = Node(x)
        else:
            temp = self.start
            self.start = Node(x)
            assert(self.start.next == None)
            self.start.next = temp
            if self.kind == "Double":
                self.start.next.prev = self.start
        self.size += 1
            
    def insertFromStart(self, rank, x):
        #rank starting at 0
        p = self.start
        if rank == 0:
            self.addToStart(x)
            return
        
        assert(rank != 0)
        def help(cur, curRank):
            if curRank == rank-1:
                tmp = cur.next
                cur.next = Node(x)
                assert(cur.next.next == None)
                cur.next.next = tmp
                if self.kind == "Double":
                    cur.next.prev = cur
                    if tmp != None:
                        tmp.prev = cur.next
                    
                return
            help(cur.next, curRank+1)
        help(p, 0)
        self.size += 1
        
    def insertFromEnd(self, rank, x):
        #rank starting at 1
        if self.kind == "Single":
            self.insertFromStart(self.size - rank, x)
            return
        if rank == 1:
            self.addToEnd(x)
            return
        
        p = self.end
        count = 1
        while(p.prev != None):
            if count == rank-1:
                tmp = p.prev
                tmp2 = p
                p.prev = Node(x)
                p.prev.prev = tmp
                if tmp != None:
                    tmp.next = p.prev
                p.prev.next = tmp2
                break
                
            p = p.prev
            count+=1
        
        self.size+=1

        
    def DLLCheck(self):
        try:
            assert(self.kind == "Double")
        except:
            raise Exception("Type of LinkedList must be Double to use DLLCheck")
        
        stack = []
        p = self.start
        while(p.next != None):
            stack.append(p)
            p = p.next
        assert(p.next == None)
        stack.append(p)
        p = self.end
        while(p.prev != None):
            cur = stack.pop()
            if p!=cur:
                return False
            p = p.prev
        assert(p.prev == None)
        cur = stack.pop()
        if p!=cur:
            return False
        assert(stack == [])
        return True
        
    def getAtIndexStart(self, indexI):
        #index starts at zero
        #returns None if not found indexI
        p = self.start
        if indexI == 0: return p.data
        index = 0
        while(p.next != None):
            
            p = p.next
            index += 1
            if index == indexI:
                return p.data
                
        return None
        
    def deleteFirst(self, x):
        
        p = self.start
        if p.data == x:
            self.start = p.next
            self.size -= 1
            if self.kind == "Double":
                self.start.prev = None
            return
        
        while(p.next != None):
            cur = p.next.data #starts at very first one
            if cur == x:
                tmp = p.next
                p.next = p.next.next
                #erase pointer of deleted node
                tmp.next = None
                self.size -= 1
                if self.kind == "Double":
                    p.next.prev = p
                return
            p = p.next
        return "Not Found"
                
        
    def deleteAll(self, x):
        og = self.size
        #worst case complexity O(n^2)
        while(self.deleteFirst(x) != "Not Found"):
            continue
            
        if self.size == og:
            return "Not Found"
        return
        
    def deleteAllLinear(self, x):
       
            
        dummy = Node(None)
        
        dummy.next = self.start
        self.start = dummy
        p = self.start
        #print("p: ", p.data, p.next.data)
        flag = False
        while(p.next != None):
            cur = p.next.data #starts at very first one
            #print("cur p: ", p.data)
            #print("next p: ", p.next.data)
            if cur == x:
                flag = True
                tmp = p.next
                p.next = p.next.next
                #erase pointer of deleted node
                #tmp.next = None
                self.size -= 1
                if self.kind == "Double":
                    p.next.prev = p
                
                
            else:
                p = p.next
            
            if p == None: break
            #print("post update: ", p.data)
            
        self.deleteFirst(None)
        if flag: return "Not Found"
        
    def deleteAtIndexStart(self, index):
        
        raise Exception("Not Yet Implemented")
        
    def removeDuplicates(self):
        #loop through linked list, add to set, if visited, remove
        raise Exception("Not Yet Implemented")
    
    def opPlus(self):
        raise Exception("Not Yet Implemented")
        
    def reverse(self):
        raise Exception("Not Yet Implemented")
        
    def findCollision(self, other):
        raise Exception("Not Yet Implemented")
        
    def cyclePoint(self):
        assert(self.kind == "Single")
        #b + ln + r
        #b + lm + r'
        #2b + 2ln + 2r = b + lm + r'
        #b + l(2n - m) + (2r - r') = 0
        #WTS: r = r' for some non-negative ints m, n
        #Set r = r'
        #b + l(2n - m) + r = 0
        #(b + r)/l = m - 2n
        #so there will exist m, n as needed when l | (b+r)
        #will choose r = b%l (DANG)
        
        turtle = self.start
        hare = self.start
        flag = False
        while(turtle.next != None and hare.next != None):
            
            turtle = turtle.next
            hare = hare.next
            if hare != None:
                hare = hare.next
            else:
                hare = self.start
                
            print(turtle, hare)
            if hare == turtle:
                print("yay" + str(hare.data))
                flag = True
                meet = hare
                assert(meet == turtle)
                break
        if not flag: return None
        else:
            #first find loop size  
            turtle = meet
            
            og = meet
            print("meet: ", meet)
            loop_size = 0
            while(turtle.next != None and hare.next != None):
                
                turtle = turtle.next
                loop_size += 1
                if turtle == og:
                    break
        print("loop: ", loop_size)
        assert(loop_size <= self.size)
        #find loop point
        p = self.start
        runner = self.start
        count = 0
        while(count < loop_size):
            p = p.next
            count += 1
        runner = p
        p = self.start
        while(runner.next != None and p.next != None):
            if p == runner:
                return (p, p.data)
            runner = runner.next
            p = p.next
            
        return "Something went wrong"
        

def testLinkedList():
    #cycle detection tests should be made by user using cyclePoint function, all functions assume acyclic linked list
    t1 = LinkedList("Single")
    t1.addToStart(2)
    print(t1)
    t1.addToStart(3)
    print(t1)
    t1.addToStart(4)
    print(t1)
    t1.addToEnd(5)
    print(t1)
    t1.addToEnd(6)
    print(t1)
    assert(t1.size == 5)
    t1.insertFromStart(1, 11)
    print(t1)
    t1.insertFromStart(0, 12)
    print(t1)
    t1.insertFromStart(7, 13)
    print(t1)
    t1.insertFromStart(4, 14)
    print(t1)
    assert(t1.size == 9)
    
    assert(t1.getAtIndexStart(3) == 3)
    assert(t1.getAtIndexStart(0) == 12)
    assert(t1.getAtIndexStart(8) == 13)
    assert(t1.getAtIndexStart(9) == None)
    
    print("Delete Tests Start")
    t1.deleteFirst(12)
    print(t1)
    t1.deleteFirst(3)
    print(t1)
    t1.deleteFirst(13)
    print(t1)
    t1.addToStart(2)
    print(t1)
    t1.addToStart(2)
    print(t1)
    t1.deleteAll(2)
    print(t1)
    t1.addToStart(6)
    print(t1)
    t1.addToStart(6)
    print(t1)
    t1.deleteAllLinear(6)
    print(t1)
    assert(t1.deleteFirst(32) == "Not Found")
    assert(t1.deleteAll(32) == "Not Found")
    print("Single tests end")
    
    
    t1 = LinkedList("Double")
    t1.addToStart(2)
    print(t1)
    t1.addToStart(3)
    print(t1)
    t1.addToStart(4)
    print(t1)
    t1.addToEnd(5)
    print(t1)
    t1.addToEnd(6)
    print(t1)
    assert(t1.size == 5)
    t1.insertFromStart(1, 11)
    print(t1)
    t1.insertFromStart(0, 12)
    print(t1)
    t1.insertFromStart(7, 13)
    print(t1)
    t1.insertFromStart(4, 14)
    print(t1)
    assert(t1.size == 9)
    t1.insertFromEnd(1, 111)
    print(t1)
    #t1.insertFromEnd(0, 121)
   # print(t1)
    t1.insertFromEnd(7, 131)
    print(t1)
    t1.insertFromEnd(4, 141)
    print(t1)
    assert(t1.size == 12)
    assert(t1.DLLCheck())
    
    assert(t1.getAtIndexStart(3) == 3)
    assert(t1.getAtIndexStart(0) == 12)
    assert(t1.getAtIndexStart(11) == 111)
    assert(t1.getAtIndexStart(12) == None)
    
    print("Delete Tests Start")
    t1.deleteFirst(12)
    print(t1)
    t1.deleteFirst(3)
    print(t1)
    t1.deleteFirst(13)
    print(t1)
    t1.addToStart(2)
    print(t1)
    t1.addToStart(2)
    print(t1)
    t1.deleteAll(2)
    print(t1)
    t1.addToStart(6)
    print(t1)
    t1.addToStart(6)
    print(t1)
    t1.deleteAllLinear(6)
    print(t1)
    assert(t1.deleteFirst(32) == "Not Found")
    assert(t1.deleteAll(32) == "Not Found")
    print("Double tests end")
    
    assert(t1.DLLCheck())
    
    t3 = LinkedList("Single")
    t3.start = Node(1)
    t3.size += 1
    t3.start.next = Node(2)
    t3.size += 1
    t3.start.next.next= Node(3)
    t3.size += 1
    t3.start.next.next.next= Node(4)
    t3.size += 1
    t3.start.next.next.next.next = Node(5)
    t3.size += 1
    t3.start.next.next.next.next.next = t3.start.next.next
    print("Cycle Tests")
    #print(t3)
    print(t3.cyclePoint())
    
#testLinkedList()
    
## Linked List Implementation Ends
    