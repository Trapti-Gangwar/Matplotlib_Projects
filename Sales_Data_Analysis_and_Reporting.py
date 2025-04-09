import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
#Sales Data Analysis and Reporting:
1.Industry: Retail, E-commerce, Manufacturing
2.Project Description:Analyze sales transaction data to identify trends, top-selling products, customer behavior, and regional performance. Generate insightful reports and visualizations to support business decision-making.
3.Potential Tasks:
    * Load and clean sales data from CSV or other formats using Pandas.
    * Calculate key metrics such as total sales, average order value, sales growth rate, and profit margins.
    * Group sales data by product category, region, customer segment, and time periods.
    * Visualize sales trends over time using line plots.
    * Compare sales performance across different categories or regions using bar charts.
    * Analyze customer purchasing patterns and identify popular product combinations.
    * Create scatter plots to explore relationships between variables like price and sales quantity.
    * Generate automated sales reports with key findings and visualizations.
4.Sample Dataset (Illustrative - you can find many more on Kaggle or other open data sources)
'''

data = {
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CustomerID': [101, 102, 101, 103, 102, 104, 101, 103, 105, 102],
    'OrderDate': ['2025-03-01', '2025-03-01', '2025-03-02', '2025-04-02', '2025-04-03', '2025-02-03', '2025-05-04', '2025-02-04', '2025-03-05', '2025-04-05'],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Home Goods', 'Clothing', 'Electronics', 'Books', 'Home Goods', 'Clothing', 'Electronics'],
    'ProductName': ['Laptop', 'T-Shirt', 'Mouse', 'Lamp', 'Jeans', 'Keyboard', 'Novel', 'Cushion', 'Socks', 'Monitor'],
    'Quantity': [1, 3, 2, 1, 1, 1, 5, 2, 4, 1],
    'UnitPrice': [1200, 25, 25, 75, 60, 75, 15, 20, 10, 300],
    'Region': ['North', 'South', 'North', 'East', 'South', 'West', 'North', 'East', 'West', 'South']}

df = pd.DataFrame(data)
df['sales'] = df['Quantity']*df['UnitPrice']
#Transforming and cleaning of data:
check_null=df.isna().sum() #this will give the count of null values in each column,thus we don't have null values in data
#KPIs -
total_sales=sum(df['Quantity']*df['UnitPrice'])
avg_ordercount= sum(df['Quantity'])//len(df['Quantity'])
#Gouped data -
g1 = df.groupby('ProductCategory').agg(sales=('sales','sum')) # sales by grouped on product category
g2= df.groupby('Region').agg(sales=('sales','sum'))           #sales by grouped on region
g3= df.groupby('CustomerID').agg(sales=('sales','sum'))       #sales by grouped on customerid
#convert date column in date format
df['OrderDate'] = pd.to_datetime(df['OrderDate']).dt.strftime('%Y-%m')
g4= df.groupby('OrderDate').agg(sales=('sales','sum'))  #sales by grouped on timeperiod YYYY-MM, month basis of same year

#Visualizations -
#Line plot ->to show trend of sales over timee
x1 = g4.index.tolist()
y1 = g4['sales'].sort_values(ascending=True).tolist()
plt.subplot(2,3,1)
plt.plot(x1,y1)
plt.title('Sales by dates',fontweight='bold',fontsize=7)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
for i in range(len(x1)):
    plt.text(i,y1[i],y1[i],ha='center',va='top',fontsize=6,color='red')
#bar charts for product categories
x2 = g1.index.tolist()
y2=g1['sales'].tolist()
plt.subplot(2,3,2)
plt.bar(x2,y2)
plt.title('Sales by product-categories',fontweight='bold',fontsize=7)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
for i in range(len(x2)):
    plt.text(i,y2[i],y2[i],ha='center',color='red',fontsize=6)

#bar chart for region
x3 = g2.index.tolist()
y3=g2['sales'].tolist()
plt.subplot(2,3,3)
plt.bar(x3,y3)
plt.title('Sales by region',fontweight='bold',fontsize=7)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
for i in range(len(x3)):
    plt.text(i,y3[i],y3[i],ha='center',fontsize=6,color='red')

#scatter plot price vs sales
x4=df['UnitPrice'].tolist()
y4= df['sales'].tolist()
plt.subplot(2,3,4)
plt.scatter(x4,y4)
plt.title('Sales vs unitprice',fontweight='bold',fontsize=7)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)

#group by customer
g5 = df.groupby('CustomerID').agg(total_sale=('sales','sum'))
x5 = g5.index.tolist()
y5= g5['total_sale'].tolist()
plt.subplot(2,3,5)
plt.bar(x5,y5,color='g')
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
for i in range(len(x5)):
    plt.text(i,y5[i],y5[i],ha='center',va='bottom',fontsize = 6,color='r')
plt.title('Customer vs sales',fontweight='bold',fontsize=7)

#pie char
g6 = df.groupby('ProductCategory').agg(cust=('CustomerID','count'))
x6 = g6.index.tolist()
y6 = g6['cust'].tolist()
plt.subplot(2,3,6)
plt.pie(y6,labels = x6,autopct = '%1.1f%%',textprops={'fontsize':6})
plt.legend(title='type',labels=x6,loc='upper right',fontsize=4, bbox_to_anchor=(1.3, 1.15))
plt.title("Product vs count",fontweight='bold',fontsize=7)

#for the whole subplot
plt.suptitle('Sales Analysis',fontweight='bold',fontsize=12,color='blue')
plt.tight_layout()
plt.show()