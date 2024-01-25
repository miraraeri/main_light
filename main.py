import streamlit as st
st.title('Супер мега крутой проект')
text_input = [0, 0, 0, 0, 0]
text_input[1] = st.text_input("Введите длину помещения", "Введите количество метров")
text_input[2] = st.text_input("Введите ширина помещения", "Введите количество метров")
text_input[3] = st.text_input(  "Введите расстояние между потенциальным светильником и поверхностью, на которую падает свет", 
  "Введите количество метров")
text_input[4] = st.text_input("Введите показатель световой отдачи", "Введите количество люксов")




# ключевые показатели для нас разрабов): S - площадь помещения (м^2), A - длина помещения (м)
# B - ширина помещения (м), H - расстояние между потенциальным светильником и поверхностью,
# на которую падает свет (м), F - показатель световой отдачи или тип и мощность лампы 
#E = (η * F) / S # расчитывает освещенность
#N=(E*S)/(U*Ф*Кз) # кол-во светильников
#i=S/(h - h1)*(a + b) #индекс
button_pressed = st.button("Рассчитать освещенность и количество светильников")
s = int(text_input[2]) * int(text_input[1])
i = s / (int(text_input[3])) * (int(text_input[2]) + int(text_input[1]))
e = (i * int(text_input[4])) / s
n=(e * s) / ( u * g * kz) 

if button_pressed:
        if text_input[1].isdigit() and text_input[2].isdigit() and text_input[3].isdigit() and text_input[4].isdigit():
          s = int(text_input[2]) * int(text_input[1])
          i = s / (int(text_input[3])) * (int(text_input[2]) + int(text_input[1]))
          e = (i * int(text_input[4])) / s
          n = (e * s) / ( u * g * kz) 
          print(s)
          print(e)
          print(n)
