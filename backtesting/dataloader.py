import pandas as pd
import twstock
import pdb

class DataLoader():
    def __init__(self):
        self.code = pd.DataFrame(twstock.codes).transpose()
    def get_stock_data(self, stock_num, start_year, start_month):
        stock = twstock.Stock(str(stock_num))
        data = self.interface(stock, start_year, start_month)
        return data
    def interface(self,stock_obj ,start_year, start_month):
        data = stock_obj.fetch_from(start_year, start_month)
        date_list = [stock.date for stock in data]
        close_list = [stock.close for stock in data]
        open_list = [stock.open for stock in data]
        high_list = [stock.high for stock in data]
        capacity_list = [stock.capacity for stock in data]
        low_list = [stock.low for stock in data]
        turnover_list = [stock.turnover for stock in data]
        transaction_list = [stock.transaction for stock in data]
        df = pd.DataFrame({'date': date_list, 'close': close_list, 'open': open_list, 'high':high_list, 'capacity': capacity_list, 'low': low_list, 'turnover': turnover_list, 'transaction': transaction_list})
        df['date'] = pd.to_datetime(df['date'])
        df.index = df['date']
        return df[df.columns[1:]]
if __name__ == '__main__':
    dl = DataLoader()
    data = dl.get_stock_data('3310', 2016, 1)
    pdb.set_trace()

