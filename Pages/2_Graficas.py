import streamlit as st
import pandas as pd
import plotly.express as px


URL="https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
dfIris= pd.read_csv(URL)

st.title("Visualización")

st.subheader(dfIris.columns[0])
fig = px.box(dfIris, y=dfIris.columns[0])
st.plotly_chart(fig,use_container_width=True)

st.subheader(dfIris.columns[1])
fig = px.box(dfIris, y=dfIris.columns[1])
st.plotly_chart(fig,use_container_width=True)

st.subheader(dfIris.columns[2])
fig = px.box(dfIris, y=dfIris.columns[2])
st.plotly_chart(fig,use_container_width=True)

st.subheader(dfIris.columns[3])
fig = px.box(dfIris, y=dfIris.columns[3])
st.plotly_chart(fig,use_container_width=True)
