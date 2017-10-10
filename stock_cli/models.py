#
# File that include data models
#

import os
import re
import time
import datetime
import numpy as np
import pandas as pd
from pandas_datareader import data as web
from pandas_datareader._utils import RemoteDataError

class DataProvider():
	"""
	Helper class to abstract Data acquisition. At the moment we use Yahoo
	finance as source but the idea is to source data from other alternate
	sources in future.
	"""
	def __init__(self, **kwargs):
		self.source = kwargs.get('source', 'yahoo')
		self.df = None

	def acquire_data(self, symbol, start, end):
		retries = 0
		df = None
		while df is None and retries < 3:
			try:
				df = web.DataReader(symbol, self.source, start, end)
			except RemoteDataError as e:
				raise RemoteDataError
			except:
				retries += 1
				time.sleep(1)
				df = None
		if df is not None:
			df = df[df["Adj Close"].notnull()]

		self.df = df
		return df


class StockEntity(DataProvider):
	"""
	Data structure that represents a Stock entity.
	"""
	def __init__(self, symbol, date_range):
		super().__init__(source='yahoo')
		self.symbol = symbol;
		self.df = None
		self.start, self.end = self.calc_num_days(date_range.lower())

	def __str__(self):
		return '{0}'.format(self.symbol);

	def calc_num_days(self, date_range):
		start = end = ""
		""" process date range and determine no of days """
		if len(date_range.split()) == 1:
			days = 0
			interval = {"today": 1, "d": 1, "w": 7, "m": 31}
			match = re.match('([0-9]+)([a-z]+)', date_range)
			if match:
				groups = match.groups()
				if groups[1] in interval.keys():
					days += int(groups[0]) * interval[groups[1]]
				else:
					days += interval["today"]
			else:
				days += interval["today"]

			end = datetime.date.today()
			start = end - datetime.timedelta(days - 1)
		elif len(date_range.split()) == 3:
			groups = date_range.split()
			if groups[1] == "to":
				start = datetime.datetime.strptime(groups[0], '%d-%m-%Y').date()
				end = datetime.datetime.strptime(groups[2], '%d-%m-%Y').date()
			else:
				start = end = datetime.date.today()

		return start, end

	def display_data(self):
		df = None
		try:
			df = self.acquire_data(self.symbol, self.start, self.end)
		except RemoteDataError as e:
			print("No data for ticker {0}: Invalid Symbol?".format(self.symbol))
			return

		if df is None:
			print("{0}: No Records to display", self.symbol)
			return
		with pd.option_context('display.max_rows', None):
			print(df)
