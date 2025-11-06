# Sales Data Analysis Project

## 📌 Project Overview

This project analyzes a **Detailed Sales Dataset** to perform data cleaning, filtering, calculations, and visualizations.
It demonstrates key **Data Science skills** such as handling missing values, removing outliers, aggregating data, calculating growth, and generating charts for insights.

---

## 🗂️ Dataset

**Files included:**

1. `sales_data_detailed.csv`

   * 1200 rows, multiple regions, products, and categories
   * Columns: `Date`, `Region`, `Product`, `Category`, `Units Sold`, `Discount`, `Revenue`, `Cost`, `Sales`
   * Includes **random null values** for `Discount`, `Units Sold`, and `Revenue` for practice
2. `cleaned_sales_stats.csv`

   * Same dataset after filling null values (no missing values)
   * Generated after data cleaning

---

## 🛠️ Python Script

**File:** `Sales_Data_Analysis.py`

The script performs the following tasks using this dataset:

1. **Data Cleaning**

   * Fill missing values in `Discount` and `Units Sold` with mode
   * Save cleaned dataset as `cleaned_sales_stats.csv`

2. **Data Exploration**

   * Count records by `Region`
   * Filter records by revenue threshold (50,000–150,000)
   * Remove discount outliers (>50%)

3. **Revenue Manipulation**

   * Increase all `Revenue` by 20%
   * Calculate average revenue per product

4. **Date-based Analysis**

   * Filter records by specific date ranges
   * Calculate **year-over-year sales growth** per product

5. **Region-based Analysis**

   * Filter records for specific regions (e.g., North)
   * Visualize total sales per region (bar chart)

6. **Profit & Sales Handling**

   * Calculate `Profit Margin = Revenue – Cost`
   * Replace negative `Sales` values with 0

7. **Top Products & Trends**

   * Visualize top 10 products by revenue
   * Plot monthly sales trends
   * Calculate total units sold per category

---

## 📊 Libraries Required

```bash
pip install pandas matplotlib
```

---

## 🚀 How to Run

1. Make sure `sales_data_detailed.csv` is in the same folder as the Python script.
2. Run the script:

```bash
python Sales_Data_Analysis.py
```

3. The script will:

   * Fill null values and save cleaned dataset as `cleaned_sales_stats.csv`
   * Print summaries, averages, and counts to console
   * Generate graphs for sales trends, top products, and region-wise revenue

---

## 🎯 Purpose / Learning Outcomes

* Learn **data cleaning** techniques with missing values
* Understand **grouping, aggregation, and filtering** in pandas
* Perform **time-series analysis** and **year-over-year growth**
* Create **visualizations** for business insights
* Practice handling **outliers and negative values**

---

## 📂 Project Structure

```
Sales_Data_Project/
│
├─ sales_data_detailed.csv
├─ cleaned_sales_stats.csv
├─ Sales_Data_Analysis.py
└─ README.md
```

---

## 📝 Notes

* The script is beginner-friendly and commented for easy understanding
* Null values and outliers are intentionally included for practice
* Can be extended with more advanced analysis like profit margin trends, correlation, or predictive modeling
