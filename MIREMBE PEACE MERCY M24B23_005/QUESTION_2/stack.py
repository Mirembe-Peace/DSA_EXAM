#initializing a stack
stack = []

#pushing elements to the stack
stack.append(10)
stack.append(3)
stack.append(8)
stack.append(78)

#printing the created stack
print(f'the newly formed stack {stack}')

#removing an element from the stack
#last in first out so 78 will be removed
stack.pop() 

#printing the stack when one element is removed
print(f'the stack after removing one element{stack}')

#printing the stack elements from top to bottom
stack.reverse()
print(f'The stack top top to bottom {stack}')

#function to checking if the stack is empty
def check_if_stack_is_empty(stack):   #initializing a function to check if the stack is empty
    value = len(stack)                #using the len function to check the size of the stak
    if value == 0:                    #if the size of the stack is 0
        print('The stack is empty')
    else:                             #otherwise
        print(f'The stack is not empty, there are {value} elements')

checker = check_if_stack_is_empty(stack)


#clearing all elements from the stack
stack.clear()
#printing the cleared stack
print(f'the cleared stack {stack}')

#checking if the stack is empty after clearing all elements
def check_if_stack_is_empty(stack):   #initializing a function to check if the stack is empty
    value = len(stack)                #using the len function to check the size of the stak
    if value == 0:                    #if the size of the stack is 0
        print('The stack is empty')
    else:                             #otherwise
        print(f'The stack is not empty, there are {value} elements')

checker = check_if_stack_is_empty(stack)


# searching for an element in the stack
def linear_search(stack,target):
    for i in range(len(stack)):
        if stack[i] == target:
           index = stack[i]
    return index

target = int(input('Enter a number that is in the stack: '))
result = linear_search(stack,target)
if result is not None:
    print('The target is found at position: ',result)
else:
    print('The target is not found')




# DISCLAIMER!!!! even after the AI auto generate was disabled it was still showing up in my work but, i did not use it so it may appear in the screen shorts but i i did not use it