class Stack:
	def __init__(self, capacity):
		self.__capacity = capacity
		self.__data = []

	def is_empty(self):
		return len(self.__data) == 0
	
	def is_full(self):
		return len(self.__data) == self.__capacity
	
	def pop(self):
		return self.__data.pop(-1)
	
	def push(self, value):
		self.__data.append(value)

	def top(self):
		return self.__data[-1]
	

# Test
myStack = Stack(capacity=5)
myStack.push(1)
myStack.push(2)

print(myStack.is_full())
print(myStack.top())
print(myStack.pop())
print(myStack.top())
print(myStack.pop())
print(myStack.is_empty())