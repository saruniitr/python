#
# stockcli.py
# The purpose of this module is to provide a command line interface to
# query historic data of a Stock using its ticker symbol
#

import os
import sys
import argparse
from models import StockEntity


def get_stock_data(**kwargs):
	symbol = kwargs.get('symbol', None)
	date_range = kwargs.get('daterange', 'today')

	if symbol is None:
		raise ValueError

	symbols = symbol.split(',')
	for sym in symbols:
		print('Symbol:', sym)
		stock = StockEntity(sym, date_range)
		stock.display_data()

	pass


def run():
	parser = argparse.ArgumentParser()

	parser.add_argument("symbol", help="Stock ticker symbol", action="store")
	parser.add_argument("daterange",
						help="Date range specified in multiples of days, \
						weeks, months or range of dates.Examples are 'today', \
						'1d', '5d', '1w', '1m', 'start to end')",
						action="store")

	args = parser.parse_args()
	try:
		get_stock_data(symbol=args.symbol, daterange=args.daterange)
	except ValueError as e:
		print("Invalid arguments")


if __name__ == "__main__":
	run()
