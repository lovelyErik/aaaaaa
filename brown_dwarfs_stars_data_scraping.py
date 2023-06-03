from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Nota importante: la página dada en el URL se mantiene por "wikipedia", por lo que puede ser actualizada en el futuro; en consecuencia, los datos actuales pueden ser diferentes
# ¡Realiza la extracción de datos desde cero utilizando etiquetas HTML / nombres de clases!


# URL para extraer datos
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

# Obtener la página
page = requests.get(url)

# Analizar la página
soup = bs(page.text,'html.parser')

# Obtener <table> con class = 'wikitable sortable'
star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)


temp_list= []

# Nota importante: la página en el enlace dado es mantenida por "wikipedia" y puede ser actualizada en el futuro
# Por lo tanto, verifica la propiedad del número de índice para star_table[1]
# Actualmente, sólo hay tres tablas con class = "class":"wikitable sortable" y la tabla "Field brown dwarfs" es la segunda tabla
# Por lo que el índice es 1
table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

# Convertir a CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")
