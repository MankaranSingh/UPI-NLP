import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet

String = 'mankaran singh should be payedd 60 rupees'

Sentences = nltk.sent_tokenize(String)
Tokens = []
for Sent in Sentences:
    Tokens.append(nltk.word_tokenize(Sent)) 
Words_List = [nltk.pos_tag(Token) for Token in Tokens]



print (Words_List)
