import streamlit as st
from PIL import Image


st.set_page_config(page_title = "OkCupid Matchmaker")

image_welcome = Image.open('WelcomePage_OkCupid.png')

st.image(image_welcome)

st.write("This dataset is from the article: 'OkCupid Data for Introductory Statistics and Data Science Courses' of the authors Kim, Albert and Escobedo-Land, Adriana published on the Journal of Statistics Education, volume 23, month 07, year 2015, number 2 (doi = 10.1080/10691898.2015.11889737).")

st.sidebar.success("Select a page above!")

