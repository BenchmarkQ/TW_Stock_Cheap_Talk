import sqlite3
import pdb
import pandas as pd
import numpy as np
import sys, os, time, io
import re

# setting
source_path_file = r'./test.txt'
base_path= r'C:\Users\rreal\Downloads\PTT_Data'

"""
with open('test.txt', 'r') as file:
    s = file.read()
    raw_text = eval(s)
conn = sqlite3.connect('PTTData.db')
c = conn.cursor()
c.execute('''CREATE TABLE PTT 
       (url text, title text, time text, main_content text, push_content text)''')
for raw_data in raw_text:
    url = raw_data['url']
    title = raw_data['title']
    time = raw_data['time']
    main_content = raw_data['main_content']
    push_content = ''.join(raw_data['push_content'])
    c.execute("INSERT INTO PTT (url, title, time , main_content, push_content) VALUES (?, ?, ?, ?, ?)", (url,title,time,main_content,push_content))
conn.commit()
conn.close()
"""
# load data
print( 'loading data from %s' % source_path_file )
with open( source_path_file, 'r') as f:
    s = f.read()
    raw_text = eval(s)

col_tags = ['url', 'title', 'time', 'main_content', 'push_content'] 
df = pd.DataFrame( columns=col_tags )
# analyzing data and reformating
print( 'analyzing data and reformating...' )
for idx, raw_data in enumerate(raw_text):
    url = raw_data['url']
    title = raw_data['title']
    time = raw_data['time']
    main_content = raw_data['main_content'].replace('\n', '\t').replace(',', '，')
    push_content = ''.join(raw_data['push_content']).replace('\n', '\t').replace(',', '，')
    df = df.append( pd.Series( [url, title, time, main_content, push_content], index=col_tags), ignore_index=True )
    print( 'processing... %d/%d' %((idx+1)//len(raw_text) , len(raw_text)) )
df.replace( ['\r\n', '\n', ',', '\u3000'], [' ', ' ', '，', ' '], inplace=True, regex=False)
# save data
print( 'saving data...' )
df.to_csv( base_path+ r'\pttData.csv' ,sep=',', na_rep='', encoding='utf-8', mode='w', header=True, index=False )
print( 'successfully save data at %s' % (base_path+ r'\pddData.csv') )
print( '\tsize of dataframe: ', df.shape )
print( '\tcol tags of dataframe is: ', col_tags )
