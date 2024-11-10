import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Companies visualization

df = pd.read_csv(r'/Users/adamrakowski/Desktop/Companies_filtered.csv')
df['Revenue (USD millions)'] = pd.to_numeric(df['Revenue (USD millions)'].str.replace(',', '').str.strip(), errors='coerce') # Converts the objects in the csv to integers, specifically the revenue objects 
df['Employees'] = pd.to_numeric(df['Employees'].str.replace(',', '').str.strip(), errors='coerce') # Converts the objects in the csv to integers, specifically the employees objects
df.plot(y='Revenue (USD millions)', x='Employees', kind='scatter', title = 'Does the Revenue of a Company Depend on the # of Employees?', s = 25, c = 'Red') # Creates the Scatter Plot
plt.show()

#China Fertility visualization

fertilityDf = pd.read_csv(r'/Users/adamrakowski/Desktop/China_fertility.csv')
fertilityDf = fertilityDf.sort_values(by='Year', ascending=True)
ax = fertilityDf.plot(x='Year', y='Fertility Rate', kind='line', title='China Fertility Rate Since 1955', color='blue')
ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])
ax.set_yticklabels(['0.0', '0.5', '1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5','5.0','5.5','6.0','6.5','7.0'])
plt.show()

#china urban population #

urbanDf = pd.read_csv(r'/Users/adamrakowski/Desktop/China_urban_pop_%.csv')
urbanDf['Urban Pop %'] = pd.to_numeric(urbanDf['Urban Pop %'].str.replace('%', ''), errors='coerce') 
ax2 = urbanDf.plot(x='Year', y='Urban Pop %', kind='line', title='China Urban Population % Since 1955', color='purple')
ax2.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax2.set_yticklabels([str(i) for i in range(0, 101, 10)])
plt.show()

#china change in population %

popDf = pd.read_csv(r'/Users/adamrakowski/Desktop/China_change_pop_%.csv')
popDf.columns = popDf.columns.str.strip()
popDf['Yearly %  Change'] = pd.to_numeric(popDf['Yearly %  Change'].str.replace('%', '').str.replace(',', ''), errors='coerce')
popDf['Year'] = pd.to_numeric(popDf['Year'], errors='coerce')
fig, ax3 = plt.subplots()
popDf.plot(x='Year', y='Yearly %  Change', kind='line', title='China Population Growth % Since 1955', color='red', ax=ax3)
ax3.set_ylim([-1, 3])  
ax3.axhline(0, color='black',linewidth=1)
plt.show()
