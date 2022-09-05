# We can implement a stack using a list
stack = [4,5]

# add elements into the stack
stack.append(1)
stack.append(2)
stack.append(3)

print('Initial stack')
print(stack)

# use pop() operation to pop items from stack
stack.pop()
print('Stack after elements are popped:')
print(stack)

stack.append('Hello')
# Access the top of the stack
print(stack[0]);

# Check if stack is empty
print('Is stack empty: ', len(stack) == 0)