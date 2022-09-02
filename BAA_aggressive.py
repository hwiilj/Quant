# origin : https://youtu.be/CclFfZVSx9k
# CAGR : 21.0% MDD : 14.6%
 
import requests
from bs4 import BeautifulSoup

data = []
index=0

def case_to_float(case):
    up = case.find('span', {'class':'relative-metric-bubble-data'}).text
    return float(up.split('%')[0])

def weigh(ticker):
    global index
    data.append([])
    print(ticker)
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    url = "https://www.barchart.com/etfs-funds/quotes/" + ticker + "/performance"
    reddit1Link = requests.get(url, headers=headers)
    soup =BeautifulSoup(reddit1Link.content,"html.parser")
    
    test = soup.find('main', {'id':'bc-main-content-wrapper'})
    test = test.find('div', {'class':'barchart-content-block symbol-price-performance'})
    test = test.find('div', {'class':'block-content'})
    performance = test.findAll('tr')

    
    for case in performance:
        #print(case)
        time = case.find('div', {'class':'period'})
        if time:
            time = time.get_text()
            if "1-Month" in time :
                t_index = 0
            elif "3-Month" in time:
                t_index = 1
            elif "6-Month" in time:
                t_index = 2
            elif "52-Week" in time:
                t_index = 3
            else:
                continue
            value = case.find('td', {'class':'cell-period-change'}).findAll('span')
            value = value[1].get_text()[1:-2]
            if value == 'unc' : value = 0
            data[index].append(float(value))            
            print(time + ":" + str(data[index][t_index]), end = ' ')

    data[index].append(data[index][0] * 12 + data[index][1] * 4 + data[index][2] * 2 + data[index][3])
    print(data[index][4])
    data[index].append(ticker)
    index = index + 1

#attack(4)
print("Attack")
weigh("QQQ")
weigh("VWO")
weigh("VEA")
weigh("BND")
#defence(7)
print("Defence")
weigh("BIL")
weigh("IEF")
weigh("TLT")
weigh("LQD")
weigh("TIP")
weigh("BND")
weigh("DBC")
#canaria
print("Canaria")
weigh("SPY")
weigh("VWO")
weigh("VEA")
weigh("BND")

if data[11][4] >=0 and data[12][4] >=0 and data[13][4]>=0 and data[14][4]>=0:
    y = sorted(data[0:4], key=lambda x:x[4], reverse=True)
    print("Attack!" + str(y[0][4]))
else:
    y = sorted(data[4:11], key=lambda x:x[3], reverse=True)
    print("Defence!")
    for i in range(3):
        print(str(y[i][5]) + " " + str(y[i][3]) + ('do not buy' if y[i][3]<0 else 'buy'))


#12개월 수익만
