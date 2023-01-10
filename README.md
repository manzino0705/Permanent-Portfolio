
## 💰 금융데이터를 활용한 금융 서비스 개발 

주제 : 영구 포트폴리오 관리용 Web Application 개발 

- **영구 포트폴리오** ( Permanent Portfolio )
서로 상관성이 낮은 자산군들( 주식, 채권, 현금, 금 ) 기반으로 자산을 배분함으로써, 꾸준히 수익률이 우상향하도록 하는 포트폴리오 전략. 
    
- 변동성이 큰 경제 상황 속에서, 많아진 자산과 적어진 자산을 파악하여 균형을 맞추는 **자산 리밸런싱 과정**이 반드시 필요함.
- 리밸런싱 할 때 마다, 여러 곳에 퍼져 있는 내 자산 현황을 빠르게 파악하고 매매하는 과정이 번거로움.
- 현재 나의 자산 배분 현황을 확인하고, 매매할 수 있는 기능을 **하나의 웹 페이지로 제공**함으로써, 포트폴리오 관리에 편의성을 주고자 함.



### 0. 개발 환경

- Python Web FrameWork : `Flask`
- DataBase : `MariaDB`
- Frontend : `BootStrap`
- Execute platform : `goormIDE`
- Data : `KRX` , `금융위원회`  



### 1. 메인 페이지

현재 자산 내역과 포트폴리오를 확인 하는 있는 페이지 

- **주요 기능**
    - 총 자산 값
    - 자산별 보유 금액
    - 자산별 차지 비율을 확인할 수 있는 **Pie Chart 형 포트폴리오**
    - 자산별 리밸런싱 필요한 비율    



### 2. 주식 수익률 확인 & 리밸런싱 페이지

보유 주식의 연간 수익률을 확인하고, 포트폴리오 리밸런싱을 진행하는 페이지 

- **주요 기능**
    - 보유 주식 연간 **수익률 TOP 5 Bar Chart**
    - 내 자산 기준으로 **자동 포트폴리오 리밸런싱** 기능
        - 주식 비율 ⬆︎ , 내가 가진 주식 중 가장 수익률 낮은 주식 매도
        - 주식 비율 ⬇︎ , 내가 가진 주식 중 가장 수익률 높은 주식 매수
    - 전체 시장 기준으로 자동 포트폴리오 리밸런싱 기능
    - 수동 포트폴리오 리밸런싱 페이지로 이동      



### 3. 자산 내역 확인 & 수동 리밸런싱 페이지

보유 자산 내역 및 오늘 시세를 확인하고, 수동으로 리밸런싱을 진행하는 페이지 

- **주요 기능**
    - 보유한 주식, 채권의 오늘 시세 확인
    - 자산/총 금액 별로 정렬 하거나, 보유하고 있는 종목 검색
    - 모든 자산 내역을 한눈에 확인
    - 수동으로 매수하고 싶은 자산 매수 가능     
