import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('c:Users/Eleena lilly babu/Downloads/Financial Sample.xlsx')

sum =data.groupby('product')['Profit'].sum()
plt.figure(figsize=(8, 6))
plt.pie(sum, labels=sum.index,autopct='%1.1f%%')
plt.title('PROFIT REPORT OF PRODUCTS',color ='green')

plt.show()
