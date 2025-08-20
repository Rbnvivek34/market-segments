# Author: 22f2001699@ds.study.iitm.ac.in
# Note: This code was generated with the help of an LLM (ChatGPT/Codex).

import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP

# --- Load data (CSV included in the PR) ---
df = pd.read_csv("mrr_quarterly_2024.csv")  # columns: Quarter, MRR_Growth

# --- Compute average using ROUND_HALF_UP so it matches 5.77 exactly ---
vals = [Decimal(str(v)) for v in df["MRR_Growth"]]
avg = (sum(vals) / Decimal(len(vals))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # 5.77

print("Quarterly MRR Growth (2024):")
print(df.to_string(index=False))
print(f"\nAverage MRR Growth: {avg}")
print("Industry Target: 15")

# --- Plot (matplotlib only, single plot, no custom colors) ---
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(df["Quarter"], df["MRR_Growth"], marker="o")
ax.axhline(15, linestyle="--")  # industry target line
ax.set_title("2024 Quarterly MRR Growth vs Industry Target")
ax.set_xlabel("Quarter")
ax.set_ylabel("MRR Growth")

# annotate points
for q, v in zip(df["Quarter"], df["MRR_Growth"]):
    ax.annotate(f"{v}", (q, v), xytext=(0, 5), textcoords="offset points", ha="center")

# annotate average
ax.annotate(f"Average: {avg}", (0.02, 0.9), xycoords="axes fraction")

plt.tight_layout()
plt.savefig("mrr_benchmark.png", dpi=150, bbox_inches="tight")
