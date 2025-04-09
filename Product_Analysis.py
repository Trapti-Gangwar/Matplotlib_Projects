import pandas as pd
import matplotlib.pyplot as plt

#2 Dataframes are given : sales_data, product_data
s_data = {
    "order_id": [101, 102, 103, 105, 106, 109, 107, 108],
    "product_id": [101,202, 101, 402, 202,401,102,301],
    "quantity": [2, 1, 3, 1, 2, 4, 1, 3],
    "revenue": [50.00, 25.50, 75.00, 25.00, 60.00, 102.00, 40.00, 75.00]
}

p_data =  {
    "product_id": [101, 102, 201, 202, 301, 302, 401, 402],
    "product_name": ["Laptop", "Mouse", "T-Shirt", "Jeans", "Coffee Maker", "Blender", "Notebook", "Pen"],
    "category": ["Electronics", "Electronics", "Apparel", "Apparel", "Home Goods", "Home Goods", "Stationery", "Stationery"]
}
sales_data = pd.DataFrame(s_data)
products_data = pd.DataFrame(p_data)

#Task1 : display highest revenue category with total revenue
merged = pd.merge(products_data,sales_data,on = 'product_id')
group1 = merged.groupby('category').agg(count=('order_id','count'),total=('revenue','sum'),average=('revenue','mean')).reset_index()
group1.sort_values(by = 'total',ascending = False,inplace = True)
print(group1.iloc[0,[0,1]])
print(group1)

#Task2: calculate avg revune per order , add new column then return df with specific columns
sales_data['Average_revenue_per_order'] = sales_data['revenue']/sales_data['quantity']
print(sales_data[['order_id','revenue','Average_revenue_per_order']])

#Task3 : plot bar chart for category vs total revenue , plot line chart for average revenue value of each category.
x = group1['category'].tolist()
y = group1['total'].tolist()
z = group1['average'].tolist()
plt.subplot(1,2,1)
plt.bar(x,y,width = 0.5,label='Total revenue',color = '#ADD8E6')
plt.plot(z,color='red',label='Average revenue') #plt.axhline(y="single value"), for list of values use plt.plot
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
#plot labels at line chart-
for i in range(len(x)):
    plt.text(i,z[i],z[i],ha='center',color='#00008B',fontweight = 'bold',fontsize=8)
plt.legend()

#Task4 : plot pie chart to show category vs order count
value = group1['count'].tolist()
color = ['#ADD8E6','#89CFF0','#B0E0E5','#6495ED']
explode = [0.02,0.02,0.02,0.02]
plt.subplot(1,2,2)
plt.pie(value,labels=x,colors = color,autopct = '%1.1f%%',explode=explode,
        wedgeprops={'edgecolor': '#000080'}, textprops={'fontsize': 8,'color':'k'})
plt.tight_layout()
plt.show()