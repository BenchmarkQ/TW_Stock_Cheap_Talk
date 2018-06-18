import pandas as pd
import pdb

class TradeResult():
    def __init__(self, trading_detail):
        self.detail = trading_detail
        self.asset = trading_detail['asset']
        self.cal_profit()
        self.cal_annual_rate
        self.cal_profit
        self.cal_sharp_ratio
    def cal_win_rate(self):
        pass
    def cal_profit(self):
        self.profit = (self.asset[-1] - self.asset[0])/self.asset[0]
    def cal_sharp_ratio(self):
        pass
    def cal_annual_rate(self):
        pass
    
    
