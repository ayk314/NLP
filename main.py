import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

response = urllib.request.urlopen('http://php.net')

html = response.read()

# print(html)

soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)

# print(text)

tokens = [t for t in text.split()]

# print(tokens)

freq = nltk.FreqDist(tokens)

for key, value in freq.items():
    print(str(key) + ':' + str(value))

#freq.plot(20, cumulative=False)

clean_tokens = tokens[:]

sr = stopwords.words('english')

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

freq.plot(10, cumulative=False)
