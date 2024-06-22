class Queue:
	def __init__(self, capacity):
		self.__capacity = capacity
		self.__data = []

	def is_empty(self):
		return len(self.__data) == 0
	
	def is_full(self):
		return len(self.__data) == self.__capacity
	
	def dequeue(self):
		return self.__data.pop(0)
	
	def enqueue(self, value):
		self.__data.append(value)

	def front(self):
		return self.__data[0]
	
# Test
myQueue = Queue(capacity=5)

myQueue.enqueue(1)
myQueue.enqueue(2)

print(myQueue.is_full())
print(myQueue.front())
print(myQueue.dequeue())
print(myQueue.front())
print(myQueue.dequeue())
print(myQueue.is_empty())