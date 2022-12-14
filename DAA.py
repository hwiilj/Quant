# origin : https://youtu.be/2cNkblOxnFQ
# CAGR : 22%, MDD : 13%
 
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
            data[index].append(float(value))
            print(time + ":" + str(data[index][t_index]), end = ' ')

    data[index].append(data[index][0] * 12 + data[index][1] * 4 + data[index][2] * 2 + data[index][3])
    print(data[index][4])
    data[index].append(ticker)
    index = index + 1

weigh("BND")
weigh("VWO")
weigh("SPY")
weigh("IWM")
weigh("QQQ")
weigh("VGK")
weigh("EWJ")
weigh("VNQ")
weigh("GSG")
weigh("GLD")
weigh("TLT")
weigh("HYG")
weigh("LQD")
weigh("SHV")
weigh("IEF")
weigh("UST")

if data[0][4]>=0 and data[1][4]>=0 and 1:
    print("Go Attack")
else:
    print("Go Defence")
print("Attack Top 2")
for i in range(1,13):
    for j in range(i+1,13):
        if data[i][4] < data[j][4]:
            data[i], data[j] = data[j], data[i]
for i in range(1,13):
    for j in data[i]:
        print(j, end=' ')
    print()

print("Defence Top 1")
for i in range(13,16):
    for j in range(i+1, 16):
        if data[i][4] < data[j][4]:
            data[i], data[j] = data[j], data[i]
for i in range(13,16):
    for j in data[i]:
        print(j, end=' ')
    print()

