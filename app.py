import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Transaction Forecast", layout="wide")
st.title("📈 Personal Expense Forecasting App")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    try:
        # Data cleaning & preprocessing
        df.drop_duplicates(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Amount'] = df['Amount'].astype(float)

        # User selects category
        categories = df['Category'].unique()
        category_to_analyze = st.selectbox("Select a category to analyze", categories)

        # Filter and group
        category_df = df[(df['Transaction Type'] == 'debit') & (df['Category'] == category_to_analyze)]
        if category_df.empty:
            st.warning(f"No debit transactions found for category: {category_to_analyze}")
        else:
            monthly_cat = category_df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
            monthly_cat['Date'] = monthly_cat['Date'].astype(str)
            monthly_cat['MonthIndex'] = np.arange(len(monthly_cat))

            # Linear Regression
            X = monthly_cat[['MonthIndex']]
            y = monthly_cat['Amount']
            model = LinearRegression()
            model.fit(X, y)

            # Forecasting
            future_index = np.arange(len(monthly_cat), len(monthly_cat) + 6)
            future_preds = model.predict(future_index.reshape(-1, 1))
            forecast_dates = pd.date_range(start=pd.to_datetime(monthly_cat['Date'].iloc[-1]) + pd.offsets.MonthBegin(1), periods=6, freq='MS')
            forecast_df = pd.DataFrame({
                'Date': forecast_dates.strftime('%Y-%m'),
                'Forecasted Amount': future_preds
            })

            # Plotting
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(monthly_cat['Date'], y, marker='o', label='Actual')
            ax.plot(list(monthly_cat['Date']) + list(forecast_df['Date']),
                    list(y) + list(forecast_df['Forecasted Amount']),
                    marker='x', linestyle='--', color='orange', label='Forecasted')
            ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('₹{x:,.0f}'))
            plt.title(f'Monthly Expenses & Forecast: {category_to_analyze}')
            plt.xlabel('Month')
            plt.ylabel('Amount (in ₹)')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            st.pyplot(fig)

            # Show forecast table
            st.subheader("📅 Forecasted Amounts for Next 6 Months")
            st.dataframe(forecast_df.set_index('Date'))

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a CSV file to begin.")
