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

dt=pd.read_csv("./data/noteBookE2new.csv")
st.write(dt.head(10))
dt1 = dt['sex'].sum()
dt2 = dt['age'].sum()
dt3 = dt['year_class'].sum()
dt4 = dt['field_of_study'].sum()
dt5 = dt['objective'].sum()
dt6 = dt['price'].sum()
dt7 = dt['store'].sum()
dt8 = dt['motivation'].sum()
dt9 = dt['parent_income'].sum()


dx=[dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9]
dx2=pd.DataFrame(dx,index=["d1","d2","d3","d4","dt5","dt6","dt7","dt8","dt9"])

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

sex=st.radio(" Sex: 2 หญิง, 1 ชาย",(1,2))
age=st.radio("อายุ:1 <20, 2 20-25 , 3 >25 ",(1,2,3))
year_class=st.radio("ระดับชั้นปี: 1. ปี1 , 2. ปี2 3. ปี3  4. ปี4",(1,2,3,4))
field_of_study=st.radio("คณะวิชา: 1. คณะวิทยาศาสตร์และเทคโนโลยี 3.คณะวิทยาการจัดการ 4. คณะพยาบาลศาสตร์" ,(1,3,4,))
objective=st.radio("วัตถุประสงค์ในการเลือกซื้อคอมพิวเตอร์โน้ตบุ๊ค:1.เพื่อการศึกษา2.เพื่อใช้ติดต่อสื่อสาร3.เพื่อสร้างรายได้เสริม4.เพื่อเล่นเกม",(1,2,3,4,5))
price=st.radio("ราคาเครื่องคอมพิวเตอร์โน้ตบุ๊ค:1. <15000 2. 15001-20000 3. 20001-25000 4. 25001-30000 5. >30001",(1,2,3,4,5))
store=st.radio("ท่านเลือกซื้อคอมพิวเตอร์โน้ตบุ๊คจากที่ใด: 1. ร้านค้าคอมพิวเตอร์ทั่วไป 2. ร้านคอมพิวเตอร์ในศูนย์การค้า 3. ในห้างสรรพสินค้า 4. ร้านตัวแทนที่ได้รับการแต่งตั้งให้จำหน่ายยี่ห้ออย่างเป็นทางการ",(1,2,3,4))
motivation=st.radio("มูลเหตุจูงใจหรือบุคคลใดที่มีอิทธิพลต่อกำรตัดสินใจเลือกซื้อคอมพิวเตอร์โน้ตบุ๊คมากที่สุด : 1.บุคคลในครอบครัว 2. การโฆษณา 3. เพื่อน/ญาติ พี่น้อง 4. ตัดสินใจซื้อด้วยตัวเอง",(1,2,3,4))
parent_income=st.radio("รายได้ของผู้ปกครอง: 1 ต่ำกว่า 15000 บาท ,2 15001-20000, 3 20001-25000, 4 25001-30000, 5 30000+",(1,2,3,4,5))

if st.button("ทำนายผล"):
   loaded_model = pickle.load(open('./data/W_model.sav', 'rb'))
   input_data =  (sex,age,year_class,field_of_study,objective,price,store,motivation,parent_income)
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

