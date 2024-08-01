class Node: 
    # constructor
    def __init__(self, data, next=None):
        self.data=data
        self.next=next 

class LinkedList: 
    # constructor
    def __init__(self):
        self.list='S' # this stands for stack, so the linked list will be a stack by default
        self.top=None # used for stack
        self.head=None # used for queue
        self.tail=None # used for queue
        self.size=0 # used to show amount of elements

    # turns the linked list into a queue
    def queue(self): 

        if self.list=='Q': # this stands for queue
            print("The linked list is already a queue")
            return # exits function
        
        else:
            self.list='Q'

            if(self.isEmpty()): 
                self.head=self.top
                
            else: #if there's at least one element,then the head and tail need to be assigned 
                self.head=self.top #the top of the stack becomes the head for the queue
                start=self.head

                #goes to the end of the linked list, the last element will be the tail 
                while (start!=None):
                    prev=start
                    start=start.next
                    
                self.tail=prev #assigns the tail  

            print("The linked list is now a queue")      

    #turns the linked list into a stack
    def stack(self):

        if self.list=='S':
            print("The linked list is already a stack")
            return # exits function

        else:
            self.list='S' #linked list is changed to stack
            self.top=self.head #the head of the queue becomes the top for the stack
            print("The linked list is now a stack")
    
    # adds elements to the stack
    def push(self, data):

        newnode= Node(data, self.top) #creates a new node 
        self.top=newnode #replaces the head of the queue with the new node
        self.size+=1

        self.display() #displays the list
       
    #removes a number of elements from the stack
    def pop(self, num):

        count=self.size

        #checks if there are enough elements to pop out of the stack
        if (count-num<0):
            return print("ERROR")

        else: #pops the elements out of the stack  
            while(num>0):
                self.top=self.top.next #top is replaced with the top's next element 
                num-=1
                self.size-=1

            self.display()
    
    #adds element to the queue
    def enqueue(self, data):

        newnode= Node(data, None) #creates a new node 
 
        if(self.isEmpty()): #replaces the head of the queue with the new node
            self.head=newnode
  
        else:  
            self.tail.next=newnode #sets the tail's next element to the new node
            
        self.tail=newnode #replaces the tail of the queue with the new node
        self.size+=1

        self.display()

    #removes an element from the queue
    def dequeue(self):

        if(self.isEmpty()):
            return print("ERROR") 

        else:
            self.head=self.head.next #head is replaced with the head's next element 
            self.size-=1

        self.display()#displays the list

    #reverses the linked list using recursion
    def reverse(self, first):
        
        if(self.isEmpty()):
            return #exits function
        
        #checks if the linked list reaches the end
        if first.next==None:
            return first

        #reverses the linked list 
        newFirst = self.reverse(first.next)

        #Puts the first element at the end 
        first.next.next=first
        first.next=None

        return newFirst #this would return the head/top of the reversed linked list

    #finds the average
    def average(self):

        if(self.isEmpty()):
            return print("0")

        if self.list=='S':
            start=self.top

        if self.list=='Q':
            start=self.head

        average=0 #initializes average
        sum=0 #initializes sum
        count=self.size 
        
        #goes through all the elements in the linked list
        while(start!=None):
            sum+=start.data #adds all the numbers in linked list
            start=start.next #goes to the next element
 
        average=sum/count 
        average=round(average, 3) #rounds number to 3 decimal places
        print(average) 

    #displays the linkedlist
    def display(self):
       
        if(self.isEmpty()):
            return print('EMPTY')

        elif self.list=='S':
            start=self.top

        elif self.list=='Q':
            start=self.head

        count=self.size

        #prints out the linkedlist
        while(count>0):
            print(start.data,end=" ") #this makes the elements get printed out in the same line
            start=start.next
            count-=1
            
        print()# makes newline

    def isEmpty(self):
        if (self.size==0):
            return True
        else:
            return False

def main():
    linkedlist=LinkedList() 
    choice=""#intiliazes choice 

    print("Operations: stack, push, pop, queue, enqueue, dequeue, display, reverse, average, help, exit")

    while(choice!="exit"):

        choice=input("Operation:")
        choice=choice.lower() #makes characters in input all lowercase

        #linked list turns into a stack
        if(choice=="stack"):
                linkedlist.stack()
        
        elif(choice=="push"):
            if(linkedlist.list=='S'):
                #checks if the input is a number or not
                try:
                    num=int(input("Enter a Number:"))#converts input into an integer
                    linkedlist.push(num)
                except:
                    print("Invalid input")
            else:
                print("The linked list is not a stack")

        elif(choice=="pop"):
            if(linkedlist.list=='S'):
                try:
                    num=int(input("Enter amount to pop:"))#converts input into an integer
                    linkedlist.pop(num)
                except:
                    print("Invalid input")
            else:
                print("The linked list is not a stack")

        #linked list turns into a queue
        elif(choice=="queue"):
                linkedlist.queue()
        
        elif(choice=="enqueue"):
            if(linkedlist.list=='Q'):
                #checks if the input is a number or not
                try:
                    num=int(input("Enter a number:"))#converts input to integer
                    linkedlist.enqueue(num)
                except:
                    print("Invalid input")
            else:
                print("The linked list is not a queue")
        
        elif(choice=="dequeue"):
            if(linkedlist.list=='Q'):
                linkedlist.dequeue()
            else:
                print("The linked list is not a queue")
        
        #displays the linked list
        elif(choice=="display"):
            linkedlist.display()
        
        #reverse the linked list
        elif(choice=="reverse"):

            if(linkedlist.list=='S'):
                linkedlist.top=linkedlist.reverse(linkedlist.top)
                linkedlist.display()
            
            if(linkedlist.list=='Q'):
                linkedlist.head=linkedlist.reverse(linkedlist.head)
                linkedlist.display()
        
        #calculates the average of the numbers in the list
        elif(choice=="average"):
                linkedlist.average()
        
        #shows the list of the operations
        elif(choice=="help"):
                print("Operations: stack, push, pop, queue, enqueue, dequeue, display, reverse, average, help, exit")
        
        #this would be the last operation and would mean that 'input' didnt have a valid operation
        elif(choice!="exit"):
            print("Not a valid operation: Try again")
        
        print(" ") #used to make space between lines

main()