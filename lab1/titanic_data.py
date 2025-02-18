import statistics as sts
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def titanic_start():
    # 6. Прочитати набір даних катастрофи "Титаніка"
    # 7. Завантажити набір даних
    titanic_passengers = pd.read_csv('lab1/TitanicSurvival.csv')

    # 8. Переглянути рядки набору даних
    print(titanic_passengers.head())
    print(titanic_passengers.tail())

    # 9. Налаштувати назви стовпців
    titanic_passengers.columns = ['Name', 'Survived?', 'Sex', 'Age', 'Class']
    print(titanic_passengers.head())
    print(titanic_passengers.tail())

    # 10. Провести простий аналіз даних
    print(titanic_passengers['Age'].min())
    print(titanic_passengers['Age'].max())
    print(titanic_passengers['Age'].mean())

    titanic_survivors = titanic_passengers[(titanic_passengers['Survived?'] == 'yes')]
    print(titanic_survivors.describe())
    print(titanic_passengers['Survived?'].value_counts(dropna=False))

    titanic_women1 = titanic_passengers[(titanic_passengers['Sex'] == 'female')
                                        & (titanic_passengers['Class'] == '1st')]
    print(titanic_women1.head())
    print(titanic_women1.tail())
    print(titanic_women1['Age'].min())
    print(titanic_women1['Age'].max())
    print(titanic_women1['Survived?'].value_counts(dropna=False))

    # 11. Побудувати гістограму віку пасажирів
    titanic_passengers.hist('Age', bins=11, color='lightblue', edgecolor='black')
    plt.title('Розподіл вікових груп')
    plt.xlabel('Вік')
    plt.ylabel('Кількість пасажирів')
    plt.show()
