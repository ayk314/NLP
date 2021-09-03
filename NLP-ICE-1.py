"""
Ali Khan, Rachel Johnson, Kaitlynn Whitney
UNT CSCE 4290/5290
NLP-ICE-1
"""
import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

# fetch article
response = urllib.request.urlopen('https://text.npr.org/2021/06/26/1009487890/spacexs-new-rocket-factory-is-making-its-texas-neighbors-mad')
html = response.read()

# initialize bs4
soup = BeautifulSoup(html, "html5lib")

# parses article and extracts text
text = soup.find('article').get_text(strip=True)

# gets all words as tokens
tokens = [t for t in text.split() if t.isalpha()]

clean_tokens = tokens[:]

# remove all stopwords
for token in tokens:
    if token.lower() in stopwords.words('english'):
        clean_tokens.remove(token)

# build frequency distribution
freq = nltk.FreqDist(clean_tokens)

# gives 10 most common words
print(freq.most_common(10))

# plot the graph
freq.plot(10, cumulative=False)
