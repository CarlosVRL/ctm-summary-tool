# CTM Summary Tool

**Create CTM Position Summaries.**

## Installation

First, if you have not done so already, install [Python 3](https://www.python.org/downloads/).

## Usage

CTM Position Summaries require (3) inputs:

* 1 Chart Data (With Loaded CTM Settings)

* 2 Strategy Tester Data (List of Trades)

* 3 Strategy Description (Name, Stop Loss)

You can obtain inputs (1) and (2) from TradingView:

<img src="https://www.tradingview.com/x/cRb5ceOg" width="550">

You will need to create input (3) using a configuration file

```
# config.properties
name=<name>
long_stop=<long-stop-percent>
```

Usage:

```
$ python app.py -h
INFO: CTM Position Summary Tool
INFO: 
INFO: INPUTS
usage: ctm-summary-tool [-h] chart strategy config

Create formatted CTM Position Summary output

positional arguments:
  chart       chart data
  strategy    strategy tester data
  config      strategy description

options:
  -h, --help  show this help message and exit
```

Example:

```
$ python app.py test/resources/chart-data.csv test/resources/strategy-tester-data.csv test/resources/config.properties 
INFO: CTM Position Summary Tool
INFO: 
INFO: INPUTS
INFO: > chart    : test/resources/chart-data.csv
INFO: > strategy : test/resources/strategy-tester-data.csv
INFO: > config   : test/resources/config.properties
INFO:
INFO: SUMMARY
INFO: > asset        : ETHUSD_CTM221105
INFO: > status       : Long Trade Active
INFO: > entry        : 1251.8
INFO: > stop_val     : 1101.58
INFO: > stop_percent : 12.0
INFO: > gain_val     : 12.29
INFO: > gain_percent : 0.98
INFO: > long_val     : 41.95
INFO: > time         : 2023-01-06 18:00:00
INFO:
INFO: OUTPUT
INFO: > summary.csv
INFO:
INFO: Summary Complete
```

## TODO

* Design an automated mechanism for pulling inputs (1) and (2)
* Add functionality for short-side positions
