import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score

df = pd.read_csv('relevance_judgements.csv', sep=',')

print('Group 19 & 10: ', cohen_kappa_score(df['19'],df['10']))
print('Group 10 & 16: ', cohen_kappa_score(df['10'],df['16']))
print('Group 19 & 16: ', cohen_kappa_score(df['19'],df['16']))
print('Average      : ', np.mean([cohen_kappa_score(df['19'],df['10']),cohen_kappa_score(df['10'],df['16']),cohen_kappa_score(df['19'],df['16'])]))