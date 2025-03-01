import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

# List of CSV files
arr = ["IBM.csv", "SHOP.TRT.csv", "TSCO.LON.csv"]

for file in arr:
    try:
        df = pd.read_csv(file)

        if 'date' in df.columns and 'high' in df.columns:
            df_binary = df[['date', 'high']].copy()  # Create a copy to avoid modifying the original

            df_binary.dropna(inplace=True)  # Remove missing values
            
            if df_binary.empty:
                print(f"Skipping {file} (no valid data).")
                continue  # Skip this file if no data left

            # Convert date column to UNIX timestamp properly
            df_binary['date'] = pd.to_datetime(df_binary['date']).astype('int64') // 10**9  

            print(f"First 5 rows of {file}:")
            print(df_binary.head())

            X = np.array(df_binary['date']).reshape(-1, 1)
            y = np.array(df_binary['high']).reshape(-1, 1)

            # Splitting the data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

            # Training the model
            regr = LinearRegression()
            regr.fit(X_train, y_train)

            # Printing the R² score
            print(f"R² Score for {file}: {regr.score(X_test, y_test)}\n")

            # User input for prediction
            user_date = input(f"Enter a date (YYYY-MM-DD) to predict stock price for {file}: ")
            try:
                user_timestamp = pd.to_datetime(user_date).timestamp()  # Convert input date to timestamp
                predicted_price = regr.predict(np.array([[user_timestamp]]))
                print(f"Predicted stock price for {file} on {user_date}: {predicted_price[0][0]:.2f}\n")
            except Exception as e:
                print(f"Invalid date input: {e}")

    except FileNotFoundError:
        print(f"Error: {file} not found.")
    except Exception as e:
        print(f"An error occurred with {file}: {e}")
