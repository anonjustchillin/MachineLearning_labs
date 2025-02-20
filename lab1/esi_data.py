import statistics as sts
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def esi_plot(esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025):
    years = ['2020', '2021', '2022', '2023', '2024', '2025']
    quarter = ['Квартал 1', 'Квартал 2', 'Квартал 3', 'Квартал 4']
    esi_mean = [round(sts.mean(esi_2020), 6),
                round(sts.mean(esi_2021), 6),
                round(sts.mean(esi_2022), 6),
                round(sts.mean(esi_2023), 6),
                round(sts.mean(esi_2024), 6),
                round(sts.mean(esi_2025), 6)]

    # гістограма 1. середні значення ІЕН
    plt.bar(years, esi_mean, color='lightgreen', edgecolor='black')
    plt.xlabel('ІЕН (Середні значення)')
    plt.ylabel('')
    plt.title('ІЕН 2020-2025')
    plt.show()

    # гістограми 2. переглад ІЕН по кварталам з 2020 по 2025
    fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(12, 4), layout="constrained")
    axs[0, 0].bar(quarter, esi_2020, color='lightcoral', edgecolor='black')
    axs[0, 0].title.set_text('2020')

    axs[0, 1].bar(quarter, esi_2021, color='moccasin', edgecolor='black')
    axs[0, 1].title.set_text('2021')

    axs[0, 2].bar(quarter, esi_2022, color='yellowgreen', edgecolor='black')
    axs[0, 2].title.set_text('2022')

    axs[1, 0].bar(quarter, esi_2023, color='powderblue', edgecolor='black')
    axs[1, 0].title.set_text('2023')

    axs[1, 1].bar(quarter, esi_2024, color='lavender', edgecolor='black')
    axs[1, 1].title.set_text('2024')

    axs[1, 2].bar(quarter[0], esi_2025, color='pink', edgecolor='black')
    axs[1, 2].title.set_text('2025')

    fig.suptitle('ІЕН 2020-2025')
    plt.show()


def esi_series_func(esi, esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025):
    print("Створення ІЕН як Series")
    esi_series = pd.Series(esi)
    print(esi_series)
    print()

    print("Створення Series з однаковими значеннями esi_2025[0]")
    print(pd.Series(esi_2025[0], range(4)))
    print()

    print("Звернення до елемента в Series")
    print(esi_series[0])
    print()

    print("Кількість елементів у Series")
    print(esi_series.count()) # кількість елементів
    print("Середнє значення у Series")
    print(round(esi_series.mean(), 6)) # середнє
    print("Мінімальне значення у Series")
    print(esi_series.min()) # мінімальне
    print("Максимальне значення у Series")
    print(esi_series.max()) # максимальне
    print("Стандартне відхилення у Series")
    print(round(esi_series.std(), 6)) # стандартне відхилення
    print("Статистика по ІЕН як Series")
    print(esi_series.describe())

    print()

    print("Створення ІЕН як Series з нестандартними індексами")
    esi_year_series1 = pd.Series([esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025],
                                 index=['2020', '2021', '2022', '2023', '2024', '2025'])
    print(esi_year_series1)
    print()

    print("Створення ІЕН як Series за допомогою словника")
    esi_year_series2 = pd.Series({'Year_2020': esi_2020,
                                  'Year_2021': esi_2021,
                                  'Year_2022': esi_2022,
                                  'Year_2023': esi_2023,
                                  'Year_2024': esi_2024,
                                  'Year_2025': esi_2025})
    print(esi_year_series2)
    print()

    print("Звернення до елемента Series з нестандартними індексами")
    print(esi_year_series1['2020'])
    print()
    print("Інший спосіб звернення, якщо індекс є рядком")
    print(esi_year_series2.Year_2021)
    print()
    print("Переглядаємо тип елементів Series")
    print(esi_year_series1.dtype)
    print()
    print("Переглядаємо тип елементів Series (ініціалізатор -- словник)")
    print(esi_year_series2.dtype)
    print()

    print("Переглядаємо базову колекцію Series")
    print(esi_series.values)
    print()

    # пропущені дії з рядками, бо в мене нема рядків у вибірці


def esi_df_func(esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025):
    print("Створення ІЕН як Data Frame на базі словника")
    esi_dict = {'2020': esi_2020,
                '2021': esi_2021,
                '2022': esi_2022,
                '2023': esi_2023,
                '2024': esi_2024,
                '2025': [esi_2025[0], pd.NA, pd.NA, pd.NA]}
    esi_df = pd.DataFrame(esi_dict)
    print(esi_df)
    print()

    print("Налаштування індексів Data Frame")
    esi_df.index = ['Квартал 1', 'Квартал 2', 'Квартал 3', 'Квартал 4']
    print(esi_df)
    print()

    print("Звернення до стовпця Data Frame")
    print(esi_df['2020'])
    print()
    print("Вибір рядка Data Frame (loc['Квартал 1'])")
    print(esi_df.loc['Квартал 1'])
    print()
    print("Вибір рядка Data Frame (iloc[0])")
    print(esi_df.iloc[0])
    print()
    print("Вибір сегмента Data Frame (loc['Квартал 1':'Квартал 3'])")
    print(esi_df.loc['Квартал 1':'Квартал 3'])
    print()
    print("Вибір сегмента Data Frame (iloc[0:2])")
    print(esi_df.iloc[0:2])
    print()
    print("Вибір сегмента Data Frame (loc[['Квартал 1', 'Квартал 3'])")
    print(esi_df.loc[['Квартал 1', 'Квартал 3']])
    print()
    print("Вибір сегмента Data Frame (iloc[[0, 2]])")
    print(esi_df.iloc[[0, 2]])
    print()
    print("Вибір підмножини рядків та стовпців Data Frame (loc['Квартал 1':'Квартал 3', ['2020', '2022']])")
    print(esi_df.loc['Квартал 1':'Квартал 3', ['2020', '2022']])
    print()
    print("Вибір підмножини рядків та стовпців Data Frame (iloc[[0, 2], [0, 2]])")
    print(esi_df.iloc[[0, 2], [0, 2]])
    print()
    print("Логічне індексування Data Frame")
    print(esi_df[(esi_df <= 80) | (esi_df >= 100)])
    print()
    print("Вибір конкретного осередку Data Frame по рядку і стовпцю (at)")
    print(esi_df.at['Квартал 3', '2024'])
    print()
    print("Вибір конкретного осередку Data Frame по індексам рядка і стовпця (iat)")
    print(esi_df.iat[2, 4])
    print()
    print("Присвоєння конкретного значення Data Frame (at)")
    esi_df.at['Квартал 2', '2024'] = 100
    print(esi_df.at['Квартал 2', '2024'])
    print()
    print("Присвоєння конкретного значення Data Frame (iat)")
    esi_df.iat[1, 4] = 109.6
    print(esi_df.iat[1, 4])
    print()

    print("Описова статистика Data Frame")
    print(esi_df.describe())
    print()
    print("Математичне сподівання Data Frame")
    print(esi_df.mean())
    print()

    print("Транспонування Data Frame")
    print(esi_df.T)
    print()
    print("Описова статистика транспонованої Data Frame")
    print(esi_df.T.describe())
    print()
    print("Математичне сподівання транспонованої Data Frame")
    print(esi_df.T.mean())
    print()

    print("Сортування рядків за індексами Data Frame")
    print(esi_df.sort_index(ascending=False))
    print()
    print("Сортування за індексами стовпців Data Frame")
    print(esi_df.sort_index(axis=1))
    print()
    print("Сортування за значеннями стовпців індексами")
    print(esi_df.sort_values(by='Квартал 2', axis=1, ascending=False))
    print()
    print("Об'єднання операції вибору (loc) із сортуванням Data Frame")
    print(esi_df.loc['Квартал 2'].sort_values(ascending=False))
    print()


def esi_start():
    # 1. Обрати дані із сайта
    # 2. Первинна обробка даних
    esi_2020 = [112.4, 87.8, 94.5, 97.5]
    esi_2021 = [92.8, 106.2, 109.7, 105.8]
    esi_2022 = [106.9, 74.3, 81.4, 92.1]
    esi_2023 = [93.6, 106.9, 107.1, 104.2]
    esi_2024 = [102.7, 109.6, 105.1, 103.4]
    esi_2025 = [106.1]
    esi = esi_2020 + esi_2021 + esi_2022 + esi_2023 + esi_2024 + esi_2025
    print("Вибірка\n", esi)

    # 3. Мат. сподівання, медіана, мода, дисперсія, середньоквадратичне відхилення
    print(f"Математичне сподівання = {round(sts.mean(esi), 6)}")
    print(f"Медіана = {sts.median(esi)}")
    print(f"Мода = {sts.mode(esi)}")
    print(f"Дисперсія = {round(sts.pvariance(esi), 6)}")
    print(f"Середньоквадратичне відхилення (ptsdev) = {round(sts.pstdev(esi), 6)}")
    print(f"Середньоквадратичне відхилення (sqrt(pvariance)) = {round(np.sqrt(sts.pvariance(esi)), 6)}")

    # 4. Гістограми для всіх можливих параметрів
    esi_plot(esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025)

    # 5. Для цих даних проробити всі дії з пункту колекції Series, DataFrame
    esi_series_func(esi, esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025)
    esi_df_func(esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025)
