import pandas as pd
import matplotlib.pyplot as plt

# 读取两个 CSV 文件
eln_df = pd.read_csv("eln.csv")
no_eln_df = pd.read_csv("no_eln.csv")

# 限定最多绘前 N 个流（可选）
N = min(len(eln_df), len(no_eln_df), 10)

# 提取字节数列并转为 Mbps（假设时长为 10s，可改为从 XML 提取精确值）
eln_mbps = eln_df["Bytes"].head(N) * 8 / 1e6 / 10
no_eln_mbps = no_eln_df["Bytes"].head(N) * 8 / 1e6 / 10

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(range(N), eln_mbps, marker='o', label="With ELN")
plt.plot(range(N), no_eln_mbps, marker='x', label="No ELN")
plt.xlabel("Flow Index")
plt.ylabel("Throughput (Mbps)")
plt.title("TCP Throughput Comparison (ELN vs No ELN)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("tcp_eln_vs_no_eln.png")
plt.show()
