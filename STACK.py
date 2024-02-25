#Use of stack without a class but with functions

def create_stack():
    stack =[] #empty array
    return stack

def check_empty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item) #LIFO vayera append ra pop mazale kaam garxa
    print("Pushed item :"+ str(item))
    return stack

def pop(stack): #esma item ko value chaiyena kinabhane last kai ta niskini ho j value vayeni
    if check_empty==True:
        return "Stack is empty"
    return stack.pop()    


print(push([1,2,3,4,5],6))


#Using stack as a class 
class Stack:
    def __init__(self):
        self.stack =[]

    def check_empty(self):
        return len(self.stack)==0

    def push(self,item):
        self.stack.append(item) 
        print("Pushed item: "+str(item))
        return self.stack

    def pop(self):
        if (check_empty()):
            return "Stack is empty"
        self.stack.pop()
        return self.stack   
              
s1= Stack()
print(s1.push(1))              