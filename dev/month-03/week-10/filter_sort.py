import pandas as pd

pop = pd.read_csv('data/raw/ward_population.csv')

big = pop[pop['population_2024'] > 30000]
print(big)