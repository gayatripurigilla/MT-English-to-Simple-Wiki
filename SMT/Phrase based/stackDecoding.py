import sys
from collections import defaultdict
import operator
import string

def findBestTranslation(finalTranslationProbability, inputFile):

	tp = defaultdict(dict)
	table = str.maketrans("","", string.punctuation)
	f=open(finalTranslationProbability,'r')
	for line in f:
		line = line.strip().split('\t')
		line[0] = line[0].translate(table)
		line[1] = line[1].translate(table)
		tp[line[0]][line[1]] = float(line[2])
	f.close()
	
	data = []
	f = open(inputFile,'r')
	for line in f:
		translationScore = defaultdict(int)
		translationSentence = defaultdict(list)
		words = line.strip().split(' ')
		for i in range(len(words)):
			words[i] = words[i].translate(table)
		count = 1
		for i in range(len(words)):
			translation = ''
			for j in range(len(words)-count+1):
				phrase = words[j:j+count]
				phrase = ' '.join(phrase)
				#print phrase
				if phrase in tp:
					translationPhrase = max(tp[phrase].items(), key=operator.itemgetter(1))[0]
					translationScore[count] += tp[phrase][translationPhrase]
					translation+=translationPhrase+' '
			if translation != '':
				translationSentence[count].append(translation)
			count += 1
		x = max(translationScore.items(), key=operator.itemgetter(1), default = 0)
		if x != 0:
			index = x[0]
		else: 
			index = 0
		finalTranslation = ' '.join(translationSentence[index])
		# data.append(words)
		data.append(finalTranslation)

	f = open('translation.txt','w')
	f.write('\n'.join(data))
	f.close()

def main():
	if len(sys.argv) != 3:                                                                               #check arguments
		print ("Usage :: python3 stackDecoding.py finalTranslationProbabilityTargetGivenSource.txt testingFile.txt ")
		sys.exit(0)

	findBestTranslation(sys.argv[1], sys.argv[2])

if __name__ == "__main__":                                                                              #main
    main()