import pandas as pd

tw_50 = pd.read_csv('tw_50.csv', index_col = 0)
tw_50_inv = pd.read_csv('tw_50_inv.csv', index_col = 0)
tw_tech = pd.read_csv('tw_tech_100.csv', index_col = 0)
tw_50.index = pd.to_datetime(tw_50.index)
tw_50_inv = pd.to_datetime(tw_50_inv.index)
tw_tech = pd.to_datetime(tw_tech.index)

#前一天波動度
#近期價格變化
#外資動態
#消息面(ptt討論度)
