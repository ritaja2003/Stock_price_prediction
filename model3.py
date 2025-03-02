import numpy as np 
import pandas as pd 
import sys
import json
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

arr = ["IBM.csv", "SHOP.TRT.csv", "TSCO.LON.csv"]

if len(sys.argv) < 2:
    print(json.dumps({"error": "No date provided"}))
    sys.exit(1)

user_date = sys.argv[1]

predictions = []

for file in arr:
    try:
        df = pd.read_csv(file)

        if 'date' in df.columns and 'high' in df.columns:
            df['date'] = pd.to_datetime(df['date']).astype('int64') // 10**9  

            X = df[['date']].values
            y = df[['high']].values

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

            regr = LinearRegression()
            regr.fit(X_train, y_train)

            r2_score = regr.score(X_test, y_test)

            user_timestamp = pd.to_datetime(user_date).timestamp()
            predicted_price = regr.predict([[user_timestamp]])[0][0]
            predictions.append({
                "stock": file,
                "predicted_price": round(predicted_price, 2),
                "accuracy": round(r2_score, 4)
            })

    except Exception as e:
        continue

print(json.dumps(predictions))


