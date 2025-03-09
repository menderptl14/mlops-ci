import streamlit as st 

# streamlit ui

st.title("Power calculator")
st.write("Enter a number to calculate its swuare , cube and fifth power")

n = st.number_input("Enter an integer" , value=1,step=1)

# Display Result
square = n ** 2
cube = n**3
fifth_power = n**5

st.write(f"The square of {n} is : {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"the fifth power of {n} is :{fifth_power}")

