import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("memory_latency_results.csv")

# Extract values
sizes = df["Bytes"]
random_lat = df["RandomAccessLatency(ns)"]
seq_lat = df["SequentialAccessLatency(ns)"]

# Cache sizes from lscpu
L1 = 32 * 1024          # 32KB per core
L2 = 256 * 1024         # 256KB per core
L3 = 9 * 1024 * 1024    # 9MB shared

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sizes, random_lat, label='Random access')
plt.plot(sizes, seq_lat, label='Sequential access')

# Vertical cache lines
plt.axvline(L1, color='red', label='L1 (32KB)')
plt.axvline(L2, color='green', label='L2 (256KB)')
plt.axvline(L3, color='brown', label='L3 (9MB)')

# Labels and title
plt.xlabel("Bytes allocated (log scale)")
plt.ylabel("Latency (ns)")
plt.title("Latency as a function of array size on Intel(R) Core(TM) i5-8500 CPU @ 3.00GHz")
plt.xscale("log")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save to file
plt.savefig("results.png", dpi=300)
print("Saved plot as results.png")
