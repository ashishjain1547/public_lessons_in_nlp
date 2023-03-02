# import these modules
import nltk
from nltk.stem.wordnet import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
  
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
  
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))

print("went :", lemmatizer.lemmatize("went", pos ="v"))

print("easier :", lemmatizer.lemmatize("easier", pos ="a"))
print("cheaper :", lemmatizer.lemmatize("cheaper", pos ="a"))
print("best :", lemmatizer.lemmatize("best", pos ="a"))
print("drilling :", lemmatizer.lemmatize("drilling", pos ="v"))
print("hammering :", lemmatizer.lemmatize("hammering", pos ="v"))


"""
print("went :", lemmatizer.lemmatize("went", pos = nltk.stem.wordnet.VERB))

AttributeError: module 'nltk.stem.wordnet' has no attribute 'VERB'
"""

"""
Try Out Lemmatizer from SpaCy.
There is also a BiText Lemmatizer.



(base) C:\Users\Ashish Jain\OneDrive\Desktop>python lemma.py
rocks : rock
corpora : corpus
better : good
went : go
easier : easy
cheaper : cheap
best : best
drilling : drill
hammering : hammer
"""