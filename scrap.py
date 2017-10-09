import os
from bs4 import BeautifulSoup, NavigableString, Tag
from urllib import urlopen
from selenium import webdriver
import pandas as pd

basedir = os.path.abspath(os.path.dirname(__file__))


def routine():
    url = 'https://developers.google.com/machine-learning/glossary/?utm_campaign=Data%2BElixir&utm_medium=email&utm_source=Data_Elixir_151#model'
    driver = webdriver.Chrome('/Users/Marc/bin/chromedriver')
    driver.get(url)
    html_source = driver.page_source
    driver.quit()

    f = open('gloss_db.csv', 'wb')
    import csv
    with open('gloss_db.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        sp = BeautifulSoup(html_source, "html.parser")
        # print sp
        items = sp.find_all(attrs={"class": "hide-from-toc"})
        for header in items:
            nextNode = header
            text = ''
            while True:
                nextNode = nextNode.nextSibling
                if nextNode is None:
                    break
                if isinstance(nextNode, NavigableString):
                    print(nextNode.strip())
                    text = text + ' ' + nextNode.strip()
                if isinstance(nextNode, Tag):
                    if nextNode.name == "h2":
                        print header.contents[0].decode('utf-8')
                        # print text
                        csvwriter.writerow([header.contents[0].decode(
                            'utf-8'), unicode(text).encode('utf-8')])
                        break
                    # print (nextNode.get_text(strip=True).strip())
                    text = text + ' ' + nextNode.get_text(strip=True).strip()

    # thing = items[0].contents[:]
    # thing = items[0].contents
    # print thing
    # print items


def convert2q():
    df = pd.read_csv(basedir + '/data/gloss_db.csv')
    df['id'] = df.index
    df = df.rename(columns={'keyword': 'question', 'definition': 'notes'})
    df['score'] = -1
    df['question'] = df['question'].apply(lambda x: "Define what is " + x)
    print df.head()
    df.to_csv(basedir + '/data/gloss_db.csv', index=False)

if __name__ == '__main__':
    # routine()
    convert2q()
