# from datetime import datetime, timedelta
import datetime
import pandas as pd
import yfinance as yf
import statistics
import math
from dateutil.relativedelta import relativedelta


#identify highly correlated assets
def corranalysis():
    pass

#optimize weights of assets in a portfolio
def optimizeportfolio():
    pass

def calculaterisk():
    pass

def calculatereturn():
    pass


if __name__ == "__main__":

    stockvalues = []
    returns = []

    start = "2017-01-01"
    end = "2021-12-23"
    symbol = "SPY"

    timenow = datetime.datetime.now()
    years_ago = timenow - relativedelta(years=6)

    try:
        ethdata = yf.download(symbol, years_ago, timenow, interval="1d")
    except OverflowError:
        pass

    ethdatadict = ethdata['Close'].to_dict()
    stockvalues = list(ethdatadict.values())
    for idx, stockvalue in enumerate(stockvalues[1:]):
        returns.append(round(((stockvalue-stockvalues[idx])/stockvalues[idx]), 2))

    avgdailyreturn = (sum(returns)/len(returns))
    stddevreturns = round((statistics.pstdev(returns) * math.sqrt(365)), 2)
    annualreturn = round(((avgdailyreturn + 1) ** 365 - 1), 2)

    print(annualreturn * 100)
    print(stddevreturns * 100)


