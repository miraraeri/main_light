import streamlit as st
st.title('Наш новый проект')
button_pressed = st.button("Рассчитать возможность получения займа")

if button_pressed:
  st.text('Исход 1')
else:
  st.text('Исход 2')
