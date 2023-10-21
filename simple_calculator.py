from stack import Stack

class SimpleCalculator:
	def __init__(self):
		"""
		Instantiate any data attributes
		"""
		self.history = []
		pass

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		log = (input_expression,)
		if '+' in input_expression:
			try:
				a,b = (float(i.strip()) for i in input_expression.split('+'))
				log = (input_expression, a+b)
			except:
				log = (input_expression, 'Error')
		elif '-' in input_expression:
			try:
				a,b = (float(i.strip()) for i in input_expression.split('-'))
				log = (input_expression, a-b)
			except:
				log = (input_expression, 'Error')
		elif '*' in input_expression:
			try:
				a,b = (float(i.strip()) for i in input_expression.split('*'))
				log = (input_expression, a*b)
			except:
				log = (input_expression, 'Error')
		elif '/' in input_expression:
			try:
				a,b = (float(i.strip()) for i in input_expression.split('/'))
				log = (input_expression, a/b)
			except:
				log = (input_expression, 'Error')
		else:
			log = (input_expression, 'Error')
		self.history.append(log)
		return log[-1]

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.history