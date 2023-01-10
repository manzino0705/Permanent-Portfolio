import pandas as pd
import numpy as np
import getpass
from pykrx import stock
from pykrx import bond
from datetime import date, timedelta, datetime
from check_weekend import check_weekend
        
day = check_weekend()
day = day[0:4] + day[5:7] + day[-2:]  

# 종목 코드, 종목명, 가격 정보 가져오기 
stock_code = stock.get_market_ticker_list() 
res = pd.DataFrame()
for ticker in stock_code:
    df = stock.get_market_ohlcv_by_date(fromdate=day, todate=day, ticker=ticker)
    df = df.assign(종목코드=ticker, 종목명=stock.get_market_ticker_name(ticker))
    res = pd.concat([res, df], axis=0)
    # time.sleep(1)
res = res.reset_index()

def pykrxData(): 
    return res