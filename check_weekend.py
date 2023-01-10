from pytz import timezone
from datetime import date, timedelta

# 주말에는 데이터가 없으므로, 오늘이 주말인지 판단해서, 
# 주말이면 금요일 날짜를 return 하는 코드 작성 

def check_weekend():
    day = date.today()+ timedelta(hours=8)
    weekday = day.weekday()  # 토요일이면 5, 일요일이면 6 
    if weekday > 4 : 
        day = day - timedelta(weekday-4)    
    
    return str(day) 

