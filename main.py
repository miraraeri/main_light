import streamlit as st
st.title('Наш новый проект')
button_pressed = st.button("Рассчитать возможность получения займа")
flag = False
if button_pressed:
  flag = not flag
if flag:
  st.text('Исход 1')
else:
  st.text('Исход 2')
