# dashboard.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -----------------------------
# Step 1: Load and inspect data
# -----------------------------
df = pd.read_csv("sales_data.csv")  # Replace with your dataset path
df.columns = df.columns.str.strip()

print("Columns:", df.columns)
print(df.head())

# Optional: calculate Profit (if needed)
# df['Profit'] = df['Total_Sales'] - (df['Quantity'] * df['Price'])

# -----------------------------
# Step 2: Seaborn statistical plots
# -----------------------------

# 1. Boxplot - Total Sales by Product
plt.figure(figsize=(8,6))
sns.boxplot(x="Product", y="Total_Sales", data=df)
plt.title("Total Sales Distribution by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 2. Violin Plot - Total Sales by Region
plt.figure(figsize=(8,6))
sns.violinplot(x="Region", y="Total_Sales", data=df, inner="quartile", palette="Set2")
plt.title("Total Sales Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 3. Heatmap - Correlation matrix for numeric columns
numeric_cols = df.select_dtypes(include=['int64','float64']).columns
plt.figure(figsize=(8,6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# -----------------------------
# Step 3: Plotly interactive charts
# -----------------------------

# 4. Pie Chart - Total Sales by Product
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()
fig1 = px.pie(product_sales, names="Product", values="Total_Sales",
              title="Total Sales by Product", hole=0.3)
fig1.show()

# 5. Bar Chart - Total Sales by Region
region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()
fig2 = px.bar(region_sales, x="Region", y="Total_Sales", color="Total_Sales",
              title="Total Sales by Region", text="Total_Sales")
fig2.update_traces(texttemplate="%{text:.2s}", textposition="outside")
fig2.show()

# 6. Line Chart - Sales Trend Over Time
if "Date" in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    sales_trend = df.groupby('Date')["Total_Sales"].sum().reset_index()
    fig3 = px.line(sales_trend, x="Date", y="Total_Sales", title="Sales Trend Over Time",
                   markers=True)
    fig3.show()

# -----------------------------
# Step 4: Combined Dashboard Layout
# -----------------------------
fig_dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Sales by Product", "Sales by Region", "Sales Distribution by Product", "Sales Trend Over Time"),
    specs=[[{"type": "domain"}, {"type": "bar"}],
           [{"type": "box"}, {"type": "scatter"}]]
)

# Pie - Product Sales
fig_dashboard.add_trace(go.Pie(labels=product_sales["Product"], values=product_sales["Total_Sales"], name="Product Sales"),
                        row=1, col=1)

# Bar - Region Sales
fig_dashboard.add_trace(go.Bar(x=region_sales["Region"], y=region_sales["Total_Sales"], name="Region Sales"),
                        row=1, col=2)

# Boxplot - Total Sales by Product
for prod in df["Product"].unique():
    fig_dashboard.add_trace(go.Box(y=df[df["Product"]==prod]["Total_Sales"], name=prod),
                            row=2, col=1)

# Line - Sales Trend
if "Date" in df.columns:
    fig_dashboard.add_trace(go.Scatter(x=sales_trend["Date"], y=sales_trend["Total_Sales"],
                                       mode='lines+markers', name="Sales Trend"),
                            row=2, col=2)

fig_dashboard.update_layout(height=800, width=1000, title_text="Interactive Sales Dashboard")
fig_dashboard.show()
