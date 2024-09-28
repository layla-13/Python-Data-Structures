class Node :
    def __init__(self, data) :
        self.data = data 
        self.next = None 
        
class Circular :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.length = 0 
        
    def beg(self, data) :
        new = Node(data)
        if self.head == None :
            self.head = new
            self.tail = new 
            # connected to itself
            new.next = new
        else :
            new.next = self.head 
            self.tail.next = new
            self.head = new  
        self.length += 1 
        
    def end(self, value) :
        new = Node(value)
    
        if self.head is None :
            self.head = new
            self.tail = new
            
            new.next = new
        else :
            self.tail.next = new 
            new.next = self.head
            self.tail = new
        self.length += 1 
        
    def del_beg(self) :
    
        if self.head is None :
            return
        elif self.head == self.tail:  # Only one element
            self.head = None
            self.tail = None
            self.length -= 1 
        else :
            self.head = self.head.next 
            self.tail.next = self.head
            
            self.length -= 1 
            
    def del_end(self) :
    
        if self.head is None :
            return
        elif self.head == self.tail:  # Only one element
            self.head = None
            self.tail = None
            self.length -= 1
        else :
            current = self.head 
            
            while current.next != self.tail :
                current = current.next
            
            current.next = self.head
            self.tail = current
            self.length -= 1 
            
    def trav(self) :
        current = self.head
        
        while current :
            print(current.data, end = " -> ")
            current = current.next
            if current == self.head :
                break
        print('Head') 
        
a = Circular()
a.beg(10)
a.end(20)
a.trav()

a.beg(90)
a.end(70)
a.trav()

a.del_end()
a.trav()
