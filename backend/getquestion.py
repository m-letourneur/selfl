import os
import sys
import pandas as pd
import numpy as np

basedir = os.path.abspath(os.path.dirname(__file__))
df = pd.read_csv(basedir + '/../data/question_db.csv')
# print df.head()

dfc = df.copy()
dimension = len(dfc['score'])
# Consider the 30% of questions with the lowest grades
lg_dim = int(np.floor(0.5*dimension))
# print lg_dim
dfc = dfc.sort_values('score', ascending=True)
print dfc.head()
# Pick one index at random in these 30%
rint = np.random.random_integers(lg_dim+1)-1
# print rint

# Reset index
dfc.reset_index(inplace=True)
id_q = dfc.iloc[rint].id
question = df.iloc[id_q].question


print question

"""
Collection data
"""
# Collect the grade for the question
new_grade = -1
df.set_value(id_q,'score', new_grade)
# Collect notes
new_notes = 'a'
print df.loc[id_q]['notes']
df.set_value(id_q,'notes', (list(df.loc[id_q]['notes'])).append(new_notes))

# Write changes
df.to_csv(basedir + '/../data/question_db.csv', index=False)
