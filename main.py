import pandas as pd

df = pd.read_csv("data/employees.csv")

print("Original Data:")
print(df)

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

# Statistics
print("\nAverage Salary:", df["Salary"].mean())
print