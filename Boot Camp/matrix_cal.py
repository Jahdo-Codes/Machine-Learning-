import streamlit as st
import numpy as np

st.title('Matrix Calculator')
st.subheader('Enter your dimensions & desired outcome')

st.selectbox("What option would you like to on your matrices?",('Addition','Subtraction','Multiplication'))
