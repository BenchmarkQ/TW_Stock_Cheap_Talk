from hmmlearn.hmm import GaussianHMM
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import backtesting as bk
import pdb

n = 3 #suppose three states
dl = bk.dataloader.DataLoader()
data = dl.get_stock_data('0050', 2005, 1)
data = data['2012-01-01':]
volume = data['transaction']
close = data['close']
logDel = np.log(np.array(data['high']) - np.array(data['low']))
logRet_1 = np.array(np.diff(np.log(close)))#这个作为后面计算收益使用)))
logRet_5 = np.log(np.array(close[5:])) - np.log(np.array(close[:-5]))
logVol_5 = np.log(np.array(volume[5:])) - np.log(np.array(volume[:-5]))
logDel = logDel[5:]
logRet_1 = logRet_1[4:]
close = close[5:]
Date = pd.to_datetime(data.index[5:])
A = np.column_stack([logDel,logRet_5,logVol_5])
A = np.nan_to_num(A)
A[np.isneginf(A)] = 0
A[np.isinf(A)] = 0
model = GaussianHMM(n_components= n, covariance_type="full", n_iter=2000).fit(A)
hidden_states = model.predict(A)
plt.figure(figsize=(25, 18))
for i in range(model.n_components):
    pos = (hidden_states == i)
    plt.plot_date(Date[pos], close[pos], 'o', label='hidden state %d'%i,lw=2)
    plt.legend(loc = "left")
plt.show()
res = pd.DataFrame({'Date':Date,'logRet_1':logRet_1,'state':hidden_states}).set_index('Date')
plt.figure(figsize=(25, 18))
for i in range(model.n_components):
    pos = (hidden_states == i)
    pos = np.append(0,pos[:-1])#第二天进行买入操作)
    df = res.logRet_1
    res['state_ret%s'%i] = df.multiply(pos)
    plt.plot_date(Date,np.exp(res['state_ret%s'%i].cumsum()),'-',label='hidden state %d'%i)
    plt.legend(loc = 'left')
plt.show()
long =  (hidden_states==0)  #做多))
short = (hidden_states==2) #做空))
long = np.append(0,long[:-1]) #第二天才能操作)
short = np.append(0,short[:-1]) #第二天才能操作)
res['ret'] =  df.multiply(long) - df.multiply(short)
plt.plot_date(Date,np.exp(res['ret'].cumsum()),'r-')
plt.show()
pdb.set_trace()
