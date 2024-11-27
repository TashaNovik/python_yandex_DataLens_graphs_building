import pandas as pd
import altair as alt

dataframe = pd.read_csv('train.csv', delimiter=',')
survives_counts = dataframe.groupby(['Pclass', 'Sex'])['Survived'].sum().reset_index()

survives_counts = survives_counts.rename(columns={
    'Pclass': 'Класс каюты',
    'Sex': 'Пол',
    'Survived': 'Количество выживших пассажиров'  # Или "Количество выживших"
})

survives_counts['Пол'] = survives_counts['Пол'].replace({'male': 'Мужской', 'female': 'Женский'})


chart = alt.Chart(survives_counts).mark_bar().encode(
    x='Пол:N',
    y='Количество выживших пассажиров:Q',
    color=alt.Color('Пол:N', scale=alt.Scale(range=['#00FF00', '#FFFF00'])),  # Ярко-зеленый и ярко - желтый
    column='Класс каюты:O'
).properties(
    title='Распределение выживших пассажиров по классу каюты и полу',
    width=200
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)

chart.save("my_chart_altair.png")





# chart = alt.Chart(survives_counts).mark_bar().encode(
#     x='Pclass:O',  # Класс каюты на оси X (O - ordinal, для категориальных данных)
#     y='Survived:Q',  # Количество выживших на оси Y (Q - quantitative)
#     color='Sex:N',  # Цвет столбцов по полу (N - nominal)
#     column='Sex:N'  # Группировка по полу в столбцах
# ).properties(
#     title='Распределение выживших пассажиров по классу каюты и полу',
#     width=200
# ).configure_axis(
#     grid=False  # Удаление сетки
# ).configure_view(
#     strokeWidth=0  # Удаление рамок
# )


