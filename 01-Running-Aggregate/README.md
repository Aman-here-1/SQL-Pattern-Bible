# 📈 Pattern 01 - Running Aggregate

## 🎯 Business Requirement

Running Aggregate is used when the business wants to track cumulative progress over time.

Instead of calculating values for individual rows, we calculate a running total, running count, or running average from the beginning up to the current row.

---

# 💼 Real Business Use Cases

- Customer Lifetime Spend
- Running Revenue
- Running Profit
- Running Orders
- Running Trips
- Running Sales
- Running Inventory
- Running Watch Time

Companies:

- Uber
- Swiggy
- Zomato
- Amazon
- Flipkart
- PhonePe
- Razorpay

---

# 🧠 Pattern Recognition

```
Need cumulative value?

↓

Running Aggregate

↓

SUM() OVER()

or

COUNT() OVER()

or

AVG() OVER()
```

---

# 📋 Business Thinking

Whenever the interviewer asks:

- Running Sales
- Lifetime Spend
- Total Earnings Till Date
- Cumulative Orders
- Running Profit

👉 Think **Running Aggregate**

---

# 🛠 SQL Template

```sql
SELECT
    customer_id,
    order_date,
    amount,

    SUM(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS running_total

FROM orders;
```

---

# 📚 Common Aggregate Functions

| Function | Use Case |
|----------|----------|
| SUM() | Running Revenue |
| COUNT() | Running Orders |
| AVG() | Running Average |
| MAX() | Highest Till Date |
| MIN() | Lowest Till Date |

---

# 🔥 Interview Questions

- Running Customer Spend
- Running Driver Earnings
- Running Order Count
- Running Profit
- Running Watch Time
- Gold Customer Identification
- Loyalty Program
- Running Revenue

---

# 🏆 Companies Asking This Pattern

- Uber
- Amazon
- Swiggy
- Zomato
- Google
- Microsoft
- Meesho
- Razorpay
- PhonePe

---

# 📖 Difficulty

⭐ Beginner

---

# 🎯 Key Takeaway

Running Aggregate is one of the most frequently asked SQL interview patterns.

Instead of solving questions individually, recognize the pattern first and then apply the appropriate window function.
