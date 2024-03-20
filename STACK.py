#Use of stack without a class but with functions
#stack follows lifo and that is all that is needed to know
'''
Applications of Stack Data Structure

To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order.
In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.
In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack.
When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.
memory management
backtracking
'''

def create_stack():
    stack =[] #empty array, so whenever we call this function an empty array called stack is returned
    return stack

def check_empty(stack): #there is no use of creating a createstack functio if we are going to give an array as a parameter
    return len(stack)==0 #returns true or false and is the one of the most confusing to me

def push(stack,item):
    stack.append(item) #LIFO vayera append ra pop mazale kaam garxa and we are lucky because this is python
    print("Pushed item :"+ str(item))
    return stack

def pop(stack): #esma item ko value chaiyena kinabhane last kai ta niskini ho j value vayeni
    if check_empty(stack)==True:
        return "Stack is empty"
    return stack.pop()    


print(push([1,2,3,4,5],6)) #direct dherai value input garna sakiyo


#Using stack as a class 
class Stack:
    def __init__(self):#as soon as we create an object using the stack class an empty array of stack will be created
        self.stack =[] #so the varaible we use here is used everywhere self.stack

    def check_empty(self):
        return len(self.stack)==0 #this again returns a boolean

    def push(self,item):
        self.stack.append(item) #the item is pushed and the stack is updated
        print("Pushed item: "+str(item))
        return self.stack # the updated stack after push will be returned

    def pop(self):
        if (check_empty()):
            return "Stack is empty"
        self.stack.pop()
        return self.stack   
              
s1= Stack()
print(s1.pop())     #esma shuru batai enque garna parxa natra khali         