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
