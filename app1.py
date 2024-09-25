import streamlit as st
# Create a text input box
text_input = st.text_input("Enter some text:")
# Create a submit button
if st.button("Submit"):
    t.write("You've inputted:", text_input)
