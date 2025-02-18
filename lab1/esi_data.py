import statistics as sts
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


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
    # додати перевірку з коду ймтасовіус
    print(f"Дисперсія = {round(sts.pvariance(esi), 6)}")
    print(f"Середньоквадратичне відхилення (ptsdev) = {round(sts.pstdev(esi), 6)}")
    print(f"Середньоквадратичне відхилення (sqrt(pvariance)) = {round(np.sqrt(sts.pvariance(esi)), 6)}")

    # 4. Гістограми для всіх можливих параметрів

    plt.hist(esi, color='lightgreen', edgecolor='black')
    plt.xlabel('ІЕН')
    plt.ylabel('')
    plt.title('ІЕН 2020-2025')
    plt.show()

    fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(6, 4), layout="constrained")
    axs[0, 0].hist(esi_2020, bins=5, color='lightgreen', edgecolor='black')
    axs[0, 0].title.set_text('2020')
    
    axs[0, 1].hist(esi_2021, bins=5, color='lightgreen', edgecolor='black')
    axs[0, 1].title.set_text('2021')
    
    axs[0, 2].hist(esi_2022, bins=5, color='lightgreen', edgecolor='black')
    axs[0, 2].title.set_text('2022')
    
    axs[1, 0].hist(esi_2023, bins=5, color='lightgreen', edgecolor='black')
    axs[1, 0].title.set_text('2023')
    
    axs[1, 1].hist(esi_2024, bins=5, color='lightgreen', edgecolor='black')
    axs[1, 1].title.set_text('2024')
    
    axs[1, 2].hist(esi_2025, bins=5, color='lightgreen', edgecolor='black')
    axs[1, 2].title.set_text('2025')
    
    fig.suptitle('ІЕН 2020-2025')
    plt.show()

    # 5. Для цих даних проробити всі дії з пункту колекції Series, DataFrame
    esi_series = pd.Series(esi)
    print(esi_series)
    print()

    print(pd.Series(esi_2025[0], range(4)))
    print()
    print(esi_series[0])
    print()

    print(esi_series.count()) # кількість елементів
    print(round(esi_series.mean(), 6)) # середнє (?)
    print(esi_series.min()) # мінімальне
    print(esi_series.max()) # максимальне
    print(round(esi_series.std(), 6)) # стандартне відхилення
    print(esi_series.describe())

    print()

    esi_year_series1 = pd.Series([esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025],
                                 index=['2020', '2021', '2022', '2023', '2024', '2025'])
    print(esi_year_series1)
    print()

    esi_year_series2 = pd.Series({'Year_2020': esi_2020,
                                  'Year_2021': esi_2021,
                                  'Year_2022': esi_2022,
                                  'Year_2023': esi_2023,
                                  'Year_2024': esi_2024,
                                  'Year_2025': esi_2025})
    print(esi_year_series2)
    print()

    print(esi_year_series1['2020'])
    print()
    print(esi_year_series2.Year_2021)
    print()
    print(esi_year_series1.dtype)
    print()
    print(esi_year_series2.dtype)
    print()

    print(esi_series.values)
    print()

    # пропущені дії з рядками, бо в мене нема рядків у вибірці

    esi_dict = {'2020': esi_2020,
                '2021': esi_2021,
                '2022': esi_2022,
                '2023': esi_2023,
                '2024': esi_2024}
    esi_df = pd.DataFrame(esi_dict)
    print(esi_df)
    print()

    esi_df.index = ['Квартал 1', 'Квартал 2', 'Квартал 3', 'Квартал 4']
    print(esi_df)
    print()

    print(esi_df['2020'])
    print()
    print(esi_df.loc['Квартал 1'])
    print()
    print(esi_df.iloc[0])
    print()
    print(esi_df.loc['Квартал 1':'Квартал 3'])
    print()
    print(esi_df.iloc[0:2])
    print()
    print(esi_df.loc[['Квартал 1', 'Квартал 3']])
    print()
    print(esi_df.iloc[[0, 2]])
    print()
    print(esi_df.loc['Квартал 1':'Квартал 3', ['2020', '2022']])
    print()
    print(esi_df.iloc[[0, 2], [0, 2]])
    print()
    print(esi_df[(esi_df >= 80) & (esi_df <= 100)])
    print()
    print(esi_df.at['Квартал 3', '2024'])
    print()
    print(esi_df.iat[2, 4])
    print()
    esi_df.at['Квартал 2', '2024'] = 100
    print(esi_df.at['Квартал 2', '2024'])
    print()
    esi_df.iat[1, 4] = 109.6
    print(esi_df.iat[1, 4])
    print()

    print(esi_df.describe())
    print()
    print(esi_df.mean())

    print(esi_df.T)
    print()
    print(esi_df.T.describe())
    print()
    print(esi_df.T.mean())
    print()

    print(esi_df.sort_index(ascending=False))
    print()
    print(esi_df.sort_index(axis=1))
    print()
    print(esi_df.sort_values(by='Квартал 2', axis=1, ascending=False))
    print()
    print(esi_df.loc['Квартал 2'].sort_values(ascending=False))
    print()
