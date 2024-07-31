import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import approaches
import json

class FOBenchmarking() :
    def __init__(self, n_inputs) :
        self._n_inputs = n_inputs
        self._apps = approaches.Approaches()
        self.approaches_data = {}
        self.approaches_data['completamente aleatoria'] = {}
        self.approaches_data['individualista'] = {}
        self.approaches_data['altruistica'] = {}
        self.approaches_data['individualista-altruistica'] = {}
        self.approaches_data['otimizacao do incomodo'] = {}

    def transform_data(self, data, divide=False):
        self.transformed_data = {}

        for approach, values in data.items():
            self.transformed_data[approach] = {}
            
            for key, value_list in values.items():
                # Convertir a lista de valores em uma lista de pares índice:valor
                key_int = int(key)  # Converter a chave para inteiro
                if divide :
                    new_list = {i: round(value_list[i] / i, 3) if i != 0 else 0 for i in range(len(value_list))}
                else :
                    new_list = {i: value_list[i] if i != 0 else 0 for i in range(len(value_list))}
                
                # Adicionar zeros para garantir que todos os índices até o máximo estão presentes
                for i in range(len(value_list)):
                    if i not in new_list:
                        new_list[i] = 0
                
                self.transformed_data[approach][key_int] = new_list

        self.approaches_data = self.transformed_data

    def get_discomfort_data(self, transform=True) :
        for n in self._n_inputs :
            _, _, self.approaches_data['completamente aleatoria'][n] = self._apps.completely_random(n, occupyAll=True)
            _, _, self.approaches_data['individualista'][n] = self._apps.individualist(n, occupyAll=True)
            _, _, self.approaches_data['altruistica'][n] = self._apps.altruistic(n, occupyAll=True)
            _, _, self.approaches_data['individualista-altruistica'][n] = self._apps.individualist_altruistic(n, occupyAll=True)
            _, _, self.approaches_data['otimizacao do incomodo'][n] = self._apps.discomfort_optimization(n, users=n)

        if transform :
            self.transform_data(self.approaches_data, divide=False)

        # print(self.approaches_data)
        with open('dicionario.json', 'w') as f:
            json.dump(self.approaches_data, f)

    def get_approach_data(self, approach:str) :
        return self.approaches_data[approach]

class Plot() :
    def __init__(self, n_inputs) :
        self._n_inputs = n_inputs
        self._fob = FOBenchmarking(self._n_inputs)
        self._fob.get_discomfort_data()
        self._approach_per_time_data = self._fob.get_approach_data('individualista-altruistica')
        print('Dados de incômodo gerados.')

    def heatmaps(self):
        # Define os nomes das abordagens
        approaches = [
            'completamente aleatoria',
            'individualista',
            'altruistica',
            'individualista-altruistica',
            'otimizacao do incomodo'
        ]
        
        for approach in approaches:
            data = self._fob.approaches_data[approach]
            df = pd.DataFrame.from_dict(data, orient='index')
            
            # Configure o estilo do seaborn
            sns.set(style='white', palette='deep')
            
            plt.figure(figsize=(8, 6))
            sns.heatmap(df, cmap='YlGnBu', annot=True, fmt='.2f', cbar=True, linewidths=0.5)
            plt.title(f'Heatmap - {approach}')
            plt.xlabel('Inputs')
            plt.ylabel('Inputs')
            plt.xticks(ticks=range(len(df.columns)), labels=df.columns, rotation=45)
            plt.yticks(ticks=range(len(df.index)), labels=df.index, rotation=0)
            
            # Salva cada heatmap em um arquivo separado
            plt.tight_layout()
            plt.savefig(f'heatmap_{approach}.png')
            plt.show()
            plt.close()

    def get_data_for_CI(self) :
        return self._approach_per_time_data

def main() :
    n_inputs = [1, 2, 3, 5, 10, 20, 30, 50, 100, 200, 300, 500, 1000]
    plot = Plot(n_inputs)
    # plot.heatmaps()

main()