import pandas as pd
import os
import matplotlib.pyplot as plt

## laczenie plikow csv
df = pd.read_csv('Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv')


files = [file for file in os.listdir('Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv('Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/' + file)
    all_months_data = pd.concat([all_months_data, df])


#Wczytanie wszystkich danych do jednego pliku
    #all_months_data.to_csv("all_data.csv", index=False)

all_data = pd.read_csv("Pandas-Data-Science-Tasks-master/all_data.csv")


#oczyszczanie danych
nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

#dodawnie kolumny 'Month'
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')


#dodawanie kolumny 'Sales'
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

#Jaki był najlepszy miesiąc pod względem sprzedaży?

###Odkomentuj poniższy blok aby zobaczyć rezultat###
#results = all_data.groupby('Month').sum()
#plt.ticklabel_format(style='plain')
#months = range(1,13)
#plt.bar(months, results['Sales'])
#plt.xticks(months)
#plt.ylabel('Sales $')
#plt.xlabel('Month number')
#plt.tight_layout()
#plt.show()


#Jakie miasto sprzedało najwięcej produktów?
def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]


all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ')')

###Odkomentuj poniższy blok aby zobaczyć rezultat###
results = all_data.groupby('City').sum()
plt.ticklabel_format(style='plain')
cities = [city for city, df in all_data.groupby('City')]
plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation='vertical', size=8)
plt.ylabel('Sales $')
plt.xlabel('City name')
plt.tight_layout()
plt.show()

#skończone na 52:15 


