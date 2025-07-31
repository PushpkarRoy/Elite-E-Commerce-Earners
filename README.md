# 🏆 Elite E-Commerce Earners
**A Year-wise High-Spender Analysis Using SQL and Python**

## 📊 Project Overview
This project identifies the **top 3 highest-spending customers for each year** in an e-commerce environment. It uses advanced SQL window functions and Python visualization tools to spotlight customers who drive the most revenue.

---

## 🔍 Objective
- Track the **top-spending customers per year**
- Visualize their **total contributions**
- Enable business teams to **prioritize loyalty strategies** for high-value users

---

## 🛠️ Tools & Technologies
- **PostgreSQL** (SQL queries and aggregation)
- **Pandas** (data wrangling)
- **Seaborn & Matplotlib** (visualizations)
- **Jupyter Notebook** (execution and analysis)

---

## 📁 Dataset Description
This analysis is based on a PostgreSQL database consisting of:
- `orders` – Order metadata and timestamps
- `payments` – Payment values associated with each order
- `customers` – Customer-level identifiers

> **Note:** The SQL script used to generate the data is available in this repo as `E_commercce_SQL.sql`.

---

## 🔧 How It Works
1. SQL query extracts:
   - Year from order timestamps
   - Total amount spent per customer
   - Top 3 customers per year using `RANK()` window function

2. The query output is visualized in Python with a **grouped bar chart** showing each top customer’s spend per year.

---

## 📊 Visual Output
<img width="729" height="925" alt="image" src="https://github.com/user-attachments/assets/e7ac0a92-5fc8-45a6-b460-a8f02a3d22e9" />


> The chart clearly shows which customers brought the most revenue in each year, enabling targeted retention strategies.

---

## 🚀 Future Enhancements
- Add customer segmentation (loyalty tiers)
- Merge with marketing data to assess ROI per customer
- Automate SQL → Python → Dashboard pipeline

---

## 👤 Author
**Pushpkar Roy**  
📧 pushpkarroy880@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/pushpkar-roy/)  
🐙 [GitHub](https://github.com/PushpkarRoy)

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
