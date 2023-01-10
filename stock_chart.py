# 내가 가진 주식의 연 수익률 구하기
import numpy as np 
import pandas as pd 
import FinanceDataReader as fdr 

from check_weekend import check_weekend

day = check_weekend()
day = day[0:4] + '-'+ day[5:7] + '-'+day[-2:]  
lastyear = str(int(day[0:4])-1) + '-'+ day[5:7] + '-'+ day[-2:]  


def stock_profit(now_account):  
    
    stock_code = fdr.StockListing('KRX')
    
    # 1. 내 잔고에서 주식 이름만 뽑아오기 
    my_stocks = [] 
    for type, name, price,cnt in now_account:
        if type == 'stock': 
            ticker = stock_code[stock_code['Name']==name]['Code'].to_string(index=False).strip()
            my_stocks.append([ticker,name])
    
    # 2. 1년간 데이터 가져와서 수익률 계산 
    df = pd.DataFrame()
    for ticker,name in my_stocks : 
        df[name] = fdr.DataReader(ticker,lastyear, day)['Close']
    
    day_profit = df.pct_change() # 일일 수익률 
    year_profit = day_profit.mean()*252 # 연간 수익률 
    # 수익률 높은 순서대로 정리 
    year_profit = year_profit.sort_values(ascending=False) 

    # TOP 5 list 뽑기 
    top_profit = [ ['',0] for _ in range(5) ]
    cnt = len(year_profit.index)

    for i in range(5):
        if i >= cnt : break 
        top_profit[i] = [ str(year_profit.index[i]), int(year_profit[i]*100)]
    
    worst_profit = str(year_profit.index[-1])
    return top_profit, worst_profit




# 가장 수익률 높고 낮은 주식 찾기 
def stock_market_profit():  
    
    stock_code = fdr.StockListing('KRX') # 상장목록 전체 
    
    # 1. 내 잔고에서 주식 이름만 뽑아오기 
    my_stocks = [] 
    for name in stock_code['Name']:
        ticker = stock_code[stock_code['Name']==name]['Code'].to_string(index=False).strip()
        my_stocks.append([ticker,name])
    
    # 2. 1년간 데이터 가져와서 수익률 계산 
    df = pd.DataFrame()
    for ticker,name in my_stocks : 
        df[name] = fdr.DataReader(ticker,lastyear, day)['Close']
    
    day_profit = df.pct_change() # 일일 수익률 
    year_profit = day_profit.mean()*252 # 연간 수익률 
    # 수익률 높은 순서대로 정리 
    year_profit = year_profit.sort_values(ascending=False) 

    # 수익률 제일 높고 낮은거 뽑기 
    top_profit = str(year_profit.index[0])
    worst_profit = str(year_profit.index[-1])
    
    return top_profit, worst_profit
