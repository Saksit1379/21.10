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


dx=[dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9,dt10,dt11]
dx2=pd.DataFrame(dx,index=["d1","d2","d3","d4","dt5","dt6","dt7","dt8","dt9","dt10","dt11"])

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

sex=st.radio(" Sex: 2 หญิง, 1 ชาย",(2, 1 ))
age=st.radio("อายุ: ",(1,2,3,))
year=st.radio("ระดับชั้นปี:",(1,2,3,4))
field=st.radio("คณะวิชา:",(1,2,3,4,5))
obje=st.radio("วัตถุประสงค์ในการเลือกซื้อคอมพิวเตอร์โน้ตบุ๊ค:",(1,2,3,4,5))
price=st.radio("ยี่ห้อคอมพิวเตอร์โน้ตบุ๊คที่เลือกซื้อ:",(1,2,3,4,5))
store=st.radio("ราคาเครื่องคอมพิวเตอร์โน้ตบุ๊ค:",(1,2,2,4,5))
pay=st.radio("ท่านเลือกซื้อคอมพิวเตอร์โน้ตบุ๊คจากที่ใด:",(1,2,2,4,5))
period=st.radio("ท่านเลือกชำระเงินในการซื้อคอมพิวเตอร์โน้ตบุ๊คอย่างไร:",(1,2))
motivation=st.radio("กรณีที่ซื้อเงินผ่อน ท่านต้องการผ่อนชำระกี่เดือน",(1,2,2,4,5))
income=st.radio("รายได้ของผู้ปกครอง: 1 ต่ำกว่า 15000 บาท ,2 15001-20000, 3 20001-25000, 4 25001-30000, 5 30000+",(1,2,2,4,5))

if st.button("ทำนายผล"):
   loaded_model = pickle.load(open('./data/wave_model.sav', 'rb'))
   input_data =  (sex,age,year,field,obje,price,store,pay,period,motivation,income)
   # changing the input_data to numpy array
   input_data_as_numpy_array = np.asarray(input_data)
   # reshape the array as we are predicting for one instance
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
   prediction = loaded_model.predict(input_data_reshaped)
   st.write(prediction)
   if prediction == 'Acer':
        st.image('./pic/AC.png')
   elif prediction == 'Asus':
        st.image('./pic/AS.png')
   elif prediction == 'Dell':
        st.image('./pic/DE.png')
   elif prediction == 'HP':
        st.image('./pic/HP.png')
   elif prediction == 'Lenovo':
            st.image('./pic/LE.png')
   else:
        st.image('./pic/MC.png')
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

