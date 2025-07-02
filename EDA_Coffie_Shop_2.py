import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =  pd.read_excel('data.xlsx')

c1 = ['#AB0012','#1C1919']
c2 = ['#F4E4C3','#E2572C']
c3 = ['#FEC700','#02462E']
colors = ['#FF6B6B', '#FFD93D', '#6BCB77', '#4D96FF',
          '#845EC2', '#FF9671', '#2C3E50', '#00C9A7']
c7 = ['#FF6B6B', '#FFD93D', '#6BCB77', '#4D96FF',
          '#845EC2', '#FF9671', '#2C3E50']
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())

df.drop('card',axis=1,inplace=True)
df['date'] = pd.to_datetime(df['date'])
df['datetime'] = pd.to_datetime(df['datetime']).dt.time
df['day'] = df['date'].dt.day_name()
top5 = df['coffee_name'].value_counts().sort_values(ascending=False).head(5)
plt.figure(figsize=(10,10))
plt.bar(top5.index,top5.values,color=['#AB0012','#1C1919','#F4E4C3','#E2572C','#FEC700'])
plt.title('Top 5 Coffees Sold This Month')
plt.xlabel('Coffee Name')
plt.ylabel('Units Sold')
plt.grid(True,ls='--',lw='0.5')
plt.savefig('Top 5 coffees.png')
plt.show()
dstb_mon = df.groupby('coffee_name')['money'].sum().sort_values(ascending=False)
top_5_mon =  dstb_mon.head(5)
plt.figure(figsize=(10,10))
plt.bar(top_5_mon.index,top_5_mon.values,color=['#1C1919','#AB0012','#F4E4C3','#FEC700','#E2572C'])
plt.title('Top 5 Coffees Sold This Month By Revenue')
plt.xlabel('Coffee Name')
plt.ylabel('Reveue Made')
plt.grid(True,ls='--',lw='0.5')
plt.savefig('Top 5 coffees by Revenue.png')
plt.show()
revenue_dstb = dstb_mon
lab_rd = revenue_dstb.index
ex = [0.1,0,0,0,0,0,0,0.1]
plt.figure(figsize=(10,10))
plt.pie(revenue_dstb, labels=lab_rd,autopct='%1.1f%%',colors=colors,explode=ex)
plt.title('Total Revenue Distribution')
plt.legend(loc='lower left')
plt.savefig('Total Revenue Distribution.png')
plt.show()
daily_sales_coffee = pd.pivot_table(data=df,index='date',columns='coffee_name',values='money',aggfunc='sum')
daily_sales = df.groupby('date')['money'].sum()
plt.figure(figsize=(10,10))
plt.plot(daily_sales.index,daily_sales.values)
plt.title('Daily Revenue Over the Last Year')
plt.xlabel('Date')
plt.ylabel('Revenue Made')
plt.grid(True,ls='--',lw='0.5')
plt.savefig('Daily Revenue Over the Last Year.png')
plt.show()
revenue_day = df.groupby('day')['money'].sum()
sale_daily = df.groupby('day')['coffee_name'].count()
plt.figure(figsize=(10,10))
plt.plot(revenue_day.index,revenue_day.values,marker='o')
plt.title('Revenue By Day')
plt.xlabel('Day')
plt.ylabel('Revenue Made')
plt.grid(True,ls='--',lw='0.5')
plt.savefig('Daily Revenue.png')
plt.show()
plt.figure(figsize=(10,10))
plt.plot(sale_daily.index,sale_daily.values,marker='o')
plt.title('Sales By Day')
plt.xlabel('Day')
plt.ylabel('Sales Made')
plt.grid(True,ls='--',lw='0.5')
plt.savefig('Daily sales.png')
plt.show()
coffee_n_payment = df.groupby('coffee_name')['cash_type'].value_counts()
print(df)
print(coffee_n_payment)
df.to_excel('new data.xlsx')