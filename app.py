import streamlit as st

# Заголовок приложения
st.title("🎨 Простое демо приложение")
st.write("Это пример интерактивного приложения на Streamlit")

# Боковая панель
st.sidebar.header("Настройки")
name = st.sidebar.text_input("Введите ваше имя:", "Друг")

# Выбор цвета
color = st.sidebar.selectbox(
    "Выберите любимый цвет:",
    ["Красный", "Синий", "Зеленый", "Желтый", "Фиолетовый"]
)

# Слайдер
age = st.sidebar.slider("Выберите возраст:", 1, 100, 25)

# Основной контент
st.header(f"Привет, {name}! 👋")
st.write(f"Твой любимый цвет: **{color}**")
st.write(f"Возраст: **{age}** лет")

# Кнопка
if st.button("Нажми меня!"):
    st.balloons()
    st.success(f"Отлично, {name}! Ты выбрал {color} цвет! 🎉")

# График
st.subheader("Простой график")
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Информация
st.info("💡 Это простое приложение для демонстрации возможностей Streamlit")
