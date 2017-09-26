import os
import sys
import pandas as pd
import numpy as np

def getquestion():
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

	# Write changes
	df.to_csv(basedir + '/../data/question_db.csv', index=False)

	return question, id_q

if __name__ == '__main__':
	question, id_q = getquestion()
	return question, id_q
	# print question
	# print id_q

	