#This module takes as input the bi-text corpuses and the number of sentences.
#It returns the training and testing dataset along with the sentence pairs. 

import random
import string
import sys
from collections import defaultdict

def preprocessing(numberOfSentences, sourceFile, targetFile):

    indices=defaultdict(int)
    trainingSource=[]
    trainingTarget=[]
    testingSource=[]
    testingTarget=[]
    
    
    for i in range(numberOfSentences):
        indices[random.randint(0,167689)] = 1

    with open(sourceFile,'r') as  fSource:
        for index,line in enumerate(fSource):
            if len(line)>0:
                line = line.strip()
                if indices[index] ==1:
                    trainingSource.append(line)
                else:
                    testingSource.append(line)
                
    with open(targetFile,'r') as  fTarget:
        for index,line in enumerate(fTarget):
            if len(line)>0:
                line = line.strip()
                if indices[index] ==1:
                    trainingTarget.append(line)
                else:
                    testingTarget.append(line)
    
            
    with open('Dataset/trainingSource.txt','w') as f:
        f.write('\n'.join(trainingSource))

    with open('Dataset/trainingTarget.txt','w') as f:
        f.write('\n'.join(trainingTarget))

    testingSource=testingSource[:25]
    with open('Dataset/testingSource.txt','w') as f:
        f.write('\n'.join(testingSource))

    testingTarget=testingTarget[:25]
    with open('Dataset/testingTarget.txt','w') as f:
        f.write('\n'.join(testingTarget))

    #return sentencePair

def main():
    if len(sys.argv)!= 4:
        print( "Usage :: python3 preprocess.py file_source file_target numberOfSentencesForTraining")
        sys.exit(0)
    
    numberOfSentences=int(sys.argv[3])
    preprocessing(numberOfSentences, sys.argv[1], sys.argv[2] )


if __name__ == "__main__":
    main()
