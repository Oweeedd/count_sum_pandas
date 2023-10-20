import pandas as pd


data = {'Дата': ['07.05.2022', '07.05.2022', '08.05.2022', '08.05.2022'],
        'Товар': ['Банан', 'Хлеб', 'Банан', 'Хлеб'],
        'Количество': [30, 10, 40, 8]}
def count_sum(df):

    result = df.groupby('Товар')['Количество'].sum().reset_index()
    result.set_index('Товар', inplace=True)
    return result

df = pd.DataFrame(data)
result_df = count_sum(df)

print(result_df)
