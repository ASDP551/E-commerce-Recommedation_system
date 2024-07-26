
import pandas as pd
import numpy as np

# Sample data (replace with your actual data)
data = {'user_id': [21, 31, 42, 532, 63],
        'product_id': [3410, 3510, 3610, 6347, 987],
        'rating': [5, 4, 3, 5, 2]}
df = pd.DataFrame(data)

# Create user-item matrix
pivot_table = df.pivot_table(index='user_id', columns='product_id', values='rating')
