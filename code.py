import requests
import csv

symbol=['IBM','TSCO.LON','SHOP.TRT' ]

for stock in symbol:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey=56GAE6TZBH33TQN4'
    r = requests.get(url)
    data = r.json()

    print(data)

    csv_header = ["date", "open", "high", "low", "close", "volume"]

    time_series= data.get("Time Series (Daily)",{})

    with open(f'{stock}.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(csv_header)
        for date, values in time_series.items():
            writer.writerow([
                date,
                values["1. open"],
                values["2. high"],
                values["3. low"],
                values["4. close"],
                values["5. volume"]

        ] )
            

        
print("Data successfully written ") # type: ignore

arr = ["IBM.csv", "SHOP.TRT.csv", "TSCO.LON.csv"]

for filename in arr:
    try:
        with open(filename, mode='r') as file:
            csvFile = csv.reader(file)
            print(f"Contents of {filename}:")
            for lines in csvFile:
                print(lines[0], lines[2])
                
            print("-" * 50)  # Separator for readability
    except FileNotFoundError:
        print(f"Error: {filename} not found.")




