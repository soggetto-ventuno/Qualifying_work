import pandas as pd
from sklearn.preprocessing import StandardScaler


df = pd.DataFrame({
    'возраст': [25, 30, 35, 40],
    'зарплата': [50000, 75000, 100000, 120000],
    'опыт': [2, 5, 8, 12]
})

# до нормализации
print(df)


# После стандартизации
scaler = StandardScaler()
df_scaled = pd.DataFrame(
    scaler.fit_transform(df),
    columns=df.columns
)
print(df_scaled)
