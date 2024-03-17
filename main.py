import streamlit as st
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


st.header("DasLicht")
text_input = [0, 0, 0, 0, 0]
text_input[1] = st.text_input("Введите длину помещения",placeholder="в метрах")
text_input[2] = st.text_input("Введите ширина помещения, placeholder="в метрах")
text_input[3] = st.text_input("Введите высоту стола",placeholder="в метрах")
text_input[4] = st.text_input("Введите показатель световой отдачи", placeholder="в люксах")
text_input[0] = st.text_input("Введите световой поток", placeholder="в люменах")


text_input[1] = text_input[1].replace(',', ".")
text_input[2] = text_input[2].replace(',', ".")
text_input[3] = text_input[3].replace(',', ".")
text_input[4] = text_input[4].replace(',', ".")
text_input[0] = text_input[0].replace(',', ".")

# ключевые показатели для нас разрабов): S - площадь помещения (м^2), A - длина помещения (м)
# B - ширина помещения (м), H - расстояние между потенциальным светильником и поверхностью,
# на которую падает свет (м), F - показатель световой отдачи или тип и мощность лампы 
#E = (η * F) / S # расчитывает освещенность
#N= E * S *k/ f # кол-во светильников
#i=S/(h - h1)*(a + b) #индекс
button_pressed = st.button("Рассчитать освещенность и количество светильников")
 

if button_pressed:
        if is_number(text_input[1]) and is_number(text_input[2]) and is_number(text_input[3]) and is_number(text_input[4]):
            s = float(text_input[2]) * float(text_input[1])
            # i = s / (float(text_input[3])) * (float(text_input[2]) + float(text_input[1]))
            e = float(text_input[4])
            f = float(text_input[0])
            n = 0
            if s <= 100 and float(text_input[3]) <= 2.7:
                n = (e * s * 2.5) / f
            else:
                n = (e * s * 3) / f
            st.text(f'Необходимая освещенность: {e}')
            st.text(f'Количество ламп: {round(n)}')
        else:
            st.error("Неверно введены данные")
