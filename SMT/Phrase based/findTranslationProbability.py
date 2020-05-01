from collections import defaultdict
import sys
import math

countSimple = defaultdict(lambda: defaultdict(int))
sumCountNormal = defaultdict(int)
countNormal = defaultdict(lambda: defaultdict(int))
sumCountSimple = defaultdict(int)


def findTranslationProbability(phrasesFile):

	f = open (phrasesFile, 'r')
	for line in f:
		phrases = line.strip().split('\t')
		if len(phrases) == 2:
			countSimple[phrases[0]][phrases[1]]+=1
			sumCountNormal[phrases[0]]+=1
			countNormal[phrases[1]][phrases[0]]+=1
			sumCountSimple[phrases[1]]+=1
	f.close

	data=[]
	for key in countSimple:
		for key1 in countSimple[key]:
			translationProbability = math.log(float(countSimple[key][key1])/sumCountNormal[key])
			data.append(key1+'\t'+key +'\t'+str(translationProbability))

	f=open('translationProbabilityTargetGivenSource.txt','w')
	f.write('\n'.join(data))
	f.close()

	data=[]
	for key in countNormal:
		for key1 in countNormal[key]:
			translationProbability = math.log(float(countNormal[key][key1])/sumCountSimple[key])
			data.append(key1+'\t'+key+'\t'+str(translationProbability))

	f=open('translationProbabilitySourceGivenTarget.txt','w')
	f.write('\n'.join(data))
	f.close()

def main():
	if len(sys.argv)!=2:
		print ("Usage :: python3 findTranslationProbability phrases.txt")
		sys.exit(0)

	findTranslationProbability(sys.argv[1])

if __name__ == "__main__":
    main()
