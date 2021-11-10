#Input (stdin)
#4
#2
#3
#4
#1
#Expected Output
#2 3 4 1

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        newn = Node(data)
        temp = head
        if (head == None):
            head = newn
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = newn
        return(head)

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
