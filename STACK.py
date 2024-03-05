#Use of stack without a class but with functions
'''
Applications of Stack Data Structure

To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order.
In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.
In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack.
When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.
'''

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


print(push([1,2,3,4,5],6)) #direct dherai value input garna sakiyo


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
        if (check_empty(stack)):
            return "Stack is empty"
        self.stack.pop()
        return self.stack   
              
s1= Stack()
print(s1.pop())     #esma shuru batai enque garna parxa natra khali         