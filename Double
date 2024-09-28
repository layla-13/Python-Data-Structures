class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None 
        
class Double :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.length = 0 
        
    def beg(self, data) :
        new = Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            new.next = self.head
            self.head.prev = new
            self.head = new 
        
        self.length += 1 
        
    def end(self, data) :
        new = Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else :
            self.tail.next = new
            new.prev = self.tail 
            
            self.tail = new 
            
        self.length += 1
        
    def insert_btw(self, data, pos) :
        new = Node(data)
        if self.head == None :
            self.head = new
            self.tail = new
        else : 
            current = self.head 
            
            for _ in range(pos - 1) :
                current = current.next 
            
            new.prev = current
            new.next = current.next
            
            # After new forms bond, now the existing bond must be broken
            current.next = new
            
        self.length += 1
     
    def delbeg(self) :
        if self.head == None :
            print('Empty list')
            return 
        else :
            remove = self.head 
            self.head = self.head.next 
            return 
        self.length -= 1 
        
    def delend(self) :
        if self.head == None :
            print('Empty list')
            return 
        else :
            remove = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        
    def del_btw(self, pos) :
        if self.head == None :
            print('Empty list')
            return 
        else : 
            current = self.head 
            for _ in range(pos - 1) :
                current = current.next 
            
            remove = current.next 
            current.next = remove.next 
        self.length -= 1
    
    
    def trav(self) :
        current = self.head
        
        while current :
            print(current.data, end = " -> ")
            current = current.next
        print("None") 
        
        
a = Double()  
print('Adding 10,8,6 in beginning')
a.beg(10)
a.beg(8)
a.beg(6)
a.trav()

print('\nAdding 12,14,16 in end')
a.end(12)
a.end(14)
a.end(16)
a.trav() 

print('\nInserting 11 at index 3')
a.insert_btw(11, 3)
a.trav()

print('\nDeleting 1st element')
a.delbeg()
a.trav()

print('\nDeleting last element')
a.delend()
a.trav() 

print('\nDeleting 11 from elements')
a.del_btw(2)
a.trav() 

