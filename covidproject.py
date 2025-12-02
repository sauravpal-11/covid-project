import pandas as pd # type: ignore
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv(r"C:\ProgramData\covid data.csv")

# Convert DATE column to datetime
df["DATE"] = pd.to_datetime(df["DATE"])

# -------- LINE PLOT --------
plt.figure(figsize=(10, 5))

plt.plot(df["DATE"], df["india"], marker='o', label="India")
plt.plot(df["DATE"], df["USA"], marker='o', label="USA")
plt.plot(df["DATE"], df["UK"], marker='o', label="UK")

plt.xlabel("DATE")
plt.ylabel("Number of cases")
plt.legend()
plt.grid(True)
plt.show()

# -------- PIE CHART --------
latest = df.iloc[-1, 1:]  # last row, columns from index 1 onward

plt.figure(figsize=(6, 6))
plt.pie(latest, labels=latest.index, autopct="%1.1f%%", startangle=90)
plt.title("Covid-19 Data (Latest)")
plt.show()
