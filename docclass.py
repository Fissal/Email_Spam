import re

def getwords(doc):
        splitter = re.compile('\\W*')
        words = [s.lower() for s in splitter.split(doc) if len(s)>2 and len(s)<20]
        # print words
        return dict([(w,1) for w in words])

# print getwords("fissal wnats to eat pizza right now, ok bitches")

class classifier:
    def __init__(self, getfeatures, filename=None):
        self.fc = {}
        self.cc = {}
        self.getfeatures = getfeatures


    def incf(self, f, cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat] += 1

    def incc(self, cat):
        self.cc.setdefault(cat,0)
        self.cc[cat] += 1

    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0

    def totalcount(self):
        return sum(self.cc.values())
    def categories(self):
        return self.cc.keys()

    def train(self, item, cat):
        features = self.getfeatures(item)
        for f in features:
            self.incf(f, cat)
        self.incc(cat)

    def fprob(self, f, cat):
        if self.catcount(cat) == 0 : return 0
        return self.fcount(f, cat)/ self.catcount(cat)

    def weightedprob(self, f, cat, prf, weight=1.0, ap=0.5):
        basicprob = prf(f, cat)
        totals = sum([self.fcount(f,c) for c in self.categories()])
        bp = ((weight*ap) + (totals*basicprob))/(weight+totals)
        return bp


class naivebayes(classifier):
    def __init__(self, getfeatures):
        classifier.__init__(self, getfeatures)
        self.threshold = {}

    def docprob(self, item, cat):
        features = self.getfeatures(item)
        p = 1
        for f in features:
            p*= self.weightedprob(f, cat, self.fprob)
        return p

    def prob(self, item, cat):
        catprob = self.catcount(cat)/self.totalcount()
        docprob = self.docprob(item, cat)
        return docprob*catprob


    def setthreshold(self, cat, t):
        self.threshold[cat] = t

    def getthreshold(self, cat):
        if cat not in self.threshold: return 1.0
        return self.threshold[cat]

    def classify(self, item, default=None):


        probs = {}
        max = 0.0
        for cat in self.categories():
            probs[cat] = self.prob(item, cat)
            if cat == 'good':
                catrev = 'bad'
            else:
                 catrev = 'good'

            if probs[cat]>max:
                max = probs[cat]
                best = cat
            else:
                best = catrev
        for cat in probs:
            if cat == best: continue
            if probs[cat]*self.getthreshold(best)>probs[best]: return default
        return best


def sampleTrain(c1,Dir1,Dir2):
    import os
    cwd = os.getcwd()
    Path = cwd + Dir1

    for F in os.listdir(Path):
        File = open(Path + '\\%s'%F,'r')
        for line in File:
            c1.train(line,'good')


    Path2 = cwd + Dir2
    #print Path2
    for J in os.listdir(Path2):
        File2 = open(Path2 + '\\%s'%J,'r')
        for line in File2:
            c1.train(line,'bad')



c1 = naivebayes(getwords)
sampleTrain(c1,'\\Ham_T','\\Spam_T')


import os
cwd = os.getcwd()
PA = cwd + '\\spam'
Lis = []
for K in os.listdir(PA):
    tesstFile = open(PA + '\\%s'%K,'r')

    Var = c1.classify(tesstFile.read(),default='unknown')
    Lis.append(Var)

print Lis
Count = 0
for l in Lis:
    if l == 'bad':
        Count += 1

print (float(Count)/len(Lis))*100






















# c1 = naivebayes(getwords)
# sampleTrain(c1)
# print c1.classify('quick rabbit', default='unknown')
# print c1.classify('quick money', default='unknown')
# c1.setthreshold('bad', 3.0)
# print c1.classify('quick money',default='unknown')
# for i in range(10): sampleTrain(c1)
# print c1.classify('quick money', default='unknown')

