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
        self.use_data = self.data.get_stock_data(str(self.num), self.year, self.month)
    def main(self):
        self.load_data()
        use_data = self.use_data
        #long timeing
        
if __name__ == '__main__':
    strategy = NaiveStrategy('0050', 2000, 1)
    pdb.set_trace()
