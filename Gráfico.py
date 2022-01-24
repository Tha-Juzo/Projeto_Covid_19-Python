#Biblioteca para criar um dataframe (Planilha) dentro do python
import pandas as pd

#Biblioteca para plotar os gráficos
import seaborn as sns
import matplotlib.pyplot as plt


covid = pd.read_csv('Dados-covid-19-municipios.csv', sep = ';', encoding='latin-1')


covid.head()


municipios = covid.query('Município == "Araraquara" | Município == "Bauru"')


fig, (axis1) = plt.subplots(1, 1, figsize=(15, 5))
axis1 = sns.barplot(x = 'Município', y = 'Mun_Total de casos', data = municipios, ax = axis1, palette = 'mako')
axis1.set_title('Casos da Covid 19 por Municipio', fontsize=25, pad=25)
axis1.set_ylabel("Total de Casos", fontsize=18)
axis1.set_xlabel("Município", fontsize=18)


fig, (axis1) = plt.subplots(1, 1, figsize=(15, 5))
axis1 = sns.barplot(x = 'Município', y = 'Mun_Total de óbitos', data = municipios, ax = axis1, palette = 'mako')
axis1.set_title('Óbitos da Covid 19 por Municipio', fontsize=25, pad=25)
axis1.set_ylabel("Total de Óbitos", fontsize=18)
axis1.set_xlabel("Município", fontsize=18)

plt.show()