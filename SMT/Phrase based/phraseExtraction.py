import sys
from alignment import findAlignment
def checkConsistency(fstart, fend, estart, eend, wordAlignment, normal, simple):
	flag = 1

	listNormal =[]
	listSimple = []

	for i in range(len(normal)):
		if i >= estart and i<=eend:
			listNormal.append(i)

	for i in range(len(simple)):
		if i >= fstart and i <=fend:
			listSimple.append(i)

	for e in listNormal:
		for f in range(len(simple)):
			if wordAlignment[e][f] == 1:
				if f >= fstart and f <=fend:
					continue
				else:
					flag = 0

	for f in listSimple:
		for e in range(len(normal)):
			if wordAlignment[e][f] == 1:
				if e >= estart and e <=eend:
					continue
				else:
					flag = 0

	return flag


def findPhrase(fstart, fend, estart, eend, normal, simple):

	phraseN = []
	#print fstart, fend, estart, eend
	for i in range(estart,eend+1):
		phraseN.append(normal[i])
	# print(len(normal), "normal ")
	# print(len(simple), "simple")
	# print(fstart, fend, estart, eend)
	# print(phraseN)
	phraseS = []
	if fend + 1 <= len(normal):
		for i in range(fstart,fend+1):
			phraseS.append(simple[i])

	return [' '.join(phraseN), ' '.join(phraseS)]

def extract(fstart, fend, estart, eend, wordAlignment, normal, simple):
	if fend == -1:
		# print("fend = -1")
		return 'NULL'

	else:
		flag = checkConsistency(fstart, fend, estart, eend, wordAlignment, normal, simple)
		if flag:
			return findPhrase(fstart, fend, estart, eend, normal, simple)
		else:
			# print("flag is 0")
			return 'NULL'

def extractPhrases(normalToSimple, simpleToNormal):

	data=[]
	fns = open(normalToSimple, 'r')
	fsn = open(simpleToNormal,'r')
	count = 0
	while True:
		count+=1
		print (count)
		line = fns.readline()
		if line == "":
			break
		normalToSimple1 = fns.readline()
		normalToSimple2 = fns.readline()
		line = fsn.readline()
		simpleToNormal1 = fsn.readline()
		simpleToNormal2 = fsn.readline()
		wordAlignment, normal, simple = findAlignment(normalToSimple1, normalToSimple2, simpleToNormal1, simpleToNormal2)

		lNormal = len(normal)
		lSimple = len(simple)
		# print(wordAlignment)
		phrases = []
		for estart in range(lNormal):
			for eend in range(estart,(lNormal)):
				fstart = lSimple
				fend = -1
				for i in wordAlignment:
					if i <= eend and i >= estart:
						for j in wordAlignment[i]:
							fstart = min(j, fstart)
							fend = max(j, fend)
				if ((eend - estart) <= 20) or ((fend -fstart) <= 20) :
					phrases.append([estart, eend, fstart, fend])
		# print phrases
		for key in phrases:
			estart = key[0]
			eend = key[1]
			fstart = key [2]
			fend = key[3]
			phrase = extract (fstart, fend,estart, eend,wordAlignment, normal, simple)
			# print (phrase)
			if phrase!= 'NULL':
				# print (phrase)
				data.append(phrase[0]+'\t'+phrase[1])
	fns.close()
	fsn.close()

	f=open('phrases.txt','w')
	f.write('\n'.join(data))
	f.close()
	
def main():
	if len(sys.argv)!=3:
		print ("Usage :: python3 phraseExtraction.py normalToSimple simpleToNormal")
		sys.exit(0)
	extractPhrases(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
