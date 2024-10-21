import streamlit as st

name = "Abu Bakar Software Wala"
desctiption = "Hi I'am Abu Bakar Software Wala A Frontend Web Developer"
button = "Hire Me"
image = "abz.jfif"
data = "abz12.mp4"
st.balloons()
st.title(name)
st.text(desctiption)
st.link_button(button, url="About")
st.video(data=data)