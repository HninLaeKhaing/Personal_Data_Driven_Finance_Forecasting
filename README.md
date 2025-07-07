# 📊 Personal Data-Driven Financial Forecasting

This project uses Python and linear regression to analyze personal transaction data and **forecast future spending**. It aims to help individuals understand their expense patterns and make informed financial decisions.

## 📌 Project Overview

In the digital age, financial data is plentiful—but insights are rare. This project transforms raw transaction records into actionable forecasts using data analysis and machine learning. Users can input a specific **category** (e.g., Mobile Phone, Rent) and view a graph of **monthly trends** and a **6-month forecast**.

## 🧠 Key Features

- Cleans and processes transaction data
- Allows **user-specified category** analysis
- Groups expenses monthly
- Forecasts **next 6 months** of spending using **linear regression**
- Visualizes trends and predictions with clear matplotlib graphs

## 🗃️ Dataset

- **Source:** Kaggle – Personal Transactions Dataset  
- **Period Covered:** January 2018 to September 2019  
- **Fields:**
  - `Date`
  - `Amount`
  - `Transaction Type` (debit/credit)
  - `Category` (e.g., Rent, Groceries, Travel, etc.)

## 🛠️ Technologies Used

- **Python 3**
- `pandas` – data handling
- `numpy` – numerical operations
- `matplotlib` – data visualization
- `scikit-learn` – linear regression modeling

## 📈 Sample Output

The project produces a plot like this:

```
Actual vs Forecasted Monthly Spending (₹) in [chosen category]
```

*(Graph will show a solid line for actuals and a dashed line for future predictions.)*

## ⚙️ How to Use

1. Upload or link your CSV file (ensure it has `Date`, `Amount`, `Transaction Type`, `Category`).
2. Run the script.
3. Enter a category when prompted (e.g., "Grocery").
4. View forecasted output in the generated plot.

## 📦 Installation

```bash
pip install pandas numpy matplotlib scikit-learn
```

## 📂 File Structure

```
├── personal_transactions.csv     # Sample transaction data
├── forecast_script.py            # Main script file
├── README.md                     # Project overview
└── .gitignore                    # Files to ignore in Git
```

## 🔍 Results & Insights

- Rent and subscriptions had consistent monthly patterns.
- Holiday spending spikes were observed in December.
- Linear regression worked well for regular categories but struggled with erratic ones.

## 🚀 Future Improvements

- Use **ARIMA or LSTM** for more accurate time-series forecasting.
- Add **user interface** for non-technical users.
- Incorporate **multiple features** like income, location, etc.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👩‍💻 Author

- **Hnin Lae Khaing**
- B.Tech CSE, Manav Rachna University  
