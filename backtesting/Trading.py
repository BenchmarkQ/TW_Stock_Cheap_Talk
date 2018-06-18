import strategy as sty
import pandas as pd
import dataloader as dl
import pdb


class Trading():
    def __init__(self, indicator_data, initial_money, transaction_cost):
        self.data = dl.DataLoader()
        self.indicator = indicator_data[0]
        self.num = indicator_data[1]
        self.money = initial_money
        self.cost = transaction_cost
        self.stock_number = 0
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
        stock_number_list, money_list, asset_list = self.trading_action(list(trading_detail.iloc[:,1]), list(trading_detail.iloc[:,0]))
        af_trading = pd.DataFrame({'money': money_list, 'stock_number': stock_number_list, 'asset': asset_list})
        af_trading.index = trading_detail.index
        #trading_detail = pd.merge(trading_detail, af_trading,)
        pdb.set_trace() 
    def trading_action(self, value_list, price_list):
        asset_list = []
        history_money_list = []
        history_stock_number_list = []
        def trading_logit(value, price ,money, stock_number):
            if value == 'Long':
                if price*1000 <= money:
                    money = money - price * 1000
                    stock_number = stock_number + 1
                    return (money, stock_number)
                elif price*1000 > money:
                    return (money, stock_number)
                else:
                    raise ValueError('Please check the type of price and money')
            elif value == 'Short':
                if stock_number >= 1:
                    money = money + price*1000 * stock_number
                    stock_number = 0
                    return (money, stock_number)
                elif stock_number == 0:
                    return (money, stock_number)
                else:
                    raise ValueError('Please check the type of price and money')
            elif value == 'Hold':
                return (money, stock_number)
        for value, price in zip(value_list, price_list):
            self.money, self.stock_number = trading_logit(value, price , self.money , self.stock_number)    
            asset = self.money + self.stock_number*price*1000
            asset_list.append(asset)
            history_stock_number_list.append(self.stock_number)
            history_money_list.append(self.money)
        return history_stock_number_list, history_money_list, asset_list

if __name__ == '__main__':
    test_strategy = sty.NaiveStrategy('0050', 2000, 1)
    indicator = test_strategy.main()
    Trading(indicator, 100000, 0.05).main()
