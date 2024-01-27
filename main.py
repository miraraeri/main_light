import streamlit as st
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


st.header("DasLicht")
text_input = [0, 0, 0, 0, 0]
text_input[1] = st.text_input("Введите длину помещения", "Введите количество метров")
text_input[2] = st.text_input("Введите ширина помещения", "Введите количество метров")
text_input[3] = st.text_input(  "Введите расстояние между потенциальным светильником и поверхностью, на которую падает свет", 
  "Введите количество метров")
text_input[4] = st.text_input("Введите показатель световой отдачи", "Введите количество люксов")

text_input[1] = text_input[1].replace(',', ".")
text_input[2] = text_input[2].replace(',', ".")
text_input[3] = text_input[3].replace(',', ".")
text_input[4] = text_input[4].replace(',', ".")

# ключевые показатели для нас разрабов): S - площадь помещения (м^2), A - длина помещения (м)
# B - ширина помещения (м), H - расстояние между потенциальным светильником и поверхностью,
# на которую падает свет (м), F - показатель световой отдачи или тип и мощность лампы 
#E = (η * F) / S # расчитывает освещенность
#N=(E*S)/(U*Ф*Кз) # кол-во светильников
#i=S/(h - h1)*(a + b) #индекс
button_pressed = st.button("Рассчитать освещенность и количество светильников")
 

if button_pressed:
        if is_number(text_input[1]) and is_number(text_input[2]) and is_number(text_input[3]) and is_number(text_input[4]):
            s =float(text_input[2]) * float(text_input[1])
            i = s / (float(text_input[3])) * (float(text_input[2]) + float(text_input[1]))
            e = (i * float(text_input[4])) / s
            n = (e * s) / (1 * 345 * 1.1)
            st.text(f'Освещенность: {e}')
            st.text(f'Количество ламп: {n}')
        else:
            st.error("Неверно введены данные")
