import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

multitasking_data = pd.read_csv('experiment_1_data.csv', header = 1)

multitasking_data['Condition'] = np.where(multitasking_data.Block.str.contains("pure"), "Pure", None)

for i, row in multitasking_data.loc[multitasking_data['Block'] == "mixed",:].iterrows():
	if multitasking_data.loc[i - 1,'Task Type'] == multitasking_data.loc[i,'Task Type']:
		
		multitasking_data.loc[i,'Condition'] = "Mixed Repeat"
	else:
		multitasking_data.loc[i,'Condition'] = "Mixed Switch"

multitasking_data.describe()
sns.catplot(x='Congruent Trial', y='RT', hue = 'Sex', col = 'Condition', kind = 'bar', data=multitasking_data)
plt.savefig('RT barplot by condition, congruency and sex.png')
grouped_data = multitasking_data.groupby(['Condition', 'Congruent Trial', 'Sex']).aggregate(lambda x: ','.join(map(str, x)))
correct_percentage_by_condition_and_congruency = multitasking_data.groupby(['Condition','Congruent Trial', 'Sex'])['Correct Response'].apply(lambda x: np.sum(x)/len(x))
grouped_data["Errors (%)"] = (1 - correct_percentage_by_condition_and_congruency) * 100
grouped_data = grouped_data.reset_index()

sns.catplot(x='Congruent Trial', y='Errors (%)', hue = 'Sex', col = 'Condition', kind = 'bar', data=grouped_data)
plt.savefig('Barplot of percentage of errors by condition, congruency and sex.png')