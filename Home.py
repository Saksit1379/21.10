import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pickle

st.image('./pic/002.jpg')

html_8="""
<div style="background-color:#EE9513;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

dt=pd.read_csv("./data/Smote.csv")
st.write(dt.head(10))
dt1 = dt['sex'].sum()
dt2 = dt['age'].sum()
dt3 = dt['year_class'].sum()
dt4 = dt['field_of_study'].sum()
dt5 = dt['objective'].sum()
dt6 = dt['price'].sum()
dt7 = dt['store'].sum()
dt8 = dt['pay'].sum()
dt9 = dt['2_period'].sum()
dt10 = dt['motivation'].sum()
dt11 = dt['parent_income'].sum()
dt12 = dt['A1'].sum()
dt13 = dt['A2'].sum()
dt14 = dt['A3'].sum()
dt15 = dt['A4'].sum()
dt16 = dt['A5'].sum()
dt17 = dt['A6'].sum()
dt18 = dt['A7'].sum()
dt19 = dt['A8'].sum()
dt20 = dt['A9'].sum()
dt21 = dt['A10'].sum()
dt22 = dt['A11'].sum()
dt23 = dt['A12'].sum()
dt24 = dt['A13'].sum()
dt25 = dt['A14'].sum()
dt26 = dt['A15'].sum()
dt27 = dt['A16'].sum()
dt28 = dt['A17'].sum()
dt29 = dt['A18'].sum()
dt30 = dt['A19'].sum()
dt31 = dt['A20'].sum()

dx=[dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9,dt10,dt11,dt12,dt13,dt14,dt15,dt16,dt17,dt18,dt19,dt20,dt21,dt22,dt23,dt24,dt25,dt26,dt27,dt28,dt29,dt30]
dx2=pd.DataFrame(dx,index=["d1","d2","d3","d4","dt5","dt6","dt7","dt8","dt9","dt10","dt11","dt12","dt13","dt14","dt15","dt16","dt17","dt18","dt19","dt20","dt21","dt22","dt23","dt24","dt25","dt26","dt27","dt28","dt29","dt30"])

if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.area_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")
st.sidebar.markdown("# วิเคราห์รายบุคคล")

html_8="""
<div style="background-color:#EE9513;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

sex=st.radio("กรุณาเลือกข้อมูล Sex: 0 หญิง, 1 ชาย",(0, 1))
age=st.radio("กรุณาเลือกข้อมูล Sex: 0 หญิง, 1 ชาย",(1,2,2,4,5))


