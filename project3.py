import pandas as pd
import numpy as np

def handle_missing_income(data):
    
    skewness = data['income'].skew()
    print(f"Skewness of income: {skewness:.2f}")
    
    if abs(skewness) < 0.5:
       
        median_value = data['income'].median()
        data['income'].fillna(median_value, inplace=True)
        print("Missing values filled with median:", median_value)
    else:
    
        mode_value = data['income'].mode()[0]
        data['income'].fillna(mode_value, inplace=True)
        print("Missing values filled with mode:", mode_value)
    
    return data


df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'income': [50000, 60000, np.nan, 40000, np.nan]
})

print("Before handling missing values:")
print(df)


df = handle_missing_income(df)

print("\nAfter handling missing values:")
print(df)
