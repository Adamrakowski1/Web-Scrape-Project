from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

table = soup.find('table', class_='wikitable sortable')

headers = [header.text.strip() for header in table.find_all('th')] # Strips the headers of any uneccessary things

# Convert the table into a dataframe
rows = table.find_all('tr') # Finds all the tr tags in the source code
table_data = [] # Creates a new list
for row in rows[1:]:  # Skip the header row, as we only want the data
    cols = row.find_all('td') # Gets the data from the td tags from the table
    cols = [col.text.strip() for col in cols] # Strips down the table data, removing spaces and other unecessary things
    table_data.append(cols) # Adds that data to the list we made before

# Create a dataframe from the table data
df = pd.DataFrame(table_data, columns=headers) 

# Strips the column names of any uneccessary things such as spaces, /n, empty space
df.columns = df.columns.str.replace(r'\n', '', regex=True).str.strip()

# Create a new dataframe, using the df we made before, with the headers 'Revenue (USD millions)' and 'Employees'
df_filtered = df[['Revenue (USD millions)', 'Employees']]

# Export the filtered dataframe to CSV
df_filtered.to_csv(r'/Users/adamrakowski/Desktop/Companies_filtered.csv', index=False)





