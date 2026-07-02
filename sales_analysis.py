import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df)

print("\nTotal Sales:",df["Sales"].sum())

plt.plot(df["Month"],df["Sales"],marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()