import csv
import re
import nltk
#nltk.download('all')
import string
import unicodedata
import sys
# import matplotlib
# import receipt
from imp import reload

reload(sys)
# sys.setdefaultencoding("utf-8")

new_file = csv.reader(open("base_teewts.csv", "r", encoding="utf-8"))

list_docs = []
list_label = []

def remove_hashtag(text):
  words = text.split()

  for i in words:
    if i.startswith("#"):
      words.remove(i)

  text = ' '.join(words)
  return text

def remove_URL(text):
  clean_text = re.match('(.*?)http.*?\s?(.*?)', text)
  if clean_text:
    return clean_text.group(1)
  else:
    return text

def remove_stopwords(text):
  regex = re.compile('[%s]' % re.escape(string.punctuation))

  a = []

  words = text.split()
  for t  in words:
    new_token = regex.sub(u'', t)
    if not new_token == u'':
      a.append(new_token)

  stopwords = nltk.corpus.stopwords.words('portuguese')
  content = [w for w in a if w.lower().strip() not in stopwords]

  clean_text = []
  for word in content:
    nfkd = unicodedata.normalize("NFKD", word)
    palavraSemAcento = u''.join([c for c in nfkd if not unicodedata.combining(c)])
    q = re.sub("[^a-zA-Z0-9 \\\]", " ", palavraSemAcento)

    clean_text.append(q.lower().strip())

  tokens = [t for t in clean_text if len(t) > 2 and not  t.isdigit()]
  ct = " ".join(tokens)

  return ct


arquivoPrincipal = csv.writer(open("nltk.csv", "w"))
# count = 0

for row in new_file:
  doc_word = remove_stopwords(row[0])
  doc_word = remove_hashtag(doc_word)
  doc_word = remove_URL(doc_word)

  tokens    = nltk.word_tokenize(doc_word)
  classes   = nltk.pos_tag(tokens)
  entidades = nltk.chunk.ne_chunk(classes)

  # arquivo = csv.writer(open("NPL-PENNPOS/nltk" + str(count) + ".csv", "w"))
  # arquivo.writerow(classes)

  arquivoPrincipal.writerow(entidades)

  # print(nltk.corpus.mac_morpho.words(entidades))
  print(classes)

  # count += 1

