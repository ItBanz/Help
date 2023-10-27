import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.info())

arofit = df ['facewash'].tolist()
crofit = df ['bathingsoap'].tolist()
monthl = df ['month_number'].tolist()
plt.figure("Biểu đồ đoạn thẳng split")
plt.subplot(2, 1, 1)
plt.title("số lương xà bông tắm đã bán")
plt.plot(monthl,arofit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'red',label = 'facewash')
plt.legend()
plt.xticks(monthl)

plt.subplot(2, 1, 2)
plt.title("số lương sửa rữa mặt đã bán")
plt.plot(monthl,crofit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'blue',label = 'bathingsoap')
plt.legend()
plt.xticks(monthl)


plt.show()

