import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.info())

# profit = df ['total_profit'].tolist()
profit = df ['facecream'].tolist()
arofit = df ['facewash'].tolist()



monthl = df ['month_number'].tolist()

plt.figure("Biểu đồ tán xạ")
plt.scatter(monthl,profit,color = 'green',label = 'facecream')
plt.scatter(monthl,arofit,color = 'red',label = 'facewash')

plt.legend()


plt.xlabel("tháng")
plt.ylabel("số lượng bán")
plt.xticks(monthl)
plt.title("số lượng bán của sữa rửa mặt và kem dưỡng da theo tháng")

plt.show()

