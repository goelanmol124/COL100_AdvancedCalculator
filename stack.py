class Stack:
	def __init__(self):
		self.s = []
	
	def push(self, item):
		# Push an item to the stack
		self.s.append(item)
		

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		if len(self.s) == 0:
			return "Error"
		else:
			return self.s[-1]
		

	def pop(self):
		# Pop an item from the stack if non-empty
		if len(self.s) == 0:
			return "Error"
		return self.s.pop()
		pass

	def is_empty(self):
		# Return True if stack is empty, False otherwise
		if len(self.s) == 0:
			return True
		return False

	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		return ' '.join([str(i) for i in self.s[::-1]])

	def __len__(self):
		# Return current number of elements in the stack
		return len(self.s)