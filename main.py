import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

col1 , col2 , col3 = st.columns(3)


# Read JSON file

# a = {
#     'name':['sakshi','anjali'],
#     'age':[20,24],
#     'city':['Allahabad','Lucknow']    
# }
# st.write(a)

#read csv file
df = pd.read_csv("data.csv")
st.title("Data Visualization")
#st.write(df)

df1= df.drop(['ID','Qty','Category','UnitPrice','TotalPrice'],axis=1)
st.write(df1)


if st.sidebar.button('load dataset'):
    st.write(df)
    
if st.sidebar.button('load Description'):
    st.write(df.describe())
    
if st.sidebar.button('load Chart'):
    df2 = df.head(20)
    
    fig=plt.figure(figsize=(10,8))
    plt.bar(df2['Country'],df2['Product'])
    st.pyplot(fig)
    
    

col1.metric("Year",'2023','2022')
col2.metric("Country",'$4301','$4200')
col3.metric("Prouct",'$4301','$4200')
