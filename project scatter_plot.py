import pandas as pd
import seaborn as sns
import matplotlib as plt

data =pd.read_excel('C:Users/Eleena lilly babu/Downloads/Financial Sample.xlsx')

sum = data.groupby('Month Name')['Profit'].sum()

plt.figure(figsize=(9,7))
sns.scatterplot(sum, s=100,color ='purple')

plt.title('MONTHLY PROFIT',color ='blue')
plt.xlabel('Months',color='green')
plt.ylabel('Profits',color='green')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
