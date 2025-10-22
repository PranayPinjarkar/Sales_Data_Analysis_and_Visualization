# 📊 Sales Data Analysis Dashboard

A Streamlit web application that performs descriptive and inferential statistical analysis on randomly generated sales data. This interactive dashboard visualizes business insights, computes statistical measures, and conducts hypothesis testing — all in real-time.

---

## 🚀 Features

- **Dynamic Sales Dataset**  
  Automatically generates a 20-product sales dataset with synthetic attributes like product category, units sold, and timestamped sales dates.

- **Descriptive Statistics**  
  Displays statistical summaries such as mean, median, mode, variance, and standard deviation for sales units.

- **Category-Level Insights**  
  Aggregates and visualizes sales performance across different product categories (Electronics, Clothing, Home, Books).

- **Inferential Statistics**  
  Calculates confidence intervals for mean sales and performs a one-sample t-test to assess statistical significance against a population mean.

- **Visual Analytics**
  - Histogram with KDE for unit distribution  
  - Category-wise box plots  
  - Aggregated bar charts of total sales  

- **Interactive UI**
  - Expandable sections for summary statistics  
  - Real-time statistical recalculations  
  - Clean, responsive Streamlit interface  

---

## 🧠 Technologies Used

- **Python 3.10+**
- **Streamlit** – UI framework for building interactive data apps  
- **Pandas** – Data manipulation and analysis  
- **NumPy** – Numerical operations and random data generation  
- **Matplotlib & Seaborn** – Data visualization  
- **SciPy** – Statistical analysis (confidence intervals, t-tests)

---

## 📂 Project Structure

Sales-Analysis-App/
│
├── app.py # Main Streamlit app file
├── sales_data.csv # Auto-generated dataset at runtime
├── requirements.txt # Project dependencies
└── README.md # Project documentation (this file)


---

## ⚙️ Installation and Setup

1. **Clone or Download the Repository**
git clone https://github.com/yourusername/sales-analysis-app.git
cd sales-analysis-app


2. **Install Dependencies**
pip install -r requirements.txt

*(If `requirements.txt` doesn’t exist yet, create one with the following line:)*
streamlit pandas numpy matplotlib seaborn scipy

3. **Run the Application**
streamlit run app.py


4. **Open in Browser**
Navigate to `http://localhost:8501/` to view the dashboard.

---

## 📸 Dashboard Preview

*Example screenshots can be added here:*  
- Dataset display  
- Statistical summaries  
- Distribution and category plots  

---

## 📈 Statistical Components

| Section | Description |
|----------|--------------|
| **Descriptive Stats** | Computes mean, median, mode, variance, and std deviation for units sold. |
| **Category Summary** | Aggregates total and average sales per product category. |
| **Confidence Interval** | Estimates 95% CI for mean units sold. |
| **T-Test** | Tests if the average units sold differ significantly from 20. |

---

## 🎨 Visualizations

- **Histogram:** Distribution of `unit_sold` with descriptive markers  
- **Boxplot:** Spread of sales across product categories  
- **Bar Chart:** Total units sold per category  

Each chart is generated dynamically with clean color palettes and labeled axes.

---

## 🧾 Example Output Summary

- Mean unit sold ≈ 20  
- 95% Confidence Interval ≈ (17.8, 22.4)  
- Hypothesis Test Result → *Fail to reject null hypothesis (p > 0.05)*

*(Note: Results will vary per run due to random data generation.)*

---

## ✨ Author

**Pranay Pinjarkar**  
💡 Passionate about data analysis, visualization, and building intelligent systems.

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).



