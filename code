class Node :
    def __init__(self, value) :
        self.value = value 
        self.next = None 
        
class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.length = 0 
        
    def start(self, value) :
        new = Node(value)
        if self.head == None :
            self.head = new 
            self.tail = new
        else :
            new.next = self.head 
            self.head = new
        self.length += 1
        
    def end(self, value) :
        new = Node(value)
    
        if self.head is None :
            self.head = new
            self.tail = new
        else :
            self.tail.next = new 
            self.tail = new 
        self.length += 1 
        
    def insert(self, value, index) :
        new = Node(value) 
        
        if index < 0 or index > self.length :
            return False
        
        # If list is empty
        if self.length == 0 :
            self.head = new
            self.tail = new 
         
        # If inserting at beginning   
        if index == 0 :
            self.start(value)
            return True
            
        else :
            current = self.head 
            for _ in range(index - 1) :
                current = current.next
            # Now current is the preceeding element of new
            # Here new and existing both together point at same thing
            new.next = current.next
            current.next = new
        self.length += 1
        return True
        
    def p1(self) :
        remove = self.head
        
        if self.length == 1 :
            self.head = None
            self.tail = None
            return remove
        else :   
            self.head = self.head.next
            
            remove.next = None
        self.length -= 1
        return remove
        
    def pend(self) :
        remove = self.tail
        
        if self.length == 1 :
            self.head = None
            self.tail = None
            return remove
        else :   
            current = self.head 
            
            while current.next is not self.tail :
                current = current.next 
                
            self.tail = current
            current.next = None
            self.length -= 1 
            return remove
        
    def pbw(self, position) :
        current = self.head 
            
        for _ in range(position - 1) :
            current = current.next 
            
        remove = current.next 
        current.next = remove.next 
        self.length -= 1
            
        return remove
    
    def trav(self) :
        current = self.head
        
        while current :
            print(current.value, end = " -> ")
            current = current.next
        print("None") 
        
    def data(self) :
        print(f"Total elements : {self.length}")
        key = input("\nWhat element you want to search : ")
        
        current = self.head
        i = 0
        while current :
          
            if current.value == int(key) :
                print(f"Element found at position {i}")
                return
            i += 1 
            current = current.next
        print("Element not found")
        return
        
        
a = LinkedList()
print("Adding 5,10,15,20,25")
a.start(10)
a.end(20)
a.end(25)
a.insert(15, 1)
a.insert(5, 0)
a.trav()

print("\nRemoving 1st element")
a.p1()
a.trav()

print("\nRemoving last element")
a.pend()
a.trav()

print("\nRemoving element at position 1")
a.pbw(1)
a.trav()

# print(a.head.value)
# print(a.tail.value)
# print(a.length)

# Line 38 is very important   
# In insert, when adding at start or end, since I am calling a function, increment is happening twice. So, return
