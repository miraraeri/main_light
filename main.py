import streamlit as st
st.title('Наш новый проект')
flag = False
button_pressed = st.button("Рассчитать возможность получения займа")
if button_pressed:
  flag = not flag
if flag:
  st.text('Исход 1')
else:
  st.text('Исход 2')
