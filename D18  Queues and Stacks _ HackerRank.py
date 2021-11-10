import sys
class node:
    def __init__(self,Data):
        self.Data = Data
        self.next = None

class Solution:
    size = 0
    size1 = 0
    # Write your code here
    def __init__(self):
        self.Head = None
        self.Head1 = None
    def pushCharacter(self,Data):
        newn = node(Data)
        if (self.Head == None):
            self.Head = newn
        else:
            newn.next = self.Head
            self.Head = newn
        Solution.size += 1
    def Display(self):
        temp = self.Head
        while(temp != None):
            print(temp.Data,end = " ")
            temp = temp.next
        print()   
    def Display1(self):
        temp = self.Head1
        while(temp != None):
            print(temp.Data,end = " ")
            temp = temp.next
        print()
    def enqueueCharacter(self,Data):
        newn = node(Data)
        if (self.Head1 == None):
            self.Head1 = newn
        else:
            temp = self.Head1
            while(temp.next != None):
                temp = temp.next
            temp.next = newn
        Solution.size1 += 1
    def popCharacter(self):
        temp = self.Head
        return temp.Data
        self.Head = temp.next
        
        
    def dequeueCharacter(self):
        temp = self.Head1
        return temp.Data
        self.Head1 = temp.next
        
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

obj.Display()  
obj.Display1()  
obj.popCharacter()
obj.dequeueCharacter()
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    