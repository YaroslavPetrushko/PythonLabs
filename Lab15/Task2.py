import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot') 
plt.rcParams['figure.figsize'] = (15, 5) 

# Зчитування даних
fixed_df = pd.read_csv('data.csv', 
                       sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')

# Побудова графіка
fixed_df.plot(figsize=(15, 10))
plt.show()

# Іизначаємо сумарну кількість велосипедистів за всіма місцями
fixed_df['Total'] = fixed_df.sum(axis=1, numeric_only=True)

# Групуємо дані за місяцями та рахуємо загальну кількість велосипедистів за місяць
monthly_totals = fixed_df['Total'].resample('ME').sum()

# Знаходимо місяць з найбільшою кількістю велосипедистів
most_popular_month = monthly_totals.idxmax().strftime('%B')

print("Місяць з найбільшою кількістю велосипедистів:", most_popular_month)
