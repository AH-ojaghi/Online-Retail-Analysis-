# Import necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori, association_rules
import datetime as dt

# Load the dataset

url = "Online Retail.xlsx"
df = pd.read_excel(url, sheet_name='Online Retail')  # Load the dataset from the Excel file

# Initial data inspection

print(df.info())  # Check the structure of the dataset (columns, data types, non-null counts)
print(df.head())  # Display the first 5 rows of the dataset
print(df.isnull().sum())  # Check for missing values in each column

# Data Cleaning
# Remove rows where InvoiceNo is missing

df.dropna(subset=['InvoiceNo'], inplace=True)

# Convert InvoiceNo to string (in case it contains non-numeric characters)

df['InvoiceNo'] = df['InvoiceNo'].astype(str)

# Remove rows where InvoiceNo starts with 'C' (these are canceled orders)

df = df[~df['InvoiceNo'].str.startswith('C')]

# Convert InvoiceDate to datetime format

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Check the dataset after cleaning

print(df.info())
print(df.isnull().sum())

# Feature Engineering: Calculate TotalSales for each transaction

df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Exploratory Data Analysis (EDA)

# 1. Total Sales Analysis

total_sales = df['TotalSales'].sum()  # Calculate total sales
print(f"Total Sales: ${total_sales:.2f}")

# Monthly Sales Analysis

df['Month'] = df['InvoiceDate'].dt.to_period('M')  # Extract month from InvoiceDate
monthly_sales = df.groupby('Month')['TotalSales'].sum()  # Calculate monthly sales

# Plot Monthly Sales

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.show()

# 2. Customer Behavior Analysis
# Identify top customers by number of purchases

customer_purchase_count = df.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False)
top_customers = customer_purchase_count.head(10)  # Top 10 customers

# Plot Top Customers

plt.figure(figsize=(10, 6))
top_customers.plot(kind='bar', color='orange')
plt.title('Top 10 Customers by Number of Purchases')
plt.xlabel('Customer ID')
plt.ylabel('Number of Purchases')
plt.show()

# 3. Product Analysis
# Identify top-selling products by total sales

product_sales = df.groupby('Description')['TotalSales'].sum().sort_values(ascending=False)
top_products = product_sales.head(10)  # Top 10 products

# Plot Top Products

plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='green')
plt.title('Top 10 Products by Sales')
plt.xlabel('Product')
plt.ylabel('Sales ($)')
plt.show()

# 4. Geographic Analysis
# Analyze sales by country

country_sales = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)
top_countries = country_sales.head(10)  # Top 10 countries by sales

# Plot Sales by Country

plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar', color='purple')
plt.title('Top 10 Countries by Sales')
plt.xlabel('Country')
plt.ylabel('Sales ($)')
plt.show()

# Advanced Analysis

# 1. RFM Analysis (Recency, Frequency, Monetary)
# Set a reference date for recency calculation (e.g., one day after the last invoice date)

reference_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Calculate RFM metrics

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',  # Frequency
    'TotalSales': 'sum'  # Monetary
})

# Rename columns

rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalSales': 'Monetary'
}, inplace=True)

# Segment customers based on RFM scores
# Assign scores from 1 to 4 (4 is the best)
# Alternatively, use pd.cut if pd.qcut fails
rfm['RecencyScore'] = pd.cut(rfm['Recency'], bins=4, labels=[4, 3, 2, 1])
rfm['FrequencyScore'] = pd.cut(rfm['Frequency'], bins=4, labels=[1, 2, 3, 4])
rfm['MonetaryScore'] = pd.cut(rfm['Monetary'], bins=4, labels=[1, 2, 3, 4])

# Calculate RFM score

rfm['RFM_Score'] = rfm['RecencyScore'].astype(int) + rfm['FrequencyScore'].astype(int) + rfm['MonetaryScore'].astype(int)

# Segment customers based on RFM score

# rfm['Segment'] = pd.qcut(rfm['RFM_Score'], 3, labels=['Low', 'Medium', 'High'])
# 
# 
# 
rfm['Segment'] = pd.cut(rfm['RFM_Score'], bins=3, labels=['Low', 'Medium', 'High'])

# Plot RFM segments

plt.figure(figsize=(8, 6))
rfm['Segment'].value_counts().plot(kind='bar', color='teal')
plt.title('Customer Segmentation based on RFM')
plt.xlabel('Segment')
plt.ylabel('Number of Customers')
plt.show()

# 2. Market Basket Analysis
# Create a transaction matrix (each row represents a transaction, and each column represents a product)

transaction_matrix = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)

# Convert quantities to binary values (1 if purchased, 0 otherwise)

# transaction_matrix = transaction_matrix.applymap(lambda x: 1 if x > 0 else 0)
# 
# 
# 
transaction_matrix = transaction_matrix.map(lambda x: 1 if x > 0 else 0)

# Find frequent itemsets

# Convert quantities to boolean values (True if purchased, False otherwise)
transaction_matrix = transaction_matrix.map(lambda x: x > 0)

# Find frequent itemsets
frequent_itemsets = apriori(transaction_matrix, min_support=0.01, use_colnames=True)


# Generate association rules

rules = association_rules(frequent_itemsets, metric='lift', min_threshold=0.5)


# Plot the rules


# Check if rules are generated
if rules.empty:
    print("No rules were generated. Try reducing min_support or min_threshold.")
else:
    print(f"{len(rules)} rules were generated.")

    # Filter rules for better visualization
    filtered_rules = rules[(rules['support'] > 0.05) & (rules['confidence'] > 0.5)]

    # Plot the rules
    plt.figure(figsize=(10, 6))
    plt.scatter(filtered_rules['support'], filtered_rules['confidence'], alpha=0.5)
    plt.title('Association Rules: Support vs Confidence')
    plt.xlabel('Support')
    plt.ylabel('Confidence')
    plt.show()

# 3. Time-Based Analysis
# Extract hour and day of week from InvoiceDate

df['Hour'] = df['InvoiceDate'].dt.hour
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()

# Analyze sales by hour

hourly_sales = df.groupby('Hour')['TotalSales'].sum()

# Plot hourly sales

plt.figure(figsize=(10, 6))
hourly_sales.plot(kind='bar', color='orange')
plt.title('Sales by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Sales ($)')
plt.show()

# Analyze sales by day of week

day_of_week_sales = df.groupby('DayOfWeek')['TotalSales'].sum()

# Plot sales by day of week

plt.figure(figsize=(10, 6))
day_of_week_sales.plot(kind='bar', color='purple')
plt.title('Sales by Day of the Week')
plt.xlabel('Day of Week')
plt.ylabel('Sales ($)')
plt.show()

# 4. Loyal Customers Analysis
# Identify loyal customers (e.g., top 10% of customers by frequency and monetary value)

loyal_customers = rfm[rfm['Segment'] == 'High']

# Analyze the purchasing behavior of loyal customers

loyal_customer_data = df[df['CustomerID'].isin(loyal_customers.index)]

# Top products bought by loyal customers

loyal_top_products = loyal_customer_data.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(10)

# Plot top products bought by loyal customers

plt.figure(figsize=(10, 6))
loyal_top_products.plot(kind='bar', color='blue')
plt.title('Top Products Bought by Loyal Customers')
plt.xlabel('Product')
plt.ylabel('Sales ($)')
plt.show()

# Key Insights

print("Key Insights:")
print(f"1. Total Sales: ${total_sales:.2f}")
print(f"2. Month with Highest Sales: {monthly_sales.idxmax()} with ${monthly_sales.max():.2f}")
print(f"3. Top Customer: {top_customers.idxmax()} with {top_customers.max()} purchases")
print(f"4. Top Product: {top_products.idxmax()} with ${top_products.max():.2f} in sales")
print(f"5. Top Country: {top_countries.idxmax()} with ${top_countries.max():.2f} in sales")
print(f"6. Number of Loyal Customers: {len(loyal_customers)}")