import strategy as sty
import pandas as pd
import dataloader as dl
import pdb


class Trading():
    def __init__(self, indicator_data):
        self.data = dl.DataLoader()
        self.indicator = indicator_data[0]
        self.num = indicator_data[1]
    def main(self):
        try:
            self.stock = self.data.get_stock_data(self.num, self.indicator.index[0].year, self.indicator.index[0].month)
        except:
            print('Using the Fake Data')
            self.stock = pd.read_csv('/home/qin/workspace/TW_Stock_Cheap_Talk/stock_EDA/tw_50.csv', index_col = 0)
            self.stock.index = pd.to_datetime(self.stock.index)
            self.stock = self.stock[self.indicator.index[0]:self.indicator.index[-1]]
            self.stock = self.stock[['close']]
        trading_detail = pd.merge(self.stock, self.indicator, left_index = True, right_index = True)
        pdb.set_trace() 
    def trading_action(self, value_list):
        def trading_logit(value):
            if value == 'Long':
                pass
            elif value == 'Short':
                pass
            elif value == 'Hold':
                pass

if __name__ == '__main__':
    test_strategy = sty.NaiveStrategy('0050', 2000, 1)
    indicator = test_strategy.main()
    Trading(indicator).main()
