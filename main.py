import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

# TKINTER
root = tk.Tk()
root.withdraw()  # Hide the main window

# BANNER
print("=" * 40)
print("       S T U D Y R E C E I P T")
print("   You studied. Here's your receipt.")
print("=" * 40)
print()

# INPUT
subjects = []
hours_list = []
marks_list = []

count = simpledialog.askinteger("Study Receipt", "How many subjects?")
print()

for i in range(count):
    name = simpledialog.askstring("Study Receipt", "Subject name:")
    hours = simpledialog.askfloat("Study Receipt", "Hours studied:")
    marks = simpledialog.askfloat("Study Receipt", "Marks scored:")
    print()

    subjects.append(name)
    hours_list.append(hours)
    marks_list.append(marks)

# PANDAS
df = pd.DataFrame({
    "Subject": subjects,
    "Hours": hours_list,
    "Marks": marks_list
})

df["Efficiency"] = round(df["Marks"] / df["Hours"], 2)

print("── Your Receipt ──")
print(df)
print()

# VERDICT
# oru hourl ethre mark(score cheythathinte) padichu.
# if i scored 90 mark by studying 5 hour, i learned for 18 mark in an hour.

avg = df["Efficiency"].mean()

print("── Verdict ──")
if avg >= 8:
    print("You actually studied. Respect.")
elif avg >= 5:
    print("Decent. Could be worse.")
elif avg >= 3:
    print("You studied. The marks didn't agree.")
else:
    print("Reconsider your life choices.")

print()

# CHART
plt.bar(df["Subject"], df["Efficiency"], color="skyblue")
plt.title("Study Receipt - Efficiency Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks per Hour")
plt.tight_layout()
plt.show()

# Close Tkinter
root.destroy()
