import streamlit as st
from about_page import show_about_page
from predict_page import show_predict_page

st.title(":rainbow[Email Spam Prediction] 🤔")

aboutPage, predictPage = st.tabs([":orange[About]", ":green[Predict]"])

with aboutPage:
   show_about_page()

with predictPage:
   show_predict_page()