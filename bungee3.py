import pandas as pd
item3= pd.read_csv("main.csv")
item3 = item3[['Team', 'Yellow Cards', 'Red Cards']]

item3 = item3.groupby('Team').sum()
item3 = item3.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)