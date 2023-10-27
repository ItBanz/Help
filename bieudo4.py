import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("sales_data.csv")
print(df.info())

# profit = df ['total_profit'].tolist()

arofit = df ['facewash'].tolist()
erofit = df ['moisturizer'].tolist()


monthl = df ['month_number'].tolist()

plt.figure("Biểu đồ đoạn thẳng")
monthl = np.arange(len(df))
plt.bar(monthl - 0.2,arofit,0.4,color = 'red',label = 'facewash')
plt.bar(monthl + 0.2,erofit,0.4,color = 'brown',label = 'moisturizer')
plt.legend()


plt.xlabel("tháng")
plt.ylabel("Lợi nhuận ($)")
plt.xticks(monthl)
plt.title("số lượng bán")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

