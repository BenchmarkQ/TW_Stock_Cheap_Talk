import pandas as pd
import math
import pdb
import twstock
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/qin/workspace/MM_project/Spot/backtest')
import interface
plt.style.use('seaborn')
import seaborn as sns
tw_50 = pd.read_csv('tw_50.csv',index_col = 0)
tw_50.index = pd.to_datetime(tw_50.index)
tw_50_inv = pd.read_csv('tw_50_inv.csv',index_col = 0)
tw_50_inv.index = pd.to_datetime(tw_50_inv.index)
tw_tech = pd.read_csv('tw_tech_100.csv', index_col = 0)
tw_tech.index = pd.to_datetime(tw_tech.index)
code_df = pd.DataFrame(twstock.codes).transpose()

def cal_HV(stock_df):
    '''
    歷史波動率的算法
    1、從市場上獲得標的股票在固定時間間隔(如每天、每周或每月等)上的價格。
    2、對於每個時間段，求出該時間段末的股價與該時段初的股價之比的自然對數。(開盤價減收盤價)
    3、求出這些對數值的標準差，再乘以一年中包含的時段數量的平方根(如，選取時間間隔為每天，則若扣除閉市，每年中有250個交易日，應乘以根號250)，得到的即為歷史波動率。 
    '''
    diff = (stock_df['close'] - stock_df['open'])/stock_df['open']
    history_volatility = diff.std() * math.sqrt(250)
    return history_volatility
hv_tw_50  =  cal_HV(tw_50)
hv_tw_50_inv = cal_HV(tw_50_inv)
pdb.set_trace()
