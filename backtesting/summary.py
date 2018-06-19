import pandas as pd
import matplotlib.pyplot as plt
import pdb

class TradeResult():
    def __init__(self, trading_detail):
        plt.style.use('seaborn')
        self.detail = trading_detail
        self.asset = trading_detail['asset']
        self.cal_count()
        self.cal_profit()
        self.cal_profit()
        self.cal_win_rate()
    def cal_win_rate(self):
        asset_change = self.asset.diff().dropna()
        self.win_rate = len(asset_change[asset_change > 0])/self.count
    def cal_max_loss(self):
        asset_change = self.asset.diff().dropna()
        self.max_loss = min(asset_change)
    def cal_profit(self):
        self.profit = (self.asset[-1] - self.asset[0])/self.asset[0]
    def cal_count(self):
        self.count = len(set(self.asset))
    def plot(self):
        self.asset.plot()
        plt.show()
    
    
