import streamlit as st
import random 
st.title("GUESSING GAME 1")
st.text("Are you ready to guess the number?")
#randomise guess
if 'Gnum' not in st.session_state:
    st.session_state.Gnum = random.randint(0,100)
#text
num = st.number_input("Guess the number", min_value=1, max_value=100)
#checking guess
def check_guess():
 if num ==st.session_state.Gnum:
    st.text("Congratulations! You guessed the correct number!")
    st.session_state.Gnum = random.randint(1, 100)
 elif num < st.session_state.Gnum:
    st.text("Try a higher number!")
 else: 
     st.text("Try a lower number!")
#button
st.button("Submit Guess", on_click=check_guess)