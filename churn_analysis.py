import pandas as pd
df = pd.read_excel("customer_churn_dataset.xlsx")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].median()
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

df["PaymentMethod"] = df["PaymentMethod"].fillna(
    df["PaymentMethod"].mode()[0]
)

# Check cleaned data
print("\nAfter Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Save
df.to_excel("cleaned_customer_churn.xlsx", index=False)

print("\nCleaning completed successfully!")
# ==========================================
# STEP 3 - EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

import matplotlib.pyplot as plt
import pandas as pd

# ------------------------------------------
# 1. BASIC CUSTOMER SUMMARY
# ------------------------------------------

print("\n==============================")
print("CUSTOMER SUMMARY")
print("==============================")

print("Total Customers:", len(df))

print("\nChurn Count:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print(
    (df["Churn"].value_counts(normalize=True) * 100).round(2)
)


# ------------------------------------------
# 2. CUSTOMER CHURN - BAR CHART
# ------------------------------------------

churn_count = df["Churn"].value_counts()

plt.figure(figsize=(6, 4))
churn_count.plot(kind="bar")

plt.title("Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------
# 3. CONTRACT TYPE vs CHURN
# ------------------------------------------

contract_churn = pd.crosstab(
    df["ContractType"],
    df["Churn"]
)

print("\n==============================")
print("CONTRACT TYPE vs CHURN")
print("==============================")

print(contract_churn)

plt.figure(figsize=(8, 5))
contract_churn.plot(kind="bar")

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------
# 4. GENDER vs CHURN
# ------------------------------------------

gender_churn = pd.crosstab(
    df["Gender"],
    df["Churn"]
)

print("\n==============================")
print("GENDER vs CHURN")
print("==============================")

print(gender_churn)

plt.figure(figsize=(7, 5))
gender_churn.plot(kind="bar")

plt.title("Customer Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------
# 5. PAYMENT METHOD vs CHURN
# ------------------------------------------

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

print("\n==============================")
print("PAYMENT METHOD vs CHURN")
print("==============================")

print(payment_churn)

plt.figure(figsize=(9, 5))
payment_churn.plot(kind="bar")

plt.title("Customer Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.show()


# ------------------------------------------
# 6. INTERNET SERVICE vs CHURN
# ------------------------------------------

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

print("\n==============================")
print("INTERNET SERVICE vs CHURN")
print("==============================")

print(internet_churn)

plt.figure(figsize=(8, 5))
internet_churn.plot(kind="bar")

plt.title("Customer Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()



# ==========================================
# 7. TENURE vs CHURN
# ==========================================

print("\n==============================")
print("TENURE vs CHURN")
print("==============================")

# Calculate average tenure
tenure_average = df.groupby("Churn")["Tenure"].mean().round(2)

print("Average Tenure:")
print(tenure_average)


# Create clean bar chart
plt.figure(figsize=(7, 5))

bars = plt.bar(
    tenure_average.index,
    tenure_average.values
)

plt.title("Average Customer Tenure by Churn",
          fontsize=15,
          fontweight="bold")

plt.xlabel("Customer Churn",
           fontsize=11)

plt.ylabel("Average Tenure (Months)",
           fontsize=11)

plt.grid(axis="y",
         linestyle="--",
         alpha=0.3)

# Add values on top of bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        f"{height:.2f}",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()


# ==========================================
# 8. MONTHLY CHARGES vs CHURN
# ==========================================

print("\n==============================")
print("MONTHLY CHARGES vs CHURN")
print("==============================")

# Calculate average monthly charges
monthly_average = df.groupby("Churn")["MonthlyCharges"].mean().round(2)

print("Average Monthly Charges:")
print(monthly_average)


# Create clean bar chart
plt.figure(figsize=(7, 5))

bars = plt.bar(
    monthly_average.index,
    monthly_average.values
)

plt.title(
    "Average Monthly Charges by Churn",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel(
    "Customer Churn",
    fontsize=11
)

plt.ylabel(
    "Average Monthly Charges",
    fontsize=11
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Add values on top of bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 2,
        f"{height:.2f}",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()

# ==========================================
# 9. SUPPORT CALLS vs CHURN
# ==========================================

print("\n==============================")
print("SUPPORT CALLS vs CHURN")
print("==============================")

print(
    df.groupby("Churn")["SupportCalls"].mean().round(2)
)

support_churn = df.groupby("Churn")["SupportCalls"].mean()

plt.figure(figsize=(6, 4))
support_churn.plot(kind="bar")

plt.title("Average Support Calls by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Support Calls")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ==========================================
# 10. AGE vs CHURN
# ==========================================

print("\n==============================")
print("AGE vs CHURN")
print("==============================")

# Calculate average age
age_average = df.groupby("Churn")["Age"].mean().round(2)

print("Average Age:")
print(age_average)


# Create clean bar chart
plt.figure(figsize=(7, 5))

bars = plt.bar(
    age_average.index,
    age_average.values
)

plt.title(
    "Average Customer Age by Churn",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel(
    "Customer Churn",
    fontsize=11
)

plt.ylabel(
    "Average Age (Years)",
    fontsize=11
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Add values on top of bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        f"{height:.2f}",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()
# ------------------------------------------
# 11. AGE GROUP ANALYSIS
# ------------------------------------------

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-65",
        "66+"
    ]
)

agegroup_churn = pd.crosstab(
    df["AgeGroup"],
    df["Churn"]
)

print("\n==============================")
print("AGE GROUP vs CHURN")
print("==============================")

print(agegroup_churn)

plt.figure(figsize=(9, 5))
agegroup_churn.plot(kind="bar")

plt.title("Customer Churn by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------
# 12. CHURN RATE BY CONTRACT TYPE
# ------------------------------------------

contract_rate = pd.crosstab(
    df["ContractType"],
    df["Churn"],
    normalize="index"
) * 100

print("\n==============================")
print("CHURN RATE BY CONTRACT")
print("==============================")

print(contract_rate.round(2))

plt.figure(figsize=(8, 5))

if "Yes" in contract_rate.columns:
    contract_rate["Yes"].plot(kind="bar")

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------
# 13. CHURN RATE BY PAYMENT METHOD
# ------------------------------------------

payment_rate = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100

print("\n==============================")
print("CHURN RATE BY PAYMENT METHOD")
print("==============================")

print(payment_rate.round(2))

plt.figure(figsize=(9, 5))

if "Yes" in payment_rate.columns:
    payment_rate["Yes"].plot(kind="bar")

plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.show()


# ------------------------------------------
# 14. FINAL SUMMARY
# ------------------------------------------

print("\n===================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("===================================")

print("Total Customers:", len(df))

print(
    "Overall Churn Rate:",
    round((df["Churn"] == "Yes").mean() * 100, 2),
    "%"
)

print("\nAverage Monthly Charges by Churn:")

print(
    df.groupby("Churn")["MonthlyCharges"]
    .mean()
    .round(2)
)

print("\nAverage Tenure by Churn:")

print(
    df.groupby("Churn")["Tenure"]
    .mean()
    .round(2)
)

print("\nAverage Support Calls by Churn:")

print(
    df.groupby("Churn")["SupportCalls"]
    .mean()
    .round(2)
)

# ==========================================
# STEP 4 - SQL ANALYSIS
# ==========================================

import sqlite3

conn = sqlite3.connect("customer_churn.db")
cursor = conn.cursor()


# ------------------------------------------
# 1. TOTAL CUSTOMERS
# ------------------------------------------

print("\n==============================")
print("1. TOTAL CUSTOMERS")
print("==============================")

cursor.execute("""
SELECT COUNT(*)
FROM customers
""")

print("Total Customers:", cursor.fetchone()[0])


# ------------------------------------------
# 2. TOTAL CHURNED CUSTOMERS
# ------------------------------------------

print("\n==============================")
print("2. TOTAL CHURNED CUSTOMERS")
print("==============================")

cursor.execute("""
SELECT COUNT(*)
FROM customers
WHERE Churn = 'Yes'
""")

print("Churned Customers:", cursor.fetchone()[0])


# ------------------------------------------
# 3. OVERALL CHURN RATE
# ------------------------------------------

print("\n==============================")
print("3. OVERALL CHURN RATE")
print("==============================")

cursor.execute("""
SELECT
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    )
FROM customers
""")

print("Churn Rate:", cursor.fetchone()[0], "%")


# ------------------------------------------
# 4. CHURN BY CONTRACT TYPE
# ------------------------------------------

print("\n==============================")
print("4. CHURN BY CONTRACT TYPE")
print("==============================")

cursor.execute("""
SELECT
    ContractType,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers
FROM customers
GROUP BY ContractType
""")

for row in cursor.fetchall():
    print(row)


# ------------------------------------------
# 5. CHURN BY PAYMENT METHOD
# ------------------------------------------

print("\n==============================")
print("5. CHURN BY PAYMENT METHOD")
print("==============================")

cursor.execute("""
SELECT
    PaymentMethod,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers
FROM customers
GROUP BY PaymentMethod
""")

for row in cursor.fetchall():
    print(row)


# ------------------------------------------
# 6. AVERAGE MONTHLY CHARGES BY CHURN
# ------------------------------------------

print("\n==============================")
print("6. AVERAGE MONTHLY CHARGES")
print("==============================")

cursor.execute("""
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2)
FROM customers
GROUP BY Churn
""")

for row in cursor.fetchall():
    print(row)


# ------------------------------------------
# 7. AVERAGE TENURE BY CHURN
# ------------------------------------------

print("\n==============================")
print("7. AVERAGE TENURE")
print("==============================")

cursor.execute("""
SELECT
    Churn,
    ROUND(AVG(Tenure), 2)
FROM customers
GROUP BY Churn
""")

for row in cursor.fetchall():
    print(row)


# ------------------------------------------
# 8. AVERAGE SUPPORT CALLS BY CHURN
# ------------------------------------------

print("\n==============================")
print("8. AVERAGE SUPPORT CALLS")
print("==============================")

cursor.execute("""
SELECT
    Churn,
    ROUND(AVG(SupportCalls), 2)
FROM customers
GROUP BY Churn
""")

for row in cursor.fetchall():
    print(row)


# ------------------------------------------
# 9. CHURN BY INTERNET SERVICE
# ------------------------------------------

print("\n==============================")
print("9. CHURN BY INTERNET SERVICE")
print("==============================")

cursor.execute("""
SELECT
    InternetService,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers
FROM customers
GROUP BY InternetService
""")

for row in cursor.fetchall():
    print(row)


# ------------------------------------------
# 10. HIGH VALUE CHURNED CUSTOMERS
# ------------------------------------------

print("\n==============================")
print("10. HIGH VALUE CHURNED CUSTOMERS")
print("==============================")

cursor.execute("""
SELECT
    ContractType,
    MonthlyCharges,
    Tenure,
    PaymentMethod
FROM customers
WHERE Churn = 'Yes'
AND MonthlyCharges >= 100
ORDER BY MonthlyCharges DESC
LIMIT 10
""")

for row in cursor.fetchall():
    print(row)


# ------------------------------------------
# CLOSE DATABASE
# ------------------------------------------

conn.close()

print("\n===================================")
print("SQL ANALYSIS COMPLETED SUCCESSFULLY!")
print("===================================")