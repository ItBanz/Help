import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.info())

# profit = df ['total_profit'].tolist()

crofit = df ['bathingsoap'].tolist()


monthl = df ['month_number'].tolist()

plt.figure("Biểu đồ đoạn thẳng")

plt.bar(monthl,crofit,color = 'blue',label = 'bathingsoap')

plt.legend()


plt.xlabel("tháng")
plt.ylabel("số lượng bán")
plt.xticks(monthl)
plt.title("số lượng xà bông tắm theo tháng")

plt.show()

