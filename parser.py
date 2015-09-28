__author__ = 'Mehdi'

# tokenize
# normalize =
    # case fold
    # remove stop words
    # stemming
# make an inverted index

from bs4 import BeautifulSoup
import nltk
# nltk.download('punkt')

doc = open("reuters21578.tar/reut2-000.sgm")
soup = BeautifulSoup(doc, "html.parser")

for body in soup.find_all('body'):
    textOnly = body.get_text()
    tokens = nltk.word_tokenize(textOnly)
    print tokens
