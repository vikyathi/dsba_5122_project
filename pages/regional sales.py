import streamlit as st
import altair as alt
import matplotlib
matplotlib.use( 'tkagg' )
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

st.header("Region sales of the Superstore")
st.markdown("As per the total region sales and region sales over the time period 2014 to 2017, West Region has the largest sales and relatively maintained the highest number of sales every year")

df = pd.read_csv("Superstore.csv", encoding='cp1252')
df['Order Date'] = pd.to_datetime(df["Order Date"], format='%m/%d/%Y')
df['OrderYear']=df['Order Date'].dt.year

region = st.sidebar.selectbox('Select Region',
  ['All','Central', 'East', 'South', 'West'])
region_sales = df.groupby(['Region'])['Sales'].sum().reset_index(name='region sales')
sales_over_time = df.groupby(['OrderYear', 'Region']).agg({'Sales':'sum'}).reset_index()

col1, col2 = st.columns(2)
with col1:
    fig1 = px.pie(
    data_frame= region_sales,
    names = 'Region',
    values = 'region sales',
    title='Total Region Sales',
    hole = 0.2,
    height= 400,
    width= 350
    )
    st.plotly_chart(fig1)
with col2:
    st.text("")
    st.text("")
    line_chart = alt.Chart(sales_over_time).mark_line().encode(
    x='OrderYear',
    y='Sales',
    color = 'Region'
    ).properties(
        height = 300,
        width = 450,
        title = 'Region sales over the time period'
    )
    st.altair_chart(line_chart, use_container_width=False)

