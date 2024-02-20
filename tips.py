import streamlit as st
import pandas as pd
import numpy as np


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


from datetime import datetime, date, timedelta
st.write("""
# Tips Analysis app

This app provides analysis of tips in some random cafe

Data obtained from 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'.
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv)
""")

# Collects user input features into dataframe


df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
import random
df["time_order"]=df["day"].apply(lambda x: date.fromisoformat("2024-01-01") + timedelta(days=random.randint(0,30)))

st.write("""
##### График показывающий динамику чаевых во времени
""")
st.line_chart(df, x="time_order", y="tip")

st.write(""" ##### График показывающий динамику чаевых во времени""")
fig=plt.figure(figsize = (18, 8))
sns.histplot(df, x="total_bill", binwidth=2,kde=True)
st.pyplot(fig)

st.write("""
##### График показывающий связь между total_bill and tip
""")
fig2=plt.figure(figsize = (18, 8))

sns.scatterplot(df, x="total_bill", y="tip", hue="day", style="time")

st.pyplot(fig2)



st.write("""##### График, связывающий total_bill, tip, и size""")

df["tipas%total"]=df["tip"]/df["total_bill"]*100

fig3=plt.figure(figsize = (18, 8))
sns.barplot(df, x="size", y="tipas%total", hue="day")
st.pyplot(fig3)

st.write("""##### График связи между днем недели и размером счета""")
fig4=plt.figure(figsize = (18, 8))
sns.barplot(df, x="day", y="total_bill", hue="day")
st.pyplot(fig4)

st.write("""##### График показывающий связь между днями недели и чаевыми""")
fig41=plt.figure(figsize = (18, 8))
sns.scatterplot(df, x="tip", y="day", hue="sex")
st.pyplot(fig41)


dayz=dict(zip(df.groupby(["time_order"])["total_bill"].sum().index, df.groupby(["time_order"])["total_bill"].sum().to_list()))
df["sumbyday"]=df['time_order'].apply(lambda x:dayz[x])
st.write("""##### График показывающий ежедневную выручку за месяц""")
fig5=plt.figure(figsize = (18, 8))

dayz=dict(zip(df.groupby(["time_order"])["total_bill"].sum().index, df.groupby(["time_order"])["total_bill"].sum().to_list()))
df["sumbyday"]=df['time_order'].apply(lambda x:dayz[x])

sns.boxplot(df, x ="time", y ="sumbyday", hue="time")
st.pyplot(fig5)


st.write("""##### График показывающий динамику чаевых во времени""")
fig6=plt.figure(figsize = (18, 8))
plt.subplot(1,2,1)
plt.title("Lunch")
sns.histplot(df[df["time"]=="Lunch"],x="tip" )
plt.subplot(1,2,2)
plt.title("Dinner")
sns.histplot(df[df["time"]=="Dinner"],x="tip" )
st.pyplot(fig6)


st.write("""##### Графики (для мужчин и женщин), показывающие связь размера счета и чаевых, дополнительно разбив по курящим/некурящим""")
fig7=plt.figure(figsize = (18, 8))
plt.subplot(1,2,1)
plt.title("Male")
sns.scatterplot(df[df["sex"]=="Male"],x="total_bill",y="tip", hue="smoker" )
plt.subplot(1,2,2)
plt.title("Female")
sns.scatterplot(df[df["sex"]=="Female"],x="total_bill", y="tip", hue="smoker" )
st.pyplot(fig7)


st.write("""##### тепловую карту зависимостей численных переменных""")
fig8=plt.figure(figsize = (18, 8))


af=df.drop(["sex","smoker","day","time","tipas%total","sumbyday","time_order"], axis=1)
sns.heatmap(af.corr())
st.pyplot(fig8)