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
		return self.currentState

	def goToInitial(self):
		self.currentState=self.startState

	def runInputList(self,inputList):
		self.goToInitial()
		for inputs in inputList:
			self.stateTransition(inputs)
		return self.acceptState()


states={0,1,2,3}
alphabet={'a','b','c','d'}
tranFunction=dict()

tranFunction[(0, 'a')] = 1

tranFunction[(0, 'b')] = 2

tranFunction[(0, 'c')] = 3

tranFunction[(0, 'd')] = 0

tranFunction[(1, 'a')] = 1

tranFunction[(1, 'b')] = 2

tranFunction[(1, 'c')] = 3

tranFunction[(1, 'd')] = 0

tranFunction[(2, 'a')] = 1

tranFunction[(2, 'b')] = 2

tranFunction[(2, 'c')] = 3

tranFunction[(2, 'd')] = 0

tranFunction[(3, 'a')] = 1

tranFunction[(3, 'b')] = 2

tranFunction[(3, 'c')] = 3

tranFunction[(3, 'd')] = 0

start_state = 0

accept_states = {2, 3}

d = DFA(states, alphabet, tranFunction, start_state, accept_states)
inputString = [list('ab'),list('abcd'),list('abcdef'),list('aaa'),list('bcde')]

for strings in inputString:
	if d.runInputList(strings)==2 or d.runInputList(strings)==3:
		print(str(strings)+" "+"Accepted")
	else:
		print(str(strings)+" "+"Rejected")






