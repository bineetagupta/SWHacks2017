import nltk
from nltk.corpus import wordnet as wn
#run: classifier.classify(["dancing", "writing"], ["poem", "poetry", "swimming", "caligraphy", "singing"])
class ResumeClassifier:
	def setupNLTK(self):
		nltk.download()
	def classify(self, kw, words):
		for keyword in kw:
			kwc = wn.synsets(keyword)
			if(len(kwc) != 0):
				kwc = kwc[0]
			else:
				continue

			for word in words:
				wc = wn.synsets(word)
				if(len(wc) != 0):
					wc = wc[0]
				else:
					continue
				dist = kwc.dist(wc)

		def compareResume(self, keywords, resume1, resume2):
			pass

classifier = ResumeClassifier()
print(classifier.classify(["dancing", "writing"], ["poem", "poetry", "swimming", "caligraphy", "singing", "writing", "dancing"]))