import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

st.set_page_config(page_title="Sales Analysis App", layout="centered")

st.title("📊 Sales Data Analysis Dashboard")

np.random.seed(42) #random state

# Create data
data = {
    'product_id': range(1, 21),
    'Product_name': [f'Product_{i}' for i in range(1, 21)],
    "category": np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], size=20),
    "unit_sold": np.random.poisson(lam=20, size=20),
    "sales_date": pd.date_range(start='2025-01-01', periods=20, freq='D') + pd.to_timedelta(np.random.randint(0, 86400, 20), unit='s')

}

sales_data = pd.DataFrame(data)
sales_data.to_csv('sales_data.csv', index=False)

# Show data section
st.header("📝 Sales Dataset")
st.dataframe(sales_data, use_container_width=True)

# ----------- Descriptive Statistics -----------
st.header("📈 Descriptive Statistics for 'unit_sold'")
discriptive_stats = sales_data['unit_sold'].describe()
st.write(discriptive_stats)

# --- Statistical summaries
mean_sales = sales_data['unit_sold'].mean()
median_sales = sales_data['unit_sold'].median()
mode_sales = sales_data['unit_sold'].mode()[0]
varience_sales = sales_data['unit_sold'].var()
std_deviation_sales = sales_data['unit_sold'].std()

with st.expander("See summary statistics"):
    st.markdown(f"**Mean unit sold:** {mean_sales}")
    st.markdown(f"**Median unit sold:** {median_sales}")
    st.markdown(f"**Mode unit sold:** {mode_sales}")
    st.markdown(f"**Variance unit sold:** {varience_sales}")
    st.markdown(f"**Standard Deviation unit sold:** {std_deviation_sales}")

category_stats = sales_data.groupby('category')['unit_sold'].agg(['sum','mean', 'median', 'var', 'std']).reset_index()

st.header("📦 Category Statistics")
st.dataframe(category_stats, use_container_width=True)

# ----------- Inferential Statistics -----------
st.header("🎯 Confidence Interval for Mean 'unit_sold'")
confidence_level = 0.95
degrees_freedom = len(sales_data['unit_sold']) - 1
sample_mean = mean_sales
sample_standard_error = std_deviation_sales / np.sqrt(len(sales_data['unit_sold']))
t_score = stats.t.ppf((1 + confidence_level) / 2, degrees_freedom)
margin_of_error = t_score * sample_standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
st.info(f"95% Confidence Interval: {confidence_interval}")

# ----------- Hypothesis Testing -----------
st.header("🔎 One-sample t-test: Is mean unit_sold = 20?")
t_statistic, p_value = stats.ttest_1samp(sales_data['unit_sold'], popmean=20)
st.write(f"**T-statistic:** {t_statistic:.3f}")
st.write(f"**P-value:** {p_value:.3f}")
if p_value < 0.05:
    st.success("Reject the null hypothesis: The average unit sold is significantly different from 20.")
else:
    st.info("Fail to reject the null hypothesis: The average unit sold is not significantly different from 20.")

# ----------- Visualizations -----------
sns.set(style='whitegrid')

st.header("📊 Distribution of Units Sold")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.histplot(sales_data['unit_sold'], bins=10, kde=True, color='blue', ax=ax1)
ax1.set_title('Distribution of Units Sold')
ax1.set_xlabel('Units Sold')
ax1.set_ylabel('Frequency')
ax1.axvline(mean_sales, color='red', linestyle='--', label='Mean')
ax1.axvline(median_sales, color='blue', linestyle='--', label='Median')
ax1.axvline(mode_sales, color='green', linestyle='--', label='Mode')
ax1.legend()
st.pyplot(fig1)

st.header("📦 Units Sold by Category (Boxplot)")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='category', y='unit_sold', data=sales_data, ax=ax2)
ax2.set_title('Units Sold by Category')
ax2.set_xlabel('Category')
ax2.set_ylabel('Units Sold')
st.pyplot(fig2)

st.header("🗂️ Total Units Sold by Category (Bar Plot)")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x='category', y='sum', data=category_stats, ax=ax3)
ax3.set_title('Total Units Sold by Category')
ax3.set_xlabel('Category')
ax3.set_ylabel('Total Units Sold')
st.pyplot(fig3)

# -------- Credits / footer -----------
st.markdown("---")
st.caption("Made by 💡 Pranay Pinjarkar | Data and calculations are generated fresh on each run.")
