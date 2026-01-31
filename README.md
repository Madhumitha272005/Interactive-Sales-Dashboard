# Interactive-Sales-Dashboard
Project Overview

The Interactive Sales Dashboard is an intermediate-level data visualization project designed to analyze sales data and provide actionable business insights. It leverages Python, Pandas, Seaborn, and Plotly to generate both statistical and interactive visualizations. The dashboard highlights key metrics such as top-selling products, regional sales trends, and temporal sales patterns, helping organizations make informed business decisions.

Features

Statistical Visualizations:

Boxplots to analyze sales distribution by product

Violin plots to visualize sales distribution by region

Correlation heatmaps to identify relationships among numerical variables

Interactive Charts with Plotly:

Pie charts for product-wise sales contribution

Bar charts for regional sales comparison

Line charts for sales trends over time

Interactive Dashboard:

Combines multiple visualizations in a 2×2 layout

Users can explore sales data interactively with hover information

Provides a professional and cohesive presentation

Data Cleaning & Preprocessing:

Handles missing values and duplicates

Normalizes column names for consistency

Supports dynamic dataset analysis

Project Structure
Interactive_Sales_Dashboard/
│
├── dashboard.py                # Main Python script with all analysis and dashboard code
├── sales_data.csv              # Sample sales dataset
├── requirements.txt            # Python dependencies
├── visualizations/             # Folder containing saved charts (optional)
│   ├── boxplot_sales_product.png
│   ├── violin_sales_region.png
│   ├── correlation_heatmap.png
│   ├── pie_sales_product.html
│   ├── bar_sales_region.html
│   ├── line_sales_trend.html
│   └── interactive_dashboard.html
└── README.md                   # Project description and instructions

Installation & Setup

Install Python 3.x from the official website.

Install Visual Studio Code (VS Code) and add the Python extension.

Clone this repository and navigate to the project folder.

Install required libraries:

pip install pandas matplotlib seaborn plotly


Run the dashboard script:

python dashboard.py

Sample Output

Total Sales Distribution by Product: Boxplot showing spread and outliers

Total Sales Distribution by Region: Violin plot showing density and variation

Top Products by Sales: Interactive pie chart with hover values

Sales by Region: Interactive bar chart comparing regional performance

Sales Trend Over Time: Line chart showing temporal patterns

Interactive Dashboard: Combines all charts in a single 2×2 layout

Key Learnings

Advanced data manipulation with Pandas: cleaning, aggregation, and filtering

Statistical visualization with Seaborn

Interactive visualization with Plotly, including hover info and dynamic charts

Designing a professional dashboard layout for business presentations

Extracting business insights such as top-selling products, regional trends, and sales seasonality

Future Improvements

Add predictive analytics to forecast sales trends

Enable interactive filtering by product, region, or date

Integrate with live sales databases for real-time dashboards

Export dashboards to PDF or web formats for presentations
