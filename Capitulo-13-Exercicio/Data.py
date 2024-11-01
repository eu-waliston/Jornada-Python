import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo CSV
df = pd.read_csv('airline-safety.csv')

# Exibindo as primeiras linhas do DataFrame
data = {
    'airline': df['airline'],
    'avail_seat_km_per_week': df['avail_seat_km_per_week'],
    'incidents_85_99': df['incidents_85_99'],
    'fatal_accidents_85_99': df['fatal_accidents_85_99'],
    'fatalities_85_99': df['fatalities_85_99'],
    'incidents_00_14': df['incidents_00_14'],
    'fatalities_85_99': df['fatalities_85_99'],
    'incidents_00_14': df['incidents_00_14'],
    # 'fatal_accidents_00_1' : df['fatal_accidents_00_1'],
    'incidents_00_14': df['incidents_00_14'],
    'fatal_accidents_00_14': df['fatal_accidents_00_14'],
    'fatalities_00_14': df['fatalities_00_14']
}
df = pd.DataFrame(data)

# Dados para o gráfico
labels = ['airline', 'avail_seat_km_per_week', 'incidents_85_99', 'fatal_accidents_85_99', 'fatalities_85_99',
          'incidents_00_14',
          'fatalities_85_99',
          'incidents_00_14',
          'incidents_00_14',
          'fatal_accidents_00_14',
          'fatalities_00_14']
sizes = [15, 30, 45, 10, 5, 56,45,87,10,34,45]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'violet', 'lightcoral', 'lightskyblue', 'lightcoral' , 'violet','violet', 'lightskyblue','gold',]
explode = (0.1, 0, 0, 0, 0,0,0,0,0,0,0)  # Destacar a primeira fatia

# Criando o gráfico de pizza
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=120)

plt.title('Acidentes aereos: Porcentagem de acidentes fatais')
plt.axis('equal')  # Igualar o eixo para um gráfico circular
plt.show()
