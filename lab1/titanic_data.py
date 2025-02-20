import csv

import matplotlib.pyplot as plt
import pandas as pd


def titanic_start():
    # 6. Прочитати набір даних катастрофи "Титаніка"
    # 7. Завантажити набір даних
    titanic_passengers = pd.read_csv('lab1/TitanicSurvival.csv')

    # 8. Переглянути рядки набору даних
    print("Переглядаємо набір даних")
    print(titanic_passengers.head())
    print(titanic_passengers.tail())

    # 9. Налаштувати назви стовпців
    print("Налаштування назв стовпців та перегляд набору даних")
    titanic_passengers.columns = ['Name', 'Survived?', 'Sex', 'Age', 'Class']
    print(titanic_passengers.head())
    print(titanic_passengers.tail())

    # 10. Провести простий аналіз даних
    print("Наймолодший пасажир")
    print(titanic_passengers['Age'].min())
    print("Найстарший пасажир")
    print(titanic_passengers['Age'].max())
    print("Середній вік пасажирів")
    print(titanic_passengers['Age'].mean())

    print("Статистика по пасажирам, які вижили")
    titanic_survivors = titanic_passengers[(titanic_passengers['Survived?'] == 'yes')]
    print(titanic_survivors.describe())
    print(titanic_passengers['Survived?'].value_counts(dropna=False))

    titanic_women1 = titanic_passengers[(titanic_passengers['Sex'] == 'female')
                                        & (titanic_passengers['Class'] == '1st')]
    print("Перегляд пасажирів: жінки з кают 1-го класу")
    print(titanic_women1.head())
    print(titanic_women1.tail())
    print("Наймолодша пасажирка з каюти 1-го класу")
    print(titanic_women1['Age'].min())
    print("Найстарша пасажирка з каюти 1-го класу")
    print(titanic_women1['Age'].max())
    print("Кількість пасажирок з каюти 1-го класу, які вижили")
    print(titanic_women1['Survived?'].value_counts(dropna=False))

    # 11. Побудувати гістограму віку пасажирів
    titanic_passengers.hist('Age', bins=11, color='lightblue', edgecolor='black')
    plt.title('Розподіл вікових груп')
    plt.xlabel('Вік')
    plt.ylabel('Кількість пасажирів')
    plt.show()
