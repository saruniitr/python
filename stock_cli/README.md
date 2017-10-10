# StockCLI
StockCLI is a simple command line utility to get historic prices of a Stock using its ticker symbol. At the moment it uses [Yahoo Finance](https://finance.yahoo.com/) as source but it can be extended to include other alternate sources.

We can provide date range either in terms of days, weeks, months or a range of dates specifying start and end dates.

### Usage
    usage: stockcli.py [-h] symbol daterange

    symbol - Stock ticker symbol
    daterange - Date range specified in multiples of days, weeks, months or range. Examples are 'today', '1d', '5d', '1w', '1m', 'start to end'


### Example usage and output

1. stockcli.py GOOG "today"
2. stockli.py GOOG "5d"
3. stockli.py GOOG "2w"
4. stockli.py GOOG "1m"
5. stockli.py GOOG "01-10-2017 to 10-10-2017"
<br>
...
