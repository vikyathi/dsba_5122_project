import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("Superstore.csv", encoding='cp1252')
df['Order Date'] = pd.to_datetime(df["Order Date"], format='%m/%d/%Y')
df['OrderYear']=df['Order Date'].dt.year

shipment_sales = df.groupby(['Ship Mode', 'OrderYear'])['Sales'].sum().reset_index(name='sales')

chart = alt.Chart(shipment_sales).mark_line().encode(
    x= 'OrderYear',
    y= 'sales'
).properties(
    width = 300,
    height = 150
).facet(
    facet = 'Ship Mode',
    columns = 2
).resolve_scale(
    y='independent'
)
st.altair_chart(chart, use_container_width= False)