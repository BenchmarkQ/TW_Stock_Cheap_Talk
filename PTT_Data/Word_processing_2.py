import pandas as pd
import json
import jieba
import jieba.analyse
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pdb
import os

path = os.getcwd()
jieba.set_dictionary('dict.txt.big')
jieba.analyse.set_stop_words('stops.txt')
with open('test.txt','r') as f:
    data = json.load(f)
dicts = list()
for d in data.values():
    #list_tmp = [jieba.cut(text) for text in d]
    list_tmp = [jieba.analyse.extract_tags(text) for text in d]
    list_tmp = [x for l in list_tmp for x in l]
    dicts += [s for s in list_tmp if s.split() and len(s)>1]
countD = Counter(dicts)
print(countD)
#f = open('test.txt','r').read()
font = path + '/wt001.ttf'
wordclound = WordCloud(font_path=font,width =1000,height = 860,margin =2).generate(json.dumps(dicts,ensure_ascii = False))
plt.imshow(wordclound) 
plt.axis('off')
plt.show()
wordclound.to_file('test.png')
