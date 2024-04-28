import streamlit as st

# Initialize x with an initial value
if "x" not in st.session_state:
    st.session_state.x = 0

col1, col2, col3 = st.columns(3)

with col1:
    minus_btn = st.button("➖", type='primary')

with col2:
    st.header(st.session_state.x)

with col3:
    plus_btn = st.button("➕", type='primary')

# Update the value of x if the buttons are clicked
if minus_btn:
    st.session_state.x -= 1
    st.session_state.sync()

if plus_btn:
    st.session_state.x += 1
    st.session_state.sync()
