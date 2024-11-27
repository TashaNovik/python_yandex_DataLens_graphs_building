import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
dataframe = pd.read_csv('train.csv', delimiter=',')

# Предобработка данных: создание столбца с комбинированным ключом
dataframe['Pclass_Sex'] = dataframe['Pclass'].astype(str) + '_' + dataframe['Sex']

# Группировка и агрегация
survived_counts = dataframe.groupby('Pclass_Sex')['Survived'].sum().reset_index()

# Разделение комбинированного ключа на отдельные столбцы
survived_counts[['Pclass', 'Sex']] = survived_counts['Pclass_Sex'].str.split('_', expand=True)
survived_counts = survived_counts.drop(columns=['Pclass_Sex'])

# Замена значений
survived_counts['Sex'] = survived_counts['Sex'].replace({'male': 'Мужской', 'female': 'Женский'})
survived_counts['Pclass'] = survived_counts['Pclass'].astype(int)

survived_counts = survived_counts.rename(columns={
    'Pclass': 'Класс каюты',
    'Sex': 'Пол',
    'Survived': 'Количество выживших пассажиров'  # Или "Количество выживших"
})

# Построение графика
plt.figure(figsize=(12, 6))
sns.barplot(x='Класс каюты', y='Количество выживших пассажиров', hue='Пол', data=survived_counts, dodge=True)

# Настройка графика
plt.title('Распределение выживших пассажиров по классу каюты и полу')
plt.xlabel('Класс каюты')
plt.ylabel('Количество выживших пассажиров')
plt.xticks(rotation=0)
plt.savefig("my_chart_seaborn.png")
plt.show()