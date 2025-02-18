import statistics as sts
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def start():
    print("Hello world")

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


    # 5. Для цих даних проробити всі дії з пункту колекції Series, DataFrame
    esi_series = pd.Series(esi)
    print(esi_series)

    print(pd.Series(esi_2025[0], range(4)))
    print(esi_series[0])

    print(esi_series.count()) # кількість елементів
    print(round(esi_series.mean(), 6)) # середнє (?)
    print(esi_series.min()) # мінімальне
    print(esi_series.max()) # максимальне
    print(round(esi_series.std(), 6)) # стандартне відхилення
    print(esi_series.describe())

    esi_year_series1 = pd.Series([esi_2020, esi_2021, esi_2022, esi_2023, esi_2024, esi_2025],
                                index=['2020', '2021', '2022', '2023', '2024', '2025'])
    print(esi_year_series1)

    esi_year_series2 = pd.Series({'Year_2020': esi_2020,
                                  'Year_2021': esi_2021,
                                  'Year_2022': esi_2022,
                                  'Year_2023': esi_2023,
                                  'Year_2024': esi_2024,
                                  'Year_2025': esi_2025})
    print(esi_year_series2)

    print(esi_year_series1['2020'])
    print(esi_year_series2.Year_2021)
    print(esi_year_series1.dtype)
    print(esi_year_series2.dtype)

    print(esi_series.values)

    # пропущені дії з рядками, бо в мене нема рядків у вибірці

    # 6. Прочитати набір даних катастрофи "Титаніка"
    # 7. Завантажити набір даних
    # 8. Переглянути рядки набору даних
    # 9. Налаштувати назви стовпців
    # 10. Провести простий аналіз даних
    # 11. Побудувати гістограму віку пасажирів
