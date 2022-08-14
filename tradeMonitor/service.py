import requests
def getData(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey=B2FRN5Z7M2R83QIU'
    r = requests.get(url)
    data = r.json()
    date=[i for i in data["Monthly Time Series"].keys()]
    openPrice=[]
    high=[]
    low=[]
    close=[]
    volume=[]
    for j in date:
        openPrice.append(data["Monthly Time Series"][j]["1. open"])
        high.append(data["Monthly Time Series"][j]["2. high"])
        low.append(data["Monthly Time Series"][j]["3. low"])
        close.append(data["Monthly Time Series"][j]["4. close"])
        volume.append(data["Monthly Time Series"][j]["5. volume"])

    data={"stockName":symbol,"date":date,"openPrice":openPrice,"high":high,"low":low,"close":close,"volume":volume}
    return(data)