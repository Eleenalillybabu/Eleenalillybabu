import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('C:Users/Eleena lilly babu/Downloads/Financial Sample.xlsx')

segments +data['Segment']
Total_Sales = data['Sales']

plt.figures(figsize=(8,6))
plt.bar(segments,Total_Sales ,color='skyblue')

plt.xlabel('segment',color ='blue')
plt.ylabel('Sales',color ='blue')
plt.itle('SALES REPORT BY SEGMENT', color ='red')

plt.xticks(segments)
plt.tight_layout()
plt.show()
