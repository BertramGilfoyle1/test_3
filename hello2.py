import numpy as np
import pandas as pd

# a = np.array([1,2,3,4,5])
# b = np.array([6,7,8,9,10])

# c = np.column_stack((a,b))

# print(c)
row_1 = [3, 2, 1, 0]
row_2 = ['a', 'b', 'c', 'd']

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
df ={}
df.update(dict(zip(row_1, row_2)))
df = pd.DataFrame.from_dict(df, orient='index').reset_index()
print(df)

print(5269.0 == 5269)
