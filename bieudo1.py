import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.info())

# profit = df ['total_profit'].tolist()
profit = df ['facecream'].tolist()
arofit = df ['facewash'].tolist()
brofit = df ['toothpaste'].tolist()
crofit = df ['bathingsoap'].tolist()
drofit = df ['shampoo'].tolist()
erofit = df ['moisturizer'].tolist()


monthl = df ['month_number'].tolist()

plt.figure("Biểu đồ đoạn thẳng")
plt.plot(monthl,profit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'green',label = 'facecream')
plt.plot(monthl,arofit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'red',label = 'facewash')
plt.plot(monthl,brofit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'orange',label = 'toothpaste')
plt.plot(monthl,crofit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'blue',label = 'bathingsoap')
plt.plot(monthl,drofit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'purple',label = 'shampoo')
plt.plot(monthl,erofit,marker = 'o',mec = 'black', mfc = 'black',linestyle = 'dashed',color = 'brown',label = 'moisturizer')
plt.legend()


plt.xlabel("tháng")
plt.ylabel("Lợi nhuận ($)")
plt.xticks(monthl)
plt.title("Lợi nhuân hàng tháng năm 2021")

plt.show()

