import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
matplotlib.use('Agg')

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

plt.figure("Biểu đồ tròn")
plt.pie(monthl,labels=profit,autopct='%1.1f%%')
plt.pie(monthl,labels=arofit,autopct='%1.1f%%')
plt.pie(monthl,labels=brofit,autopct='%1.1f%%')
plt.pie(monthl,labels=crofit,autopct='%1.1f%%')
plt.pie(monthl,labels=drofit,autopct='%1.1f%%')
plt.pie(monthl,labels=erofit,autopct='%1.1f%%')



plt.title("mặt hàng 2021")

plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

