import sqlite3
import pdb

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

