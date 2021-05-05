import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns

mutitasking_data = pd.read_csv('experiment_1_data.csv', header = 1)
mutitasking_data.head()
print(mutitasking_data.columns)

mutitasking_data.describe()
mutitasking_data["RT"].mean()
plt.hist(mutitasking_data['RT'], bins = 10)
plt.show()

