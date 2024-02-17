import pandas as pd
import mstplotlib.pyplot as plt

data = pd.read_excel('C:/Users/Eleena lilly babu/Downloads/Financial Sample.xlsx')

sales_sum =data.groupby('Month Name')['Sales'].sum()

plt.figure(figsize=(8,6))
plt.plot(sales_sum, marker='o;, linestyle='-')

plt.xlabel('Months',color='purple')
plt.ylabel('Sales',color='purple')
plt.itle('MONTHLY SALES',color='purple')

plt.xticks(rotation =45)
plt.tight_layout()
plt.show()
