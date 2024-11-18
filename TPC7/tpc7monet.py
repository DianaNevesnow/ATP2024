# Function to read meteorological data from a CSV file and store it in a list of dictionaries
def read_meteo_data(file_path):
    data = []
    file = open(file_path, 'r')
    headers = file.readline().strip().split(',')
    for linha in file:
        values = linha.strip().split(',')
        entry = {headers[i]: values[i] for i in range(len(headers))}
        data.append(entry)
    file.close()
    return data

# Function to generate plots for minimum, maximum temperatures and precipitation
def plot_meteo_data(data):
    min_temps = [float(entry['TempMin']) for entry in data]
    max_temps = [float(entry['TempMax']) for entry in data]
    precipitations = [float(entry['Precipitation']) for entry in data]
    days = [entry['Day'] for entry in data]

    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))
    plt.plot(days, min_temps, label='Temperatura Mínima', color='blue')
    plt.plot(days, max_temps, label='Temperatura Máxima', color='red')
    plt.bar(days, precipitations, label='Pluviosidade', color='green', alpha=0.3)

    plt.xlabel('Dias')
    plt.ylabel('Valores')
    plt.title('Gráficos de Temperatura e Pluviosidade')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to save meteorological data to a JSON file
def save_data_to_json(data, output_file):
    import json
    json_file = open(output_file, 'w')
    json.dump(data, json_file, indent=4)
    json_file.close()

# Sample execution
file_path = 'dados_meteo.csv'  # Example CSV file
output_file = 'dados_meteo.json'

meteo_data = read_meteo_data(file_path)
if len(meteo_data) > 0:
    plot_meteo_data(meteo_data)
    save_data_to_json(meteo_data, output_file)
    print("Dados salvos no arquivo JSON.")
else:
    print("Não há dados para processar.")
