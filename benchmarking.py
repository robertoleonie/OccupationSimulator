from statistics import mean, variance
import matplotlib.pyplot as plt
import pandas as pd
import approaches

class Benchmarking():
    def __init__(self):
        self.apps = approaches.Approaches()

    def completely_random_metrics(self, positions, rounds=1000):
        self._round_steps_random = []

        for _ in range(rounds):
            steps = self.apps.completely_random(positions)
            self._round_steps_random.append(steps)
        
        sample_mean = mean(self._round_steps_random)
        sample_var = variance(self._round_steps_random)
        sample_sd = sample_var ** (1/2)

        return sample_mean, sample_var, sample_sd
    
    def individualist_metrics(self, positions, rounds=1000):
        self._round_steps_individualist = []

        for _ in range(rounds):
            steps = self.apps.individualist(positions)
            self._round_steps_individualist.append(steps)
        
        sample_mean = mean(self._round_steps_individualist)
        sample_var = variance(self._round_steps_individualist)
        sample_sd = sample_var ** (1/2)

        return sample_mean, sample_var, sample_sd
    
    def altruistic_metrics(self, positions, rounds=1000):
        self._round_steps_altruistic = []

        for _ in range(rounds):
            steps = self.apps.altruistic(positions)
            self._round_steps_altruistic.append(steps)
        
        sample_mean = mean(self._round_steps_altruistic)
        sample_var = variance(self._round_steps_altruistic)
        sample_sd = sample_var ** (1/2)

        return sample_mean, sample_var, sample_sd
    
    def cleaner_metrics(self, positions, rounds=1000):
        self._round_steps_cleaner = []

        for _ in range(rounds):
            steps = self.apps.cleaner(positions)
            self._round_steps_cleaner.append(steps)
        
        sample_mean = mean(self._round_steps_cleaner)
        sample_var = variance(self._round_steps_cleaner)
        sample_sd = sample_var ** (1/2)

        return sample_mean, sample_var, sample_sd
    
    def discomfort_optimization_metrics(self, positions, rounds=1000):
        self._round_steps_discomfort = []

        for _ in range(rounds):
            steps = self.apps.discomfort_optimization(positions, positions//2)
            self._round_steps_discomfort.append(steps)
        
        sample_mean = mean(self._round_steps_discomfort)
        sample_var = variance(self._round_steps_discomfort)
        sample_sd = sample_var ** (1/2)

        return sample_mean, sample_var, sample_sd

class Simulation():
    def __init__(self):
        self._benchmarking = Benchmarking()
        self.app = ['completamente aleatória', 'individualista', 'altruística', \
                    'faxineiro', 'otimização do incômodo']

    def all_means(self, positions):
        completely_random_sample_mean = self._benchmarking.completely_random_metrics(positions)[0]
        individualist_sample_mean = self._benchmarking.individualist_metrics(positions)[0]
        altruistic_sample_mean = self._benchmarking.altruistic_metrics(positions)[0]
        cleaner_sample_mean = self._benchmarking.cleaner_metrics(positions)[0]
        discomfort_optimization_sample_mean = self._benchmarking.discomfort_optimization_metrics(positions)[0]

        return completely_random_sample_mean, individualist_sample_mean, altruistic_sample_mean, \
            cleaner_sample_mean, discomfort_optimization_sample_mean

    def all_variances(self, positions):
        completely_random_sample_var = self._benchmarking.completely_random_metrics(positions)[1]
        individualist_sample_var = self._benchmarking.individualist_metrics(positions)[1]
        altruistic_sample_var = self._benchmarking.altruistic_metrics(positions)[1]
        cleaner_sample_var = self._benchmarking.cleaner_metrics(positions)[1]
        discomfort_optimization_sample_var = self._benchmarking.discomfort_optimization_metrics(positions)[1]

        return completely_random_sample_var, individualist_sample_var, altruistic_sample_var, \
            cleaner_sample_var, discomfort_optimization_sample_var

    def all_std_devs(self, positions):
        completely_random_sample_sd = self._benchmarking.completely_random_metrics(positions)[2]
        individualist_sample_sd = self._benchmarking.individualist_metrics(positions)[2]
        altruistic_sample_sd = self._benchmarking.altruistic_metrics(positions)[2]
        cleaner_sample_sd = self._benchmarking.cleaner_metrics(positions)[2]
        discomfort_optimization_sample_sd = self._benchmarking.discomfort_optimization_metrics(positions)[2]

        return completely_random_sample_sd, individualist_sample_sd, altruistic_sample_sd, \
            cleaner_sample_sd, discomfort_optimization_sample_sd

    def all_metrics(self, n_inputs):
        cols = ['Posições', 'Abordagem', 'Tempo Médio', 'Variância do tempo', 'Desvio padrão do tempo']
        df = pd.DataFrame(columns=cols)

        for n in n_inputs:
            for ap in range(5):
                new_line = {cols[0]: n, cols[1]: self.app[ap], cols[2]: round(self.all_means(n)[ap], 3), \
                        cols[3]: round(self.all_variances(n)[ap], 3), cols[4]: round(self.all_std_devs(n)[ap], 3)}
                print(new_line)
                df.loc[len(df)] = new_line

        df.to_csv('all_metrics.csv', sep=',', index=False, encoding='latin-1')

class Plot():
    def __init__(self, n_inputs):
        self.sim = Simulation()
        self.n_inputs = n_inputs

        self._apps = {i: self.sim.app[i] for i in range(5)}
        self._structures = {self.sim.app[i]: f"x{i}" for i in range(5)}

        self.x0 = []
        self.x1 = []
        self.x2 = []
        self.x3 = []
        self.x4 = []
        self.generate_all_data()

    def generate_paired_data(self, first_approach:str, second_approach:str):
        first_structure = self._structures[first_approach]
        second_structure = self._structures[second_approach]

        if first_structure == second_structure:
            raise ValueError("Impossível comparar uma mesma abordagem duas vezes.")

        self.first_data = getattr(self, first_structure, None)
        self.second_data = getattr(self, second_structure, None)

    def generate_all_data(self):
        for n in self.n_inputs:
            means = list(self.sim.all_means(n))  # Convertendo a tupla para lista
            self.x0.append(means[0])
            self.x1.append(means[1])
            self.x2.append(means[2])
            self.x3.append(means[3])
            self.x4.append(means[4])

    def draw_paired_graphics(self, first_data:str, second_data:str):
        self.generate_paired_data(first_data, second_data)

        plt.figure(figsize=(10, 6))

        plt.plot(self.n_inputs, self.first_data, label=first_data, alpha=0.7)
        plt.plot(self.n_inputs, self.second_data, label=second_data, alpha=0.7)

        plt.xlabel("Entrada n de capacidade da instalação")
        plt.ylabel("Tempo médio de execução")
        plt.title(f"Gráfico comparativo das abordagens {first_data} e {second_data}")
        plt.legend()
        plt.grid(True)
        plt.show()

    def draw_all_line_graphics(self):
        plt.figure(figsize=(10, 6))

        plt.plot(self.n_inputs, self.x0, label=self.sim.app[0], alpha=0.7)
        plt.plot(self.n_inputs, self.x1, label=self.sim.app[1], alpha=0.7)
        plt.plot(self.n_inputs, self.x2, label=self.sim.app[2], alpha=0.7)
        plt.plot(self.n_inputs, self.x3, label=self.sim.app[3], alpha=0.7)
        plt.plot(self.n_inputs, self.x4, label=self.sim.app[4], alpha=0.7)

        plt.xlabel("Entrada n de capacidade da instalação")
        plt.ylabel("Tempo médio de execução")
        plt.title("Gráfico comparativo para todas as abordagens")
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    n_inputs = [1, 2, 3, 5, 10, 20, 30, 50, 100, 200, 300, 500, 1000]

    plot = Plot(n_inputs)
    plot.draw_all_line_graphics()
    plot.draw_paired_graphics('completamente aleatória', 'individualista')
    plot.draw_paired_graphics('completamente aleatória', 'altruística')
    plot.draw_paired_graphics('completamente aleatória', 'faxineiro')
    plot.draw_paired_graphics('completamente aleatória', 'otimização do incômodo')

    sim = Simulation()
    sim.all_metrics(n_inputs)

main()
