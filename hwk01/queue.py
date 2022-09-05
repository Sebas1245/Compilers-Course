# We can implement a queue using a list
queue = []

# Enqueue items
queue.append(1)
queue.append(2)
queue.append(3)
print('Initial queue')
print(queue)

# Dequeue an item
queue.pop(0);
print('Queue aftere dequeing an item')
print(queue)

# get the size of the queue
print('Size of the queue ', len(queue))

# check if queue is empty
print('Is queue empty? ', len(queue) == 0)

