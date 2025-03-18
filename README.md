# Online Retail Data Analysis Project

![Online Retail](https://www.retailgazette.co.uk/wp-content/uploads/2021/01/Online-shopping_online-sales_online-retail_ecommerce_ST.jpg)


## Overview
This project focuses on analyzing the **Online Retail Dataset** to uncover insights into customer behavior, sales trends, and product performance. The analysis includes **Exploratory Data Analysis (EDA)**, **RFM Analysis**, **Market Basket Analysis**, and **Time-Based Analysis**. The goal is to provide actionable insights for improving sales strategies and customer engagement.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Features](#features)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Overview

This project analyzes the **Online Retail Dataset**, which contains transaction data for an online retail store. The dataset includes information such as:
- Invoice numbers
- Stock codes
- Product descriptions
- Quantities
- Invoice dates
- Unit prices
- Customer IDs
- Countries

The analysis is divided into the following sections:
1. **Exploratory Data Analysis (EDA):** Understanding the dataset, cleaning data, and visualizing key trends.
2. **RFM Analysis:** Segmenting customers based on Recency, Frequency, and Monetary value.
3. **Market Basket Analysis:** Identifying frequently purchased product combinations.
4. **Time-Based Analysis:** Analyzing sales trends over time (hourly, daily, monthly).

---

## Dataset

The dataset used in this project is the **Online Retail Dataset**, available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/static/public/352/online+retail.zip). It contains transaction data from December 2010 to December 2011 for a UK-based online retail store.

### Dataset Columns
- **InvoiceNo:** Invoice number (unique identifier for each transaction).
- **StockCode:** Product code (unique identifier for each product).
- **Description:** Product description.
- **Quantity:** Quantity of each product in the transaction.
- **InvoiceDate:** Date and time of the transaction.
- **UnitPrice:** Price of each product.
- **CustomerID:** Unique identifier for each customer.
- **Country:** Country where the transaction occurred.

---

## Features

### 1. **Exploratory Data Analysis (EDA)**
- Data cleaning and preprocessing.
- Visualization of sales trends, top products, and top customers.
- Geographic analysis of sales by country.

### 2. **RFM Analysis**
- Customer segmentation based on:
  - **Recency:** How recently a customer made a purchase.
  - **Frequency:** How often a customer makes a purchase.
  - **Monetary:** How much money a customer spends.
- Visualization of customer segments.

### 3. **Market Basket Analysis**
- Identification of frequently purchased product combinations using the **Apriori algorithm**.
- Generation of association rules to understand product relationships.

### 4. **Time-Based Analysis**
- Analysis of sales trends by hour, day of the week, and month.
- Visualization of peak sales periods.

---

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/online-retail-analysis.git
   cd online-retail-analysis
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset:**
   - Download the dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/static/public/352/online+retail.zip).
   - Place the `Online Retail.xlsx` file in the project directory.

---

## Usage

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Online_Retail_Analysis.ipynb
   ```

2. Run the notebook cells step by step to:
   - Perform data cleaning and preprocessing.
   - Conduct exploratory data analysis (EDA).
   - Perform RFM analysis and customer segmentation.
   - Conduct market basket analysis.
   - Analyze sales trends over time.

---

## Results

### Key Insights
1. **Total Sales:** The total sales for the period were $X.
2. **Top Products:** The top-selling products were [Product A, Product B, Product C].
3. **Top Customers:** The most frequent customers were [Customer X, Customer Y, Customer Z].
4. **Peak Sales Periods:** Sales peaked during [specific hours/days/months].

### Visualizations
- **Monthly Sales Trends:** A bar chart showing sales trends over time.
- **Customer Segmentation:** A bar chart showing the distribution of customer segments (Low, Medium, High).
- **Market Basket Analysis:** A scatter plot showing association rules (Support vs. Confidence).

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Dataset provided by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/static/public/352/online+retail.zip).
- Libraries used: `pandas`, `numpy`, `matplotlib`, `seaborn`, `mlxtend`.

---

## ✍️ Author  
**Amirhossein Ojaghi**  
🔗 [GitHub](https://github.com/AH-ojaghi/911-Calls-Capstone)

