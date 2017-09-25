import os
import sys
import pandas as pd
import numpy as np
basedir = os.path.abspath(os.path.dirname(__file__))


def collectfeedback(id_q, new_grade, new_notes):
    # basedir = os.path.abspath(os.path.dirname(__file__))
    df = pd.read_csv(basedir + '/../data/question_db.csv')

    # Store the grade for the question
    df.set_value(id_q, 'score', new_grade)
    # Store the notes
    old_notes = df.loc[id_q]['notes']
    # if 
    #     upd_notes = str(old_notes) + new_notes
    # else:
    #     upd_notes = new_notes
    df.set_value(id_q, 'notes', upd_notes)
    df.to_csv(basedir + '/../data/question_db.csv', index=False)


if __name__ == '__main__':
    id_q = 1
    new_grade = 8
    new_notes = 'Versatile language.'
    df = pd.read_csv(basedir + '/../data/question_db.csv')
    print df.iloc[id_q]['notes']
    print df.iloc[id_q]['score']
    collectfeedback(id_q, new_grade, new_notes)
    print df.iloc[id_q]['notes']
    print df.iloc[id_q]['score']
