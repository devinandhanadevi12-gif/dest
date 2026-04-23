import pandas as pd

data = {
    'students': ["shruthu", "anu", "priya","sneha", "kavya","gopika", "sara", "nisha", "sindhu", "sree"],
    'marks': [50, 40, 45,30, 35, 25, 20, 15, 10, 5]
}
df = pd.DataFrame(data) 
print(df)

print(df.loc[0])
print(df.loc[4])