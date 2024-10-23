import streamlit as st
import pandas as pd
from PIL import Image
import pickle

model = pickle.load(open('GradientBoostingRegressor.pkl', 'rb'))

def run():
    st.title("Welcome to MediInsurance, Predicting Your Medical Expenses")
    img = Image.open('medi_image.jpg')
    st.image(img,  use_column_width=True)

    print()

    name = st.text_input("Enter your first name :")

    age = st.number_input("Enter your Age :", value = 0)

    sex_display = ('Female', 'Male')
    sex_options = list(range(len(sex_display)))
    sex = st.selectbox("Sex :", sex_options, format_func=lambda x: sex_display[x])

    bmi = st.number_input("Enter your BMI value :",value = 0.0)

    children_diaplay = ('0', '1', '2', '3', '4', '5+')
    children_options = list(range(len(children_diaplay)))
    children = st.selectbox("If you have children, How many you have? ", children_options, format_func=lambda x: children_diaplay[x])

    smoker_display = ('No', 'Yes')
    smoker_options = list(range(len(smoker_display)))
    smoker = st.selectbox("Snoking Status :", smoker_options, format_func=lambda x: smoker_display[x])

    region_display = ('Southeast', 'southwest', 'northwest', 'northeast')
    region_options = list(range(len(region_display)))
    region = st.selectbox("Your Region :", region_options, format_func=lambda x: region_display[x])

    if st.button("Predict Your Insurance Cost"):

         features = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                    columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
         print(features)

         prediction = model.predict(features)

          # Extract the prediction from the array
         prediction_value = prediction[0]

         # Round the prediction value to 2 decimal places
         st.success(f"Hello {name}, your estimated insurance cost is $ {round(prediction_value, 0)}")

run()