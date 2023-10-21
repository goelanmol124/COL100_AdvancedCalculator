from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		super().__init__()
		self.history2 = []

	def evaluate_expression(self, input_expression, h = True):
		try:
			list_tokens = self.tokenize(input_expression)
			if (not self.check_brackets(list_tokens) ) or list_tokens == "Error" or len(list_tokens)== 0:
				log = (input_expression, "Error")
				ans = "Error"
			else:
				ans = self.evaluate_list_tokens(list_tokens)
				if ans != "Error":
					ans = float(ans)
				log = (input_expression,ans)
			#log)
			if h == True:
				self.history2.append(log)
			return ans
		except Exception as e:
			ans = "Error"
			log = (input_expression,"Error")
			if h == True:
				self.history2.append(log)
			return ans

	def tokenize(self, input_expression):
		lst =  []
		num = False
		for i in input_expression:
			if i in '}{)(+-/*':
				if num:
					lst.append(int(num))
					num = False
				lst.append(i)
			elif i in '0123456789':
				if num:
					num = num + i
				else:
					num = i
			elif i in 'abcdefghijklmnopqrstuvwxyz':
				return 'Error'
		if num:
			lst.append(int(num))
			num = False
		return lst

	def check_brackets(self, list_tokens):
		bracket = Stack()
		simplebracket = False
		for i in list_tokens:
			if i == '(':
				bracket.push('(')
				simplebracket = True
			elif i == '{':
				bracket.push('{')
				if simplebracket:
					return False
			elif i == ')':
				if bracket.pop() != '(':
					return False
			elif i == '}':
				if bracket.pop() != '{':
					return False
		if len(bracket) != 0:
			return False
		return True

	def evaluate_list_tokens(self, list_tokens):
		equations = Stack()
		count = 0
		Found = False
		lst = []
		for i in list_tokens:
			if i == '(' or i == '{':
				count += 1
				if Found == False:
					Found = True
				else:
					lst.append(i)
			elif i == ')' or i == '}':
				count -= 1
				if count == 0:
					Found = False
					res = self.evaluate_list_tokens(lst)
					equations.push(res)
				else:
					lst.append(i)
			elif Found == True:
				lst.append(i)
			else:
				equations.push(i)
		
		try:
			if len(equations) == 1:
				return equations.pop()
			equations = str(equations).split()[::-1]
			for op in '/*-+':
				while op in equations:
					ind = equations.index(op)
					a = float(equations[ind-1])
					c = float(equations[ind+1])
					if op == '/':
						equations[ind] = a/c
					if op == '*':
						equations[ind] = a*c
					if op == '+':
						equations[ind] = a+c
					if op == '-':
						equations[ind] = a-c
					equations.pop(ind-1)
					equations.pop(ind)
			if len(equations) == 1:
				return equations.pop()
			
		except Exception as e:
			return "Error"
		

	def get_history(self):
		return self.history2[::-1]

'''
if __name__ == "__main__":
	calculator = AdvancedCalculator()
	assert calculator.evaluate_expression("2 +                                 3") == 5, "Wrong"
	assert calculator.evaluate_expression("")
	assert (calculator.evaluate_expression('') == "Error"), "Wrong"
	assert calculator.evaluate_expression('2/3') == 2/3, "Wrong"
	assert calculator.evaluate_expression('2+3') == 2+3, "Wrong"
	assert calculator.evaluate_expression('2-3') == -1, "Wrong"
	assert calculator.evaluate_expression('2*3') == 2*3, "Wrong"
	assert calculator.evaluate_expression('2') == 2, "Wrong"
	assert calculator.evaluate_expression('(2)') == 2, "Wrong"
	assert calculator.evaluate_expression('((2/3))') == 2/3, "Wrong"
	assert calculator.evaluate_expression('5{3-2}*') == 'Error', "Wrong"
	assert calculator.evaluate_expression('(2/{3*10})') == "Error", "Wrong"
	assert calculator.evaluate_expression('(2/(3*10))') == 2/30, "Wrong"
	assert calculator.evaluate_expression('2+2+3') == 7, "Wrong"
	assert calculator.evaluate_expression('111+12+13/5') == 111 + 12 + 13/5, "Wrong"
	assert calculator.evaluate_expression('1146*(46)') == 1146*46, "Wrong"
	assert calculator.evaluate_expression('45565/(25+56)') == 45565/(25+56), "Wrong"
	assert calculator.evaluate_expression('12+(5+(8))') == 12+5+8, "Wrong"
	assert calculator.evaluate_expression('1*5-9+5/4') == 1*5-9+5/4, "Wrong"
	assert calculator.evaluate_expression('2+(') == "Error", "Wrong"
	assert calculator.evaluate_expression('3+{){}}') == "Error", "Wrong"
	assert calculator.evaluate_expression('645drew64') == "Error", "Wrong"
	assert calculator.evaluate_expression('89357t9368q4f4[]') == "Error", "Wrong"
	assert calculator.evaluate_expression('4354454+85679+9/}{()54395*7983464+9') == "Error", "Wrong"
	assert calculator.evaluate_expression('546+2') == 548, "Wrong"
	assert calculator.evaluate_expression('5+4+3/3+4*8+{6+5-(9+8*5/4-12+(12-13))}') == 5+4+3/3+4*8+(6+5-(9+8*5/4-12+(12-13))), "Wrong"
	print("Done")
'''