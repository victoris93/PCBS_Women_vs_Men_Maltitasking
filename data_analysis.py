import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

multitasking_data = pd.read_csv('experiment_1_data.csv', header = 1)
multitasking_data.head()

sns.catplot(x='Congruent Trial', y='RT', hue = 'Sex', col = 'Block', kind = 'bar', data=multitasking_data) 
plt.show()

multitasking_data['Condition'] = np.where(multitasking_data.Block.str.contains("pure"), "Pure", None)

for i, row in multitasking_data.loc[multitasking_data['Block'] == "mixed",:].iterrows():
	if multitasking_data.loc[i - 1,'Task Type'] == multitasking_data.loc[i,'Task Type']:
		
		multitasking_data.loc[i,'Condition'] = "Mixed Repeat"
	else:
		multitasking_data.loc[i,'Condition'] = "Mixed Switch"
print(multitasking_data)	