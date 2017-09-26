import os
import sys
import pandas as pd
import numpy as np
basedir = os.path.abspath(os.path.dirname(__file__))


def getquestion():
	df = pd.read_csv(basedir + '/../data/question_db.csv')
	# print df.head()

	dfc = df.copy()
	dimension = len(dfc['score'])
	# Consider the 50% of questions with the lowest grades
	lg_dim = int(np.floor(0.5 * dimension))
	# print lg_dim
	dfc = dfc.sort_values('score', ascending=True)
	print dfc.head()
	# Pick one index at random in these 30%
	rint = np.random.random_integers(lg_dim + 1) - 1
	# print rint

	# Reset index
	dfc.reset_index(inplace=True)
	id_q = dfc.iloc[rint].id
	print "id_q after reset index in getquestion() = " + str(id_q)
	question = df.iloc[id_q].question

	# Write changes
	df.to_csv(basedir + '/../data/question_db.csv', index=False)

	return question, id_q


def collectfeedback(id_q, new_grade, new_notes):
    # basedir = os.path.abspath(os.path.dirname(__file__))
    df = pd.read_csv(basedir + '/../data/question_db.csv')

    # Store the grade for the question
    df.set_value(id_q, 'score', new_grade)
    # Store the notes
    old_notes = df.loc[id_q]['notes']
    # if len(old_notes) > 0:
    upd_notes = old_notes + ' ' + new_notes
    # else:
    #     upd_notes = new_notes
    df.set_value(id_q, 'notes', upd_notes)
    df.to_csv(basedir + '/../data/question_db.csv', index=False)

# if __name__ == '__main__':
# 	question, id_q = getquestion()
# 	# return question, id_q
# 	# print question
# 	# print id_q
#   	id_q = 1
#     new_grade = 8
#     new_notes = 'Versatile language.'
#     df = pd.read_csv(basedir + '/../data/question_db.csv')
#     print df.iloc[id_q]['notes']
#     print df.iloc[id_q]['score']
#     collectfeedback(id_q, new_grade, new_notes)
#     print df.iloc[id_q]['notes']
#     print df.iloc[id_q]['score']
	
