import streamlit as st
st.title('Супер мега крутой проект')
flag = False
button_pressed = st.button("Рассчитать возможность получения займа")
if button_pressed:
  flag = not flag
if flag:
  st.text('Исход 1сыршвсршыостошыв')
else:
  st.text('Исход 2мавировыиарыимиаым')
