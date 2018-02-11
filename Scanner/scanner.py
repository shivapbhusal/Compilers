# Python implemntation of a Scanner 

class DFA:
	currentState=None

	def __init__(self,states, alphabet, tranFunction,startState,acceptStates):
		self.states=states
		self.alphabet=alphabet
		self.tranFunction=tranFunction
		self.startState=startState
		self.acceptStates=acceptStates
		self.currentState=startState
		return 

	def stateTransition(self,inputList):
		if ((self.currentState,inputList) not in self.tranFunction.keys()):
			self.currentState=None 
			return 
		self.currentState=self.tranFunction[(self.currentState,inputList)]
		return 

	def acceptState(self):
		return self.currentState in acceptStates

	def goToInitial(self):
		self.currentState=self.startState

	def runInputList(self,inputList):
		self.goToInitial()
		for inputs in inputList:
			self.stateTransition(inputs)
			continue 
		return self.acceptState()

states={0,1,2,3}
alphabet={'a','b','c','d'}
tf=dict()

tf[(0, 'a')] = 1

tf[(0, 'b')] = 2

tf[(0, 'c')] = 3

tf[(0, 'd')] = 0

tf[(1, 'a')] = 1

tf[(1, 'b')] = 2

tf[(1, 'c')] = 3

tf[(1, 'd')] = 0

tf[(2, 'a')] = 1

tf[(2, 'b')] = 2

tf[(2, 'c')] = 3

tf[(2, 'd')] = 0

tf[(3, 'a')] = 1

tf[(3, 'b')] = 2

tf[(3, 'c')] = 3

tf[(3, 'd')] = 0

start_state = 0

accept_states = {2, 3}

d = DFA(states, alphabet, tf, start_state, accept_states)
inp_program = list('abcdabcdabcd')
print (d.runInputList(inp_program))






