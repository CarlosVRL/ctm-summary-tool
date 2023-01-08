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

## TODO

* Design an automated mechanism for pulling inputs (1) and (2)
* Add functionality for short-side positions
