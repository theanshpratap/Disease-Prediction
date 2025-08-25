import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration
st.set_page_config(page_title="Health Assitant",layout="wide")


# set the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))


# loading of the saved model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))


#sidebar for navigation
with st.sidebar:
	selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'], menu_icon='hospital-fill',icons=['activity','heart'],default_index=0)

if selected == 'Diabetes Prediction':
	st.title('Diabetes Prediction Using ML')
	col1,col2,col3 = st.columns(3)

	glucose = col1.slider('Glucose Level',0,600,120)
	bloodpressure = col2.slider('Blood Pressure Value',0,200,80)
	skinthickness = col3.slider('Skin Thickness Value',0,100,20)
	insulin = col1.slider('Insulin Level',0,500,30)
	bmi = col2.slider('BMI Value',0.0,70.0,25.0)
	dpf = col3.slider('Diabetes Pedigree Function Value',0.0,2.5,0.5)
	age = col1.slider('Age of the Person',0,100,25)

	if st.button('Diabetes Test Result'):
		user_input = [glucose,bloodpressure,skinthickness,insulin,bmi,dpf,age]
		diab_prediction = diabetes_model.predict([user_input])
		diab_diagnosis = 'The Person is Diabetic' if diab_prediction[0] == 1 else 'The Person is not Diabetic'
		st.success(diab_diagnosis)


#heart
if selected == 'Heart Disease Prediction':
	st.title('!!!!! COMING SOON !!!!!')






