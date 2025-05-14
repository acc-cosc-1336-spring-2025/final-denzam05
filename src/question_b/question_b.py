#write functions here, don't add input('') statements here!

import os

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name
    
def write_to_file( file_name):
    file = open(file_name, 'w')

    file.write('AAPL' + '\t' + ' Apple Inc\n')
    file.write('CAT' + '\t' + 'Caterpillar\n')
    file.write('EK' + '\t' + 'Eastman Kodak\n')
    file.write('GOOG' + '\t' + 'Google\n')
    file.write('MSFT' + '\t' + 'Microsoft\n')

    file.close ()
    
def read_from_file(file_name):
    file = open(file_name, 'r')

    file_lines = file.read()
    file.close()

    print(file_lines)

    

def get_stock_list():
    stock_list = []
    with open('stock_file.dat', 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)
            if len(parts) == 2:
                symbol, company_name = parts
                stock_list.append(Stock(symbol, company_name))
    return stock_list
