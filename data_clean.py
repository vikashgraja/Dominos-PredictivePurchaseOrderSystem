import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns


sales_data = pd.read_excel('dataset/master/Pizza_Sale.xlsx')
ingredients_data = pd.read_excel('dataset/master/Pizza_ingredients.xlsx')

sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Check for missing values
print("Missing Values:\n", sales_data.isnull().sum())
sales_data.fillna(0, inplace=True)  # Simple imputation for missing values

# Remove outliers in sales quantity (optional)
q1 = sales_data['Quantity Sold'].quantile(0.25)
q3 = sales_data['Quantity Sold'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
sales_data = sales_data[(sales_data['Quantity Sold'] >= lower_bound) & 
                        (sales_data['Quantity Sold'] <= upper_bound)]

print("Cleaned Sales Data:\n", sales_data.head())

sales_data.to_excel('dataset/process/Pizza_Sale.xlsx',index=False)
ingredients_data.to_excel('dataset/process/Pizza_ingredients.xlsx',index=False)