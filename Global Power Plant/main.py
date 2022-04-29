import pandas as pd

data_frame = pd.read_csv('original_data/global_power_plant_database.csv', na_values=['NA'], dtype = {'other_fuel3': str})

print(data_frame.dtypes)