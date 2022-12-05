import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

st.header('Superstore Dataset')
df = pd.read_csv("Superstore.csv", encoding='cp1252')
df['Order Date'] = pd.to_datetime(df["Order Date"], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df["Ship Date"]).dt.date
st.write(df.head())

sales = int(df['Sales'].sum())
profit = int(df['Profit'].sum())
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", "$"+ str(sales))
col2.metric("Total Profit", "$"+ str(profit))
col3.metric("Profit ratio", round(sales/profit,2))

category_df = df.groupby(['Category'])['Category'].count().reset_index(name='counts')
category_sales = df.groupby(['Category'])['Sales'].sum().reset_index(name='category sales')
category_profit = df.groupby(['Category'])['Profit'].sum().reset_index(name='category profit')


category_selected = st.sidebar.selectbox('Select category',
  ['Most popular category','Category sales', 'Category profit'])

if category_selected == 'Most popular category':
    dataframe = category_df
    x_axis = 'counts'
elif category_selected == 'Category sales':
    dataframe = category_sales
    x_axis = 'category sales'
else:
    dataframe = category_profit
    x_axis = 'category profit'

bar_plot = alt.Chart(dataframe).mark_bar().encode(
    x=x_axis,
    y=alt.Y('Category', sort='-x'),
    color = x_axis
).properties(
    height = 150
)
st.altair_chart(bar_plot, use_container_width=True)





