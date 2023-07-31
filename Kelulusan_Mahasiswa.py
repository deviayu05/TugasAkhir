import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
from sklearn.ensemble import RandomForestClassifier

# tampilan web
st.write(""" 
# Classification of Student Graduation (Web Apps)
Web-based application for predicting (classifying) Graduation Timeliness of Informatics Engineering Students, UDINUS
""")

#img = Image.open('graduation.png')
#img = img.resize((500,500))
#st.image(img, use_column_width=False)

# Upload File Excel untuk parameter inputan
st.sidebar.header('Upload your Excel file')
upload_file = st.sidebar.file_uploader('')
if upload_file is not None:
    inputan = pd.read_excel(upload_file)
else:
    def input_user():
        st.sidebar.text('')
        st.sidebar.header('INPUTAN USER')

        col1, col2 = st.sidebar.columns(2)
        with col1:           
            gender = st.selectbox('Gender', ('0', '1'))
            st.caption('0 = Male 1 = Female')

        with col2:
            age = st.number_input('Age', value=0)
            st.caption('usia saat melakukan pendaftaran')

        with col1:
            pathways = st.selectbox('Pathways', ('0', '1'))
            st.caption('0 = PMDK, 1 = Reguler')

        col3, col4, col5 = st.sidebar.columns(3)
        with col3:        
            ips1 = st.number_input('IPS 1', min_value=0.00, max_value=4.00)
        with col4:
            ips2 = st.number_input('IPS 2', min_value=0.00, max_value=4.00)
        with col5:
            ips3 = st.number_input('IPS 3', min_value=0.00, max_value=4.00)
        with col3:
            ips4 = st.number_input('IPS 4', min_value=0.00, max_value=4.00)
        with col4:
            ips5 = st.number_input('IPS 5', min_value=0.00, max_value=4.00)
        with col5:
            ips6 = st.number_input('IPS 6', min_value=0.00, max_value=4.00)
        with col3:
            ips7 = st.number_input('IPS 7', min_value=0.00, max_value=4.00)
        with col4:
            ips8 = st.number_input('IPS 8', min_value=0.00, max_value=4.00)
        with col3:
            ips9 = st.number_input('IPS 9', min_value=0.00, max_value=4.00)
        with col4:
            ips10 = st.number_input('IPS 10', min_value=0.00, max_value=4.00)
        
        with col1:
            marital = st.selectbox('Marital', ('0', '1'))
            st.caption('0 = Not Married, 1 = Married')
        with col2:
            achievement = st.selectbox('Achievement', ('0', '1'))
            st.caption("0 = Have, 1 = Don't Have")

        data = {'gender' : gender,
                'age' : age,
                'pathways' : pathways,
                'ips1' : ips1,
                'ips2' : ips2,
                'ips3' : ips3,
                'ips4' : ips4,
                'ips5' : ips5,
                'ips6' : ips6,
                'ips7' : ips7,
                'ips8' : ips8,
                'ips9' : ips9,
                'ips10' : ips10,
                'marital' : marital,
                'achievement' : achievement}
        fitur = pd.DataFrame(data, index=[0])
        return fitur
    inputan = input_user()

# Menggabungkan input dan dataset
students_graduation_raw = pd.read_excel("studentsdata.xlsx")
students_graduation = students_graduation_raw.drop(columns=['graduation'])
df = pd.concat([inputan, students_graduation], axis=0)

# Menampilkan parameter hasil inputan
st.subheader('Parameter of Input')

if upload_file is not None:
    st.write(df)
else:
    st.write('Waiting for the excel file to upload..')
    st.write(df)

# Load save model
load_model = pickle.load(open('Graduation_Model.pkl', 'rb'))

# Terapkan Random Forest
prediction = load_model.predict(df)

#st.subheader('Class Label Description')
graduation = np.array(['ON TIME','LATE'])
#st.write(graduation)

st.subheader('''Prediction Results (Classification)''')
st.subheader('''Time of Student Graduation''')
st.write(graduation[prediction])