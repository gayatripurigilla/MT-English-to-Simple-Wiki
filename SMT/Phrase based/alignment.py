from collections import defaultdict
import string

def findAlignment(simple, normalAligned, normal, simpleAligned):
	
	wordAlignment = defaultdict(lambda: defaultdict(int))				
	# wordIndexnormal = defaultdict(lambda: -1)
	# wordIndexsimple = defaultdict(lambda: -1)
	table = str.maketrans("","", string.punctuation)
	simple  = simple.strip().split()
	for i in range(len(simple)):
		simple[i] = simple[i].translate(table)
		
		
	normal = normal.strip().split()
	for i in range(len(normal)):
		normal[i] = normal[i].translate(table)


	normalAligned = normalAligned.strip().split(" })")
	normalAligned = normalAligned[1:]
	count = 0
	for key in normalAligned:
		words = key.split('({')
		if len(words)>1 and words[1]!='':
			normalWord = words[0].strip()
			normalWord = normalWord.translate(table)
			indices = words[1].split()
			for i in indices:
				i = int(i)
				wordAlignment[count][i-1] = 1
		count += 1
				
	simpleAligned = simpleAligned.strip().split(" })")
	simpleAligned = simpleAligned[1:]
	count = 0
	for key in simpleAligned:
		words = key.split('({')
		if len(words)>1 and words[1]!='':
			simpleWord = words[0].strip()
			simpleWord = simpleWord.translate(table)
			indices = words[1].split()
			for i in indices:
				i= int(i)
				wordAlignment[i-1][count] = 1			
		count +=1

	return wordAlignment, normal, simple
