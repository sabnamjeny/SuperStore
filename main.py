import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Step 1: Load Data
df = pd.read_csv("C:/Users/Hp/Downloads/SuperStore_Sales_Dataset.csv")  
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

# ✅ Step 2: Feature Engineering
df['month'] = df['order_date'].dt.to_period('M')

# ✅ Step 3: Monthly Sales Trend
monthly_sales = df.groupby('month')['sales'].sum().reset_index()

# ✅ Step 4: Top 10 Products
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)

# ✅ Step 5: Top 10 Cities
region_sales = df.groupby('city')['sales'].sum().sort_values(ascending=False).head(10)

# ================== Streamlit Layout ==================

st.title("📊 Sales Dashboard - Superstore")
st.markdown("A simple dashboard with Monthly Trend, Top Products, and Regional Performance.")

# 🔹 Monthly Sales Trend
st.subheader("📅 Monthly Sales Trend")
fig1, ax1 = plt.subplots(figsize = (12,6))
ax1.plot(monthly_sales['month'].astype(str), monthly_sales['sales'], marker='o', color='teal')
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
ax1.set_title("Monthly Sales Trend")
plt.xticks(rotation=45)
st.pyplot(fig1)

# 🔹 Top 10 Products
st.subheader("🏆 Top 10 Products")
fig2, ax2 = plt.subplots(figsize = (10,5))
top_products.plot(kind='bar', ax=ax2, color='orange')
ax2.set_ylabel("Sales")
ax2.set_title("Top 10 Products by Sales")
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig2)

# 🔹 Regional Sales (City-wise)
st.subheader("🌆 Top 10 Cities by Sales")
fig3, ax3 = plt.subplots(figsize = (10,5))
region_sales.plot(kind='bar', ax=ax3, color='purple')
ax3.set_ylabel("Sales")
ax3.set_title("Top 10 Cities")
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig3)

# 🔹 View Data
with st.expander("🔍 See Raw Data"):
    st.dataframe(df.head(20))

