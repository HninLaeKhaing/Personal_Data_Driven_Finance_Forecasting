import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.linear_model import LinearRegression

# uploaded file
file_path = '/content/personal_transactions.csv'
df = pd.read_csv(file_path)

#data cleaning
df.drop_duplicates()
df.head(10)
print(df)

# Preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = df['Amount'].astype(float)

# User input for category
category_to_analyze = input("Enter category to analyze (e.g., Mobile Phone): ")

# Filter and group by month
category_df = df[(df['Transaction Type'] == 'debit') & (df['Category'] == category_to_analyze)]
monthly_cat = category_df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
monthly_cat['Date'] = monthly_cat['Date'].astype(str)
monthly_cat['MonthIndex'] = np.arange(len(monthly_cat))

# Linear Regression Forecasting
X = monthly_cat[['MonthIndex']]
y = monthly_cat['Amount']
model = LinearRegression()
model.fit(X, y)

#  Forecast next 6 months
future_index = np.arange(len(monthly_cat), len(monthly_cat) + 6)
future_preds = model.predict(future_index.reshape(-1, 1))


# Forecast output
forecast_dates = pd.date_range(start=pd.to_datetime(monthly_cat['Date'].iloc[-1]) + pd.offsets.MonthBegin(1), periods=6, freq='MS')
forecast_df = pd.DataFrame({
    'Date': forecast_dates.strftime('%Y-%m'),
    'Forecasted Amount': future_preds
})


# 📊 Plotting
plt.figure(figsize=(10, 5))
plt.plot(monthly_cat['Date'], y, marker='o', label='Actual')
plt.plot(list(monthly_cat['Date']) + list(forecast_df['Date']),
         list(y) + list(forecast_df['Forecasted Amount']),
         marker='x', linestyle='--', color='orange', label='Forecasted')


plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('₹{x:,.0f}'))

plt.title(f'Monthly Expenses & Forecast: {category_to_analyze}')
plt.xlabel('Month')
plt.ylabel('Amount (in ₹)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

