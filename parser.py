__author__ = 'Mehdi'

# tokenize
# normalize =
    # case fold
    # remove stop words
    # stemming
# make an inverted index

from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords


# nltk.download('punkt') due to errors

# Getting Stop Words
stops = set(stopwords.words('english'))
# Getting the collection
doc = open("reuters21578.tar/reut2-000.sgm")
# Parsing the collection
soup = BeautifulSoup(doc, "html.parser")

# Getting body text, tokenizing, lower case, and stopwords removal
for body in soup.find_all('body'):
    textOnly = body.get_text()
    tokens = nltk.word_tokenize(textOnly)
    words = [w.lower() for w in tokens]
for w in words:
    if w not in stops:
        count = 0
        print w
        ++count
print count
