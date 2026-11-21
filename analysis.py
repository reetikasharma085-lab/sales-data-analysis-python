# Sales Data Analysis using Python
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('sales.csv')

# 1. Data Cleaning
df = df.drop_duplicates()
df = df.dropna()

# 2. City-wise Sales Analysis
city_sales = df.groupby('City')['Amount'].sum()
print(city_sales)

# 3. Product-wise Sales Analysis
product_sales = df.groupby('Product')['Amount'].sum()
print(product_sales)

# 4. Month-wise Sales Analysis
month_sales = df.groupby('Month')['Amount'].sum()
print(month_sales)

# 5. Visualization
product_sales.plot(kind='bar')
plt.title('Product-wise Sales')
plt.show()
