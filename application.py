# 필요 라이브러리 import 
import sys
import pymysql
from pytz import timezone
from datetime import date, timedelta
from flask import Flask, session, render_template, redirect, request, url_for 
from flaskext.mysql import MySQL

# 필요 함수 import 
from myAccount import get_now_account, get_now_ratio 
from check_weekend import check_weekend
from stock_chart import stock_profit , stock_market_profit 
from stock_asset import rebal_asset , rebal_market

# flask, db 생성 
application=Flask(__name__)
db = MySQL() 

# DB 연동
application.config['MYSQL_DATABASE_USER'] = 'root'
application.config['MYSQL_DATABASE_PASSWORD'] = 'password'
application.config['MYSQL_DATABASE_DB'] = 'fin'
application.config['MYSQL_DATABASE_HOST'] = 'localhost'
application.secret_key = "ABCDEFG"
db.init_app(application)

conn = db.connect()
cursor = conn.cursor() 
# cursor.close()
# conn.close()


# 현재 잔고 내역 불러오기
def now_account_data() :    
    sql = 'select * from account'
    value = [] 
    cursor.execute(sql, value) 
    # cursor.execute("set names utf8")

    account_data = list(cursor.fetchall()) 
    now_account = get_now_account(account_data)
    
    return now_account


# 총 자산 내역, 조정 필요한 비율, 현재 내 포트폴리오 차트 보여주는 페이지 
@application.route('/')
def main(): 
    now_account = now_account_data()
    
    # 영구 포트폴리오 비율 
    static_ratio = {'stock':25,'bond':25,'gold':25,'cash':25} 
    now_ratio, total = get_now_ratio(now_account)

    # 내 포트폴리오 조정 필요한 비율 계산 
    cal_ratio={} 
    for i in ['stock','bond','gold','cash']:  
        cal_ratio[i]=static_ratio[i]-now_ratio[i][2] 
        
    return render_template("index.html", account=now_ratio, cal_ratio=cal_ratio, total=total)


# 수익률 확인 초기 화면 
@application.route('/stocks')
def stockchart():
    day = check_weekend()
    now_account= now_account_data()
    stock_profits, worst_profit = stock_profit(now_account)
    
    return render_template("stock_chart.html", day=day, profit=stock_profits)


# 내 자산으로 비율 조절 
@application.route('/stocks-asset')
def stockchart_asset():
    day = check_weekend()
    now_account= now_account_data() 
    now_ratio, total = get_now_ratio(now_account)
    stock_profits, worst_profit = stock_profit(now_account)
    
    best_stock = stock_profit(now_account)[0][0][0]
    worst_stock = worst_profit
    sql1, sql2 = rebal_asset(now_account, now_ratio, total, best_stock, worst_stock )
    
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
    
    return render_template("stock_chart.html", day=day, profit=stock_profits)


# 시장에서 수익률 가장 높은/낮은 주식으로 비율 조절  
@application.route('/stocks-market')
def stockchart_market():
    day = check_weekend()
    now_account= now_account_data()
    now_ratio, total = get_now_ratio(now_account)
    stock_profits, worst_profit = stock_profit(now_account)
    
    best_stock, worst_stock= stock_market_profit()
    
    sql1, sql2 = rebal_market(now_account, now_ratio, total, best_stock, worst_stock )
     
    return render_template("stock_chart.html", day=day, profit=stock_profits)
    

@application.route('/tables', methods=['GET','POST']) # 현재 자산 내역 표시 
def table(): 
        
    day = check_weekend()    

    # 값 입력 받으면 여기로 
    if request.method == 'POST' : 
        newType = request.form['newType']
        newName = request.form['newName']
        newCnt = request.form['newCnt']
        
        # 현재 잔고 내역 추가하기    
        # insert into account values ('gold', '금',1);  # type, name, cnt 순서 
        sql = 'insert into account values ("'+newType+'","'+ newName+'",'+newCnt+')'
        cursor.execute(sql)
        conn.commit()
        
    # 값 입력 없으면 여기부터 실행 
    now_account = now_account_data()

    return render_template("table.html", now=day, account=now_account)
    
if __name__ == '__main__':
    application.run(host='0.0.0.0') 