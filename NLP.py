import csv
import re
import nltk
import string
import unicodedata
import sys
from imp import reload

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

new_file = csv.reader(open("base_teewts.csv", "r"))

list_docs = []
list_label = []

def remove_hashtag(text):
  words = text.split()
  
  for i in words:
    if i.startswitch("#"):
      words.remove(i)
      
  text = ' '.join(words) 
  return text

def remove_URL(text):
  clean_text = re.match("(.*?http.*?\s?(.*?)", text)
  if clean_text:
    return clean_text.group(1)
  else:
    return text
    