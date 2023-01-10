# DB에서 내 자산 목록 가져온 다음에 금액이랑 합쳐서 return  
from bond_data import bondData
from pykrx_data import pykrxData

bond_data = bondData()
pykrx_data = pykrxData()

my_account=[]

# 내 주식 현재 가격 조회해서 list 화 해주기 
def get_now_account(account_data):
    
    # type, name, count 순서 
    my_account = [] 
    
    for type, name, cnt in account_data: 
        if type == 'stock' : # 주식이면, 
            my_account.append([type, name, int(pykrx_data[(pykrx_data.종목명 == name)]['종가'].tolist()[0]) * cnt ,cnt])
            # print(int(pykrx_data[(pykrx_data.종목명 == name)]['종가'].tolist()[0]))
        elif type == 'bond' : # 채권이면, 
            print(name)
            my_account.append([type, name, int(bond_data[(bond_data.itmsNM == name)]['mkpPrc'].tolist()[0]) * cnt ,cnt])
        else : 
            my_account.append([type,name,cnt,1])
    
    return my_account # my_account ['stock', '삼성전자', 444000, 8] 


def get_now_ratio(my_account): 
      
    # 비율 구하기    
    total_account = 0 
    # now_rate = [0,0,0,0,0]  # stock, bond, cash, gold, 총합 순서로 rate 구하기 
    # now_rate : {'stock': [1689000, 3, 0]  # 총합, 갯수, 비율 
    now_rate = {'stock':[0,0,0],'bond':[0,0,0],'cash':[0,0,0],'gold':[0,0,0]}  # 총합, 갯수, 비율 

    for a in my_account :   
        now_rate[a[0]][0] += a[2]
        now_rate[a[0]][1] += 1 # 주식 종류 
        total_account += a[2]

    for i in ['stock','bond','cash', 'gold']:
        if now_rate[i][1] == 0 : continue 
        # print( now_rate[i][0] / total_account ) 
        now_rate[i][2] = int( (now_rate[i][0] / total_account ) * 100 )
    
    return now_rate, total_account

