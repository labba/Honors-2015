apiList = []
funcClass = {}
curFunc = ""
func_class = 0

def processData(filename):
	funcApiList = {}	
	f = open(filename)	
	for line in f:
		if line[0] == '$':
			curFunc = line[1:]
			funcApiList[line[1:]] = []
		else:
			if curFunc != None:
				funcApiList[curFunc].append(line)
				if line not in apiList:
					apiList.append(line)
	funcClass[func_class] = funcApiList

def printData():
	for cl in funcClass:
		vectorMatrix = []	
		print "#" + str(cl)
		funcApiList = funcClass[cl]
		for func in funcApiList:
			newVector = []
			for api in apiList:
				if api in funcApiList[func]:
					newVector.append(1)
				else:
					newVector.append(0)
			vectorMatrix.append(newVector)
		

		for vector in vectorMatrix:
			s=""
			for i in vector:	
				s = s + str(i) + ','
			print s[:-1]
	


if __name__ == '__main__':
	s1 = raw_input()
	func_class = 1
	processData(s1)
	
	s2 = raw_input()
	func_class = 2	
	processData(s2)

	printData()
	
