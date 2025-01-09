import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import matplotlib
import pandas as pd
#import pendulum
import os
#os.system('cls')
#ticker_list = ["TNXP", "PRTG", "OPTX", "NUKK", "KWE", "NWTNW"]
ticker_list = ["RELI","TRAW","PIK","PHIO"]
#ticker_list = ["PALI", "LOOP", "JUNS"]
all_symbols  = " ".join(ticker_list)
tickers = yf.Tickers(all_symbols)
for ticker in ticker_list:
    #institucion = (tickers.tickers[ticker].info['heldPercentInstitutions'])
    #print("All infos :",tickers.tickers[ticker].info)
    #print("institucion test  :",tickers.tickers[ticker].info['heldPercentInstitutions']*100)
    #try:
    #    (institucion == tickers.tickers[ticker].info['heldPercentInstitutions'])
    #except NameError:
    #    institucion = '? no Data ?'
    #    print("int false:") #,institucion)    
    
    #else:
     #   institucion = tickers.tickers[ticker].info['heldPercentInstitutions']
      #  print("int verdadero:",institucion)

    #"heldPercentInsiders": 0.00066,
    #PercentInsiders = tickers.tickers[ticker].info['heldPercentInsiders']
    name = tickers.tickers[ticker].info['symbol']
    openprice = tickers.tickers[ticker].info['regularMarketOpen']
    currentprice = tickers.tickers[ticker].info["currentPrice"]
    float = tickers.tickers[ticker].info['floatShares']
    volume = tickers.tickers[ticker].info['volume']
    regvolume = tickers.tickers[ticker].info['regularMarketVolume']
    averageVolume = tickers.tickers[ticker].info['averageVolume']
    averageVolume10days = tickers.tickers[ticker].info['averageVolume10days']
    averageDailyVolume10Day = tickers.tickers[ticker].info['averageDailyVolume10Day']
    #institucion = institucion * 100
    float = float / 1000000
    volume = volume / 1000000
    averageVolume = averageVolume / 1000000
    averageVolume10days = averageVolume10days / 1000000
    playprice = 0
    playinst = 0
    playfloat = 0
    market_cap = tickers.tickers[ticker].info["marketCap"]
    operatingCashflow = tickers.tickers[ticker].info['operatingCashflow']
    fullTimeEmployees = tickers.tickers[ticker].info['fullTimeEmployees']
    closeprice = tickers.tickers[ticker].info['previousClose']
    gup = ((openprice-closeprice)/closeprice)
    gupcloseyest =  ((currentprice*100)/closeprice)
    dayHigh = tickers.tickers[ticker].info['dayHigh']
    dayLow =  tickers.tickers[ticker].info['dayLow']

    enterpriseToEbitda = tickers.tickers[ticker].info['enterpriseToEbitda']
    ebitda = tickers.tickers[ticker].info['ebitda']
    totalDebt = tickers.tickers[ticker].info['totalDebt']
    quickRatio = tickers.tickers[ticker].info['quickRatio']
    currentRatio =tickers.tickers[ticker].info['currentRatio']
    debtToEquity = tickers.tickers[ticker].info['debtToEquity']
    returnOnAssets = tickers.tickers[ticker].info['returnOnAssets']
    returnOnEquity = tickers.tickers[ticker].info['returnOnEquity']
    freeCashflow = tickers.tickers[ticker].info['freeCashflow']
  
    print('^-'*30)
    print("\nTICKER                               : ",name)
    print("OPEN Price                           : ",openprice,"$  -> GUP% : ", f'{gup:,.2f}'"%")
    print("Close price                          : ", f'{closeprice:,.2f}',"$ -> GUP% : ", f'{gupcloseyest:,.2f}'"%")
    print("Float 2@50 M                         : ",f'{float:,.2f}'"M")
    print("Last Price                           : ",currentprice,"$")
    print("Volumen (M)                          : ",f'{volume:,.2f}'"M")
    print("Volumen moyen (M)                    : ",f'{averageVolume:,.2f}'"%")
    print("Volumen moyen Diario 10Jours (M)     : ",f'{averageVolume10days:,.2f}'"%")
    print("Market CAP (M)                       : ",f'{market_cap:,.2f}'"$M")
    print("Operation CashFlow (M)               : ",f'{operatingCashflow:,.2f}'"$M")
    print("Nro Total Employees                  : ",f'{fullTimeEmployees:,.0f}')
    print("% Institution %                      : ",f'{(tickers.tickers[ticker].info['heldPercentInstitutions']*100):.2f}'"%")
    #print("% Insider %                          : ",f'{(PercentInsiders*100):.2f}'"%")
    #print("% Institucion %                      : ",f'{institucion:.2f}')

    print("High Day Price                       : ",f'{dayHigh:,.2f}'"$ -> %PUSH-UP%", f'{((dayHigh-openprice)/openprice)*100:,.2f}',"%")
    print("Low Day Price                        : ",f'{dayLow:,.2f}'"$ -> %PUSH-DOWN%", f'{((dayLow-openprice)/openprice)*100:,.2f}',"%")

    #print("High Day Price                       : ",f'{dayHigh:,.2f}'"$ -> %PUSH-UP%", f'{((dayHigh*100)/openprice):,.2f}',"%")
    #print("Low Day Price                        : ",f'{dayLow:,.2f}'"$ -> %PUSH-DOWN%", f'{((dayLow*100)/openprice):,.2f}',"%")
    print('------ Aditional Info : ------')
    print("enterpriseToEbitda (M)               : ",f'{enterpriseToEbitda:,.2f}'"$M")
    print("Ebitda (M)                           :",f'{ebitda:,.2f}'"$M")
    print("Total Debt (M)                       : ",f'{totalDebt:,.2f}'"$M")
    print("Quick Ratio (M)                      : ",f'{quickRatio:,.2f}'"$M")
    print("Current Ratio (M)                    : ",f'{currentRatio:,.2f}'"$M")
    print("Total Debt/Equity (mrq)              : ",f'{debtToEquity:,.2f}'"$M")
    print("Return on Assets (ttm) (M)           : ",f'{returnOnAssets:,.2f}'"$M")
    print("Return on Equity (ttm) (M)           : ",f'{returnOnEquity:,.2f}'"$M")
    print("Levered Free Cash Flow (ttm) (M)     : ",f'{freeCashflow:,.2f}'"$M")



    #actions = ticker.get_actions()
    #cf = tickers.tickers[ticker].get_cashflow()
    #info = tickers.tickers[ticker].get_info()
    #inst_holders = ticker.get_institutional_holders()
    #print("CASH FLOW                             :\n ",cf)
    print('\nAnalisis Metodo - GUP : \n')
    if openprice < 10:
        print(openprice,"Prix OK")
        playprice = 0        
    else:
        print(openprice,"Prix trop haut")
        playprice = 1

    #if (tickers.tickers[ticker].info['heldPercentInstitutions']*100) > 20:
    #    print(f'{institucion:.2f}', "% Institucion High >20% ")
    #    playinst = 1
    #else:
    #    print(f'{(tickers.tickers[ticker].info['heldPercentInstitutions']*100):.2f}', "% Institucion <20% OK")
    #    playinst = 0
    
    if 2 <= float and float <= 50:
        print(f'{float:,.2f}', "Float entre 2@50M : OK")
        playfloat = 0
    else:
        print(f'{float:,.2f}', " Float trop petit ou Trop Haut")
        playfloat = 1

    if playfloat == 0 and playprice == 0 and playinst == 0:
        print('PLAY A?')
        ini_price = (openprice * 0.05)+openprice
        close_price = (openprice * 0.40)+openprice
        print('Prix Entrer 5% du Open price :',f'{ini_price:,.2f}')
        print('Prix Sorti 40% :', f'{close_price:,.2f}')
    else:
        print('PLAY B/C')
    print('\n')
    


    #ticker = yf.Ticker("CPIX")
    
    #institucion = tickers.tickers[ticker].info['heldPercentInstitutions']
    
    #institucion = tickers.tickers[ticker].info['heldPercentInstitutions']
    #print("test wh :",institucion)


    #pd.options.display.max_rows=10  # To decrease printouts
    #start = pendulum.parse('2024-12-08 09:30').add(hours=7)  # My tz is UTC+03:00, original TZ UTC-04:00. So adds to my local time 7 hours
    #end = pendulum.parse('2024-12-09 10:30').add(hours=7)  # Same
    #print(start)
    # print(yf.download(tickers=name, interval="1m", start=start, end=end))
    


  #  from datetime import datetime, timedelta

    #yesterday = datetime.now() - timedelta(days=1)
    #yesterday.strftime('%m%d%y')
   # gold = yf.download(tickers="GC=F", period="5d", interval="1m")
   # filtered = gold[yesterday: datetime.now()]



    #print("Info :",info)
    #print('*'*20)
    #print("Institution Holders      : ",inst_holders)




    #from datetime import datetime, timedelta
    
    #ticker_symbol = 'CPIX'

    #data = yf.download(ticker, start='2024-12-11', end='2024-12-12')
    #print('Historico : \n',data)
    #print(yf.download('ISF.L ECAR.L', start='2024-12-09', end='2024-12-09', interval='1d', auto_adjust=True, group_by='ticker'))
    #print(yf.download('ECAR.L ISF.L', start='2021-03-01', end='2021-03-12', interval='1d', auto_adjust=True, group_by='ticker'))
    
    # worked for several years
    #yf.download('^SPX', period='30d', interval='1h', ignore_tz = True, progress=False)
    # leads to: ...Period '30d' is invalid, must be one of ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']") 
    # newly forced to use start-end instead
    # yf.download('^SPX', start = X, interval='1h', ignore_tz = True, progress=False)

#https://www.alphavantage.co/
#https://www.matecdev.com/posts/python-packages-yahoo-finance.html
#https://theautomatic.net/yahoo_fin-documentation/
#https://theautomatic.net/2018/07/31/how-to-get-live-stock-prices-with-python/