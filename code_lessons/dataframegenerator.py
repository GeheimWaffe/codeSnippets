import random

import pandas as pd
import numpy as np
def generate_dataframe_1() -> pd.DataFrame:
    size = 20
    categories = ['Mer', 'Montagne', 'Campagne']
    category = [categories[i % 3] for i in range(size)]
    col1 = [random.random()*i for i in range(size)]
    col2 = [i**2 for i in range(size)]
    col3 = [np.sqrt(i) for i in range(size)]
    values = zip(categories, col1, col2, col3)
    df = pd.DataFrame(values, columns=['Lieu', 'Temperature', 'Pressure', 'Wind'])
    return df