import pandas as pd
import dataloader as dl
import pdb

class Strategy():
    def __init__(self):
        self.data = dl.DataLoader()
    def cal_action(self, date_list, value_list):
        action_df = pd.DataFrame({'date': date_list, 'value': value_list})
        action_df.index = pd.to_datetime(action_df['date'])
        return action_df[['value']]
    
class NaiveStrategy(Strategy):
    def __init__(self, stock_num, start_year, start_month):
        Strategy.__init__(self)
        self.num = stock_num
        self.year = start_year
        self.month = start_month
    def load_data(self):
        try:
            self.use_data = self.data.get_stock_data(str(self.num), self.year, self.month)
        except:
            print('Using Fake Data')
            self.use_data = pd.read_csv('/home/qin/workspace/TW_Stock_Cheap_Talk/stock_EDA/tw_50.csv', index_col = 0)
            self.use_data.index = pd.to_datetime(self.use_data.index)

    def main(self):
        self.load_data()
        use_data = self.use_data
        date_list = use_data.index 
        indicator = (use_data['close'] - use_data['open'])/(use_data['open'])
        indicator = indicator.shift(1).dropna()
        indicator = pd.DataFrame(indicator, columns = ['sign'])
        def trans_value(value):
            if value > 0.012:
                return 'Short'
            elif value < -0.012:
                return 'Long' 
            elif value < 0.012 and value > -0.012:
                return 'Hold'
        indicator['value'] = indicator['sign'].apply(trans_value)
        return (indicator[['value']], self.num)
        
if __name__ == '__main__':
    strategy = NaiveStrategy('0050', 2000, 1)
    strategy.main()
    pdb.set_trace()
