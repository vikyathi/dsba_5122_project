import streamlit as st
import altair as alt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

st.header("Sales and Profits of each Category")
st.markdown("Based on the catogory and sub category, Furniture had most sales and profit over the time and In Furniture chairs had most sales and profit")

df = pd.read_csv("Superstore.csv", encoding='cp1252')
df['Order Date'] = pd.to_datetime(df["Order Date"], format='%m/%d/%Y')
df['OrderYear']=df['Order Date'].dt.year

selected_category = st.sidebar.selectbox('Select category',
  ['Furniture','Office Supplies', 'Technology'])

sub_category_sales = df.groupby(['Sub-Category', 'Category'])['Sales'].sum().reset_index(name='sales')
sub_category_profit = df.groupby(['Sub-Category', 'Category'])['Profit'].sum().reset_index(name='profit')

tab1, tab2, tab3, tab4 = st.tabs(['Category Sales', 'Category Profit',
                'Sub Category Sales','Sub Category Profits'])

with tab1:
    category_sales = df.groupby(['OrderYear', 'Category']).agg({'Sales':'sum'}).reset_index()
    line_chart = alt.Chart(category_sales).mark_line().encode(
        x='OrderYear:Q',
        y='Sales',
        color = 'Category'
    ).properties(
        height = 300
    )
    st.altair_chart(line_chart, use_container_width=True)

with tab2:
    category_profit = df.groupby(['OrderYear', 'Category']).agg({'Profit':'sum'}).reset_index()
    line_chart = alt.Chart(category_profit).mark_line().encode(
        x='OrderYear:Q',
        y='Profit',
        color = 'Category'
    ).properties(
        height = 300
    )
    st.altair_chart(line_chart, use_container_width=True)

with tab3:
    st.caption("Select a category from the drop down to view sales of sub category")
    sales_chart = alt.Chart(sub_category_sales).mark_bar().encode(
    alt.X(field='Sub-Category', type='nominal', sort= '-y'),
    y='sales',
    color = 'sales'
    ).transform_filter(
        alt.FieldEqualPredicate(field='Category', equal= selected_category)
    )
    st.altair_chart(sales_chart, use_container_width=True)

with tab4:
    st.caption("Select a category from the drop down to view profts of sub category")
    profit_chart = alt.Chart(sub_category_profit).mark_bar().encode(
    alt.X(field='Sub-Category', type='nominal', sort= '-y'),
    y='profit',
    color = 'profit'
    ).transform_filter(
        alt.FieldEqualPredicate(field='Category', equal= selected_category)
    )
    st.altair_chart(profit_chart, use_container_width=True)


