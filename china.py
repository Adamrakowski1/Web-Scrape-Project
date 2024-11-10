from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/world-population/china-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

table = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')

headers = [header.text.strip() for header in table.find_all('th')]

df = pd.DataFrame(columns = headers)

column_data = table.find_all('tr')

for row in column_data[1:]:
	row_data = row.find_all('td')
	individual_row_data = [data.text.strip() for data in row_data]
	length = len(df)
	df.loc[length] = individual_row_data

df.to_csv(r'/Users/adamrakowski/Desktop/ChinaFull_filtered.csv', index=False)


#Fertility rate change by year
rows = table.find_all('tr')

fertility = []
for row in rows[1:]:  
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    fertility.append(cols)

df2 = pd.DataFrame(fertility, columns=headers)

df2.columns = df2.columns.str.replace(r'\n', '', regex=True).str.strip()

fertilityDf = df2[['Year', 'Fertility Rate']]

fertilityDf.to_csv(r'/Users/adamrakowski/Desktop/China_fertility.csv', index=False)

#Population pop % by year

rows = table.find_all('tr')

urbanPercent = []
for row in rows[1:]:  
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    urbanPercent.append(cols)

df3 = pd.DataFrame(urbanPercent, columns=headers)

df3.columns = df3.columns.str.replace(r'\n', '', regex=True).str.strip()

urbanDf = df3[['Year', 'Urban Pop %']]

urbanDf.to_csv(r'/Users/adamrakowski/Desktop/China_urban_pop_%.csv', index=False)

#Yearly change in population #

rows = table.find_all('tr')

popPercent = []
for row in rows[1:]:  
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    popPercent.append(cols)

df4 = pd.DataFrame(popPercent, columns=headers)

df4.columns = df4.columns.str.replace(r'\n', '', regex=True).str.strip()

popDf = df4[['Year', 'Yearly %  Change']]

popDf.to_csv(r'/Users/adamrakowski/Desktop/China_change_pop_%.csv', index=False)