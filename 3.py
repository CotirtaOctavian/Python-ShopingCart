import requests
import csv

class StockItem(object):

    def __init__ (self, open, high, low, close,)
        self.open = open
        self.high = high
        self.low = low
        self.close = close



class GetStockFinance(object):

    def __init__(self, url, stockindex):
        self.url = url
        self.stockindex = stockindex

    def get_stock_finance(self):
        download = requests.get(self.url+self.stockindex+'.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)

    def get_stock_finance_return_set(self):
        download = requests.get(self.url + self.stockindex + '.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    return set_obiecte_StockItem

class WriteReadToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, continut):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(continut)
    def read_from_csv(self,...):
        return set_obiecte_StockItem



a = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/','AAPL')
csv_de_scris = a.get_stock_finance()
b = WriteToCsv('test.csv')
b.write_to_csv(csv_de_scris)