import streamlit as st

st.title('Theming with config.toml')

st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number: ', 0, 10, 5)
st.write('Selected number for slider widget is:', number)