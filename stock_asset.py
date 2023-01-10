# 내 자산 중에 가장 수익률 좋은 종목으로 포트폴리오 리밸런싱 

# now_account = [('stock', '삼성전자', 44000,8), ('stock', '카카오', 250000, 10), ('stock', 'KT', 100000, 9) ] 
# now_ratio = {'stock': [1689000, 3, 0], 'cash':[4000000,1,0]}
# total = 1000000
# best_stock = '삼성전자'
# worst_stock = '카카오'

import pandas as pd 
import FinanceDataReader as fdr 
from check_weekend import check_weekend

day = check_weekend()
day = day[0:4] + '-'+ day[5:7] + '-'+day[-2:]  
lastyear = str(int(day[0:4])-1) + '-'+ day[5:7] + '-'+ day[-2:]  


def rebal_asset(now_account, now_ratio, total, best_stock, worst_stock ): 
    
    for a in now_account:
        if a[1] == best_stock:
            best_stock_price = a[2]/a[3]
            best_stock_cnt = a[3]
            break 
    for a in now_account:
        if a[1] == worst_stock:
            worst_stock_price = a[2]/a[3]
            worst_stock_cnt = a[3]
            break 
    
    cash = now_ratio['cash'][0]
    rate = now_ratio['stock'][2]
    
    # 주식 비율이 높으면, 수익률 낮은 주식을 판다 
    # 판매한 금액은 현금이 된다  
    if rate >= 25 : 
        rebal_money = total * 0.01 * ( rate-25 )
        sell_cnt = rebal_money / worst_stock_price  # 판매할 주식 개수 
        
        if sell_cnt < worst_stock_cnt : 
            sell_sql = 'update account set cnt='+ str( worst_stock_cnt - sell_cnt )+ ' where name="'+ worst_stock +'"' 
        else : 
            sell_cnt = worst_stock_cnt 
            sell_sql = 'delete from account where name=' + worst_stock
        
        cash_sql = 'INSERT INTO account VALUES ("cash", "현금", '+ str(sell_cnt * worst_stock_price) + ")" 
        
        print(rebal_money, sell_cnt, sell_sql, cash_sql)
        return sell_sql, cash_sql 
        
    # 주식 비율이 낮으면, 수익률 높은 주식을 산다 
    else : 
        rebal_money = total * 0.01 * ( 25-rate )
        buy_cnt = rebal_money / best_stock_price  # 구매할 주식 개수 
        
        buy_sql = 'update account set cnt='+ str( best_stock_cnt + buy_cnt )+ ' where name="'+ best_stock+'"'
        
        if cash >= buy_cnt * best_stock_price : 
            cash_sql = 'update account set cnt='+ str( cash - buy_cnt * best_stock_price )+ ' where name="현금"' 
        else : 
            cash_sql = 'delete from account where name="현금"' 
    
        return buy_sql, cash_sql
        
        
               

# market 
def rebal_market(now_account, now_ratio, total, best_stock, worst_stock ): 
    
        
    best_ticker = stock_code[stock_code['Name']==best_stock]['Code'].to_string(index=False).strip()
    worst_ticker = stock_code[stock_code['Name']==worst_stock]['Code'].to_string(index=False).strip()
    
    best_price = fdr.DataReader(best_ticker,lastyear, day)['Close']
    worst_price = fdr.DataReader(worst_ticker,lastyear, day)['Close']
    
    cash = now_ratio['cash'][0]
    rate = now_ratio['stock'][2]
    
    # 주식 비율이 높으면, 수익률 낮은 주식을 판다 
    # 판매한 금액은 현금이 된다  
    if rate >= 25 : 
        rebal_money = total * 0.01 * ( rate-25 )
        sell_cnt = rebal_money / worst_stock_price  # 판매할 주식 개수 
        
        if sell_cnt < worst_stock_cnt : 
            sell_sql = 'update account set cnt='+ str( worst_stock_cnt - sell_cnt )+ ' where name="'+ worst_stock +'"' 
        else : 
            sell_cnt = worst_stock_cnt 
            sell_sql = 'delete from account where name=' + worst_stock
        
        cash_sql = 'INSERT INTO account VALUES ("cash", "현금", '+ str(sell_cnt * worst_stock_price) + ")" 
        
        # print(rebal_money, sell_cnt, sell_sql, cash_sql)
        return sell_sql, cash_sql 
        
    # 주식 비율이 낮으면, 수익률 높은 주식을 산다 
    else : 
        rebal_money = total * 0.01 * ( 25-rate )
        buy_cnt = rebal_money / best_stock_price  # 구매할 주식 개수 
        
        buy_sql = 'update account set cnt='+ str( best_stock_cnt + buy_cnt )+ ' where name="'+ best_stock+'"'
        
        if cash >= buy_cnt * best_stock_price : 
            cash_sql = 'update account set cnt='+ str( cash - buy_cnt * best_stock_price )+ ' where name="현금"' 
        else : 
            cash_sql = 'delete from account where name="현금"' 
    
        return buy_sql, cash_sql
    
        
    
# rebal_asset(now_account, now_ratio, total, best_stock, worst_stock )